import os
import requests
from dotenv import load_dotenv

import utils


def post_to_group(post):
    url = f"https://graph.facebook.com/{os.environ['FB_GROUP_ID']}/photos"

    with open(post["txt"]) as text, open(post["img"], "rb") as photo:
        params = {"caption": text.read(), "access_token": os.environ["FB_MARKER"]}
        files = {"source": photo}
        response = requests.post(url, params=params, files=files)
    response.raise_for_status()
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
        post_to_group(post)
    except requests.HTTPError as error:
        exit(error)
