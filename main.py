import os
import logging
import requests
import telegram
from dotenv import load_dotenv

import vk
import fb
import tgram
import utils

logging.basicConfig(
    filename="post.log",
    filemode="w",
    format="%(asctime)s:%(message)s",
    level=logging.ERROR,
)

directory = utils.get_directory()

try:
    post = utils.get_post(directory)
except FileNotFoundError as error:
    exit(error)
except KeyError as error:
    exit(f"{error} is unsupported file format")

load_dotenv()
try:
    vk.post_to_group(post)
except requests.HTTPError as error:
    logging.error(error)

try:
    fb.post_to_group(post)
except requests.HTTPError as error:
    logging.error(error)

try:
    tgram.post_to_channel(post)
except (telegram.error.NetworkError, telegram.error.TelegramError) as error:
    logging.error(error)
