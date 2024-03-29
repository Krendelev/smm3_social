import os
import requests
from dotenv import load_dotenv

import utils


def check_vk_response(response):
    if "error" in response:
        raise requests.HTTPError(response["error"]["error_msg"])
    return None


def get_upload_url(payload):
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    params = {**payload, "group_id": os.environ["VK_GROUP_ID"]}
    response = requests.get(url, params=params).json()
    check_vk_response(response)
    return response["response"]["upload_url"]


def upload_picture(url, image):
    files = {"photo": image}
    response = requests.post(url, files=files).json()
    check_vk_response(response)
    return response


def save_picture(payload, upload_info):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        **payload,
        "group_id": os.environ["VK_GROUP_ID"],
        "server": upload_info["server"],
        "photo": upload_info["photo"],
        "hash": upload_info["hash"],
    }
    response = requests.post(url, params=params).json()
    check_vk_response(response)
    return response["response"][0]


def post_to_wall(payload, pic_info, message):
    url = "https://api.vk.com/method/wall.post"
    params = {
        **payload,
        "owner_id": f"-{os.environ['VK_GROUP_ID']}",
        "from_group": 1,
        "message": message,
        "attachments": f"photo{pic_info['owner_id']}_{pic_info['id']}",
    }
    response = requests.get(url, params=params).json()
    check_vk_response(response)
    return None


def post_to_group(post):
    payload = {"access_token": os.environ["VK_ACCESS_TOKEN"], "v": 5.101}
    upload_url = get_upload_url(payload)
    with open(post["txt"]) as text, open(post["img"], "rb") as photo:
        upload_info = upload_picture(upload_url, photo)
        picture_info = save_picture(payload, upload_info)
        post_to_wall(payload, picture_info, text.read())
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
