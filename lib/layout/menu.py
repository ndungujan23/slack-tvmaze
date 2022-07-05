def menu_layout_view():
    return {
        "type": "modal",
        "callback_id": "main_menu_modal",
        "title": {"type": "plain_text", "text": "Explore"},
        "close": {"type": "plain_text", "text": "Cancel"},
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "emoji": True,
                    "text": "Welcome to the unofficial TVMaze slack app"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "emoji": True,
                    "text": "\n"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "emoji": True,
                    "text": "\n"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<https://www.tvmaze.com/|TVMaze>*\nUnofficial slack app that helps you find data about "
                            "movies, tv shows and the good stuff 😉 "
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://pbs.twimg.com/profile_images/1027586212234768385/c0hzVIBb_400x400.jpg",
                    "alt_text": "logo thumbnail"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "emoji": True,
                    "text": "\n"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*What would you like to checkout? 🕵️‍♂️*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Movies*\nFind popular, latest and search for movies"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Choose"
                    },
                    "value": "movies_btn",
                    "action_id": "movies_explorer_modal"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Tv Shows*\nFind popular, latest and search for TV Shows"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Choose"
                    },
                    "value": "tv_shows_btn",
                    "action_id": "shows_explorer_modal"
                }
            }
        ]
    }
