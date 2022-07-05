import json
from htmlslacker import HTMLSlacker


def explorer_layout_view(is_movies: bool = True, results=None):
    if results is None:
        results = []

    title = f"{'Movies' if is_movies else 'Tv Shows'}"
    total = len(results)

    blocks = [
        {
            "dispatch_action": True,
            "type": "input",
            "block_id": "input_query",
            "element": {
                "type": "plain_text_input",
                "action_id": f"{'movies' if is_movies else 'shows'}_explorer_search-action"
            },
            "label": {
                "type": "plain_text",
                "text": "Search",
                "emoji": True
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"We found *{total} {title}* Results"
            }
        },
        {
            "type": "divider"
        },
    ]

    if total > 0:
        for idx, x in enumerate(results):
            blocks.append(single_movie_view(x) if is_movies else single_show_view(x))
            if idx + 1 != len(results):
                blocks.append({
                    "type": "divider"
                })
    else:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Please type to start searching"
            }
        })

    blocks = json.dumps(blocks)

    return {
        "type": "modal",
        "callback_id": "explorer_modal",
        "title": {"type": "plain_text", "text": f"Explore {title}"},
        "close": {"type": "plain_text", "text": "Cancel"},
        "blocks": blocks
    }


def single_show_view(result):
    show = result['show']
    name = show['name']
    summary = show['summary']
    link = show['officialSite']
    alternate_link = show['url']
    rating = show['rating']['average']
    image = show['image']

    if image is not None:
        if 'medium' in image:
            image = image['medium']
    else:
        image = 'https://pbs.twimg.com/profile_images/1027586212234768385/c0hzVIBb_400x400.jpg'

    summary = HTMLSlacker(summary if summary is not None else '').get_output()

    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*<{link if link is not None else alternate_link}|{name}>*\n{summary}\nRated: {rating}"
        },
        "accessory": {
            "type": "image",
            "image_url": image,
            "alt_text": ""
        }
    }


def single_movie_view(result):
    title = result['title']
    year = result['year']
    poster = result['poster']
    poster = f"{poster if poster is not None else ''}"

    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*{title}*\n\nYear: {year}"
        },
        "accessory": {
            "type": "image",
            "image_url": poster,
            "alt_text": ""
        }
    }
