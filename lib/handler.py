from lib.layout.explorer import explorer_layout_view
from lib.api import Api


def action_movies_main(ack, body, client, logger):
    logger.info(body)
    ack()

    trigger_id = body["trigger_id"],
    view_id = body["view"]["id"]
    vhash = body["view"]["hash"]

    client.views_update(
        trigger_id=trigger_id,
        # Pass the view_id
        view_id=view_id,
        # String that represents view state to protect against race conditions
        hash=vhash,
        # View payload with updated blocks
        view=explorer_layout_view()
    )


def action_shows_main(ack, body, client, logger):
    logger.info(body)
    ack()

    trigger_id = body["trigger_id"],
    view_id = body["view"]["id"]
    vhash = body["view"]["hash"]

    client.views_update(
        trigger_id=trigger_id,
        # Pass the view_id
        view_id=view_id,
        # String that represents view state to protect against race conditions
        hash=vhash,
        # View payload with updated blocks
        view=explorer_layout_view(False)
    )


def action_search_changed(ack, body, client, logger):
    logger.info(body)

    api = Api()
    is_movies = False
    query = None

    for i in body['actions']:
        if i['action_id'] == 'movies_explorer_search-action':
            is_movies = True
            query = f"{i['value']}".lstrip()
        elif i['action_id'] == 'shows_explorer_search-action':
            is_movies = False
            query = f"{i['value']}".lstrip()

    ack()

    if is_movies:
        results = api.search_movie(query)
    else:
        results = api.search_show(query)

    client.views_update(
        # Pass the view_id
        view_id=body["view"]["id"],
        # String that represents view state to protect against race conditions
        hash=body["view"]["hash"],
        # View payload with updated blocks
        view=explorer_layout_view(is_movies, results)
    )
