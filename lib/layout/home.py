def home_layout():
    return {
        "type": "home",
        "callback_id": "home_view",
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
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": "Note: All command options provided below are optional and just shortcuts :)",
                        "emoji": True
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "\n"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*1️⃣ Use the `/tvmaze movies` command*.\nType `/tvmaze movies` "
                            "to search and explore popular, upcoming and latest movies. Try it out by using "
                            "the `/tvmaze movies` command (also shown below). "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "\n"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*2️⃣ Use the `/tvmaze shows` command*.\nType `/tvmaze shows` "
                            "to search and explore popular, upcoming and latest Tv Shows. Try it out by using "
                            "the `/tvmaze shows` command (also shown below). "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "\n"
                }
            }
        ]
    }
