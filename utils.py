import os
import argparse


def get_post(directory):
    formats = {".jpg": "img", ".png": "img", ".gif": "img", ".txt": "txt"}
    file_names = [name for name in os.listdir(directory) if not name.startswith(".")]
    post = {
        formats[os.path.splitext(name)[1]]: os.path.join(directory, name)
        for name in file_names
    }
    return post


def get_directory():
    parser = argparse.ArgumentParser(
        description="""Make post to VKontakte, Facebook and Telegram.
                    Place text and image to be posted in directory and provide its name as an argument.
                    Text should be in TXT format and image can be JPG, PNG or GIF."""
    )
    parser.add_argument("dir", help="Name of the directory containing your post")
    return parser.parse_args().dir
