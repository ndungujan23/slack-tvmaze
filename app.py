import logging
from os import environ
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from lib.layout.home import home_layout as home_view_layout
from lib.layout.menu import menu_layout_view
from lib.layout.explorer import explorer_layout_view
from lib.handler import action_movies_main, action_shows_main, action_search_changed

load_dotenv()
logging.basicConfig(level=logging.INFO)

app = App(
    token=environ.get('SLACK_BOT_TOKEN', None),
    signing_secret=environ.get('SLACK_SIGNING_SECRET', ''),
)


# logger middleware
@app.middleware
def logger_middleware(logger, body, next):
    logger.debug(body)
    next()


@app.event('app_home_opened')
def home_opened_handler(client, event, logger):
    try:
        # views.publish is the method that your app uses to push a blocks to the Home tab
        client.views_publish(
            # the user that opened your app's app home
            user_id=event["user"],
            # the blocks object that appears in the app home
            view=home_view_layout()
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


@app.command('/tvmaze')
def main_command(command, ack, client, logger, respond):
    logger.info(command)
    ack()

    option = f"{command['text']}".lower().lstrip()
    command_options = ['movie', 'movies', 'show', 'shows', '']
    error = {
        "response_type": "ephemeral",
        "text": f"Sorry, slash commando, option `{option}` doesn't exist. "
                "Please try `shows` or `movies` as options."
    }

    view = menu_layout_view()
    if option not in command_options:
        respond(error)
    else:
        if option == 'movie' or option == 'movies':
            view = explorer_layout_view()
        elif option == 'show' or option == 'shows':
            view = explorer_layout_view(False)
        else:
            view = menu_layout_view()

    client.views_open(trigger_id=command["trigger_id"], view=view)


# Main modal navigation handlers including their shortcuts
app.action('movies_explorer_modal')(action_movies_main)
app.shortcut('movies_explorer_modal')(action_movies_main)
app.action('shows_explorer_modal')(action_shows_main)
app.shortcut('shows_explorer_modal')(action_shows_main)
# Input changed handler
app.action('movies_explorer_search-action')(action_search_changed)
app.action('shows_explorer_search-action')(action_search_changed)


if __name__ == "__main__":
    handler = SocketModeHandler(app, environ.get('APP_TOKEN', None))
    handler.start()
