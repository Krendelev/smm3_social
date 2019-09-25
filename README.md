[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8f52980688da44b195bdd1f4d66de65c)](https://www.codacy.com/manual/Krendelev/smm3_social?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Krendelev/smm3_social&amp;utm_campaign=Badge_Grade)

# Social media poster

Post to [VKontakte](https://vk.com), [Facebook](https://facebook.com) and [Telegram](https://telegram.org/) all at once.

## How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Create groups at FB and VK and Telegram channel. Put all your credentials into the `.env` file in the working directory like this:

```bash
FB_MARKER=replace_with_marker
FB_GROUP_ID=replace_with_group_id
TELEGRAM_TOKEN=replace_with_token
CHANNEL_ID=-replace_with_channel_id
VK_ACCESS_TOKEN=replace_with_token
VK_GROUP_ID=replace_with_group_id
```

Place text and image to be posted in a directory. Text should be in `txt` format and image can be `jpg`, `png` or `gif`. Run `main.py` with directory name as an argument or run each script separately.

```bash
$ python main.py my_post
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
