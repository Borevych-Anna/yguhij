import emoji


def show_emoji():
    message = emoji.emojize(
        "Python is fun! :snake: :rocket: :smile:",
        language="alias"
    )

    print(message)