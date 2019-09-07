import os
import telegram
from dotenv import load_dotenv

import utils


def post_to_channel(post):
    bot = telegram.Bot(os.environ["TELEGRAM_TOKEN"])
    bot.send_message(chat_id=os.environ["CHANNEL_ID"], text=open(post["txt"]).read())
    bot.send_photo(chat_id=os.environ["CHANNEL_ID"], photo=open(post["img"], "rb"))
    return None


if __name__ == "__main__":

    load_dotenv()

    directory = utils.get_directory()
    try:
        post = utils.get_post(directory)
    except FileNotFoundError as error:
        exit(error)
    except KeyError as error:
        exit(f"{error} is unsupported file format")

    try:
        post_to_channel(post)
    except (telegram.error.NetworkError, telegram.error.TelegramError) as error:
        exit(error)
