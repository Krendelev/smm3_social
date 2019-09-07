# Social media poster

Post to [VKontakte](https://vk.com), [Facebook](https://facebook.com) and [Telegram](https://telegram.org/) at once.

### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Put all your credentials into the `.env` file in the working directory. Place text and image to be posted in a directory. Text should be in `txt` format and image can be `jpg`, `png` or `gif`. Run `main.py` with directory name as an argument or run each script separately.

```bash
$ python main.py my_post
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
