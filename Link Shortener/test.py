import dotenv
import os
import json
from praw import Reddit, reddit
dotenv.load_dotenv()


SECRET = os.getenv("CLIENT_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")
USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
USER_AGENT = "reddit automatic poster and commenter by u/VeryToastyMicrowave"

SUBREDDIT_JSON = "./subs.json"

TITLE = ''
URL = ''
COMMENT = """"""


def post_to_sub(sub_name, reddit_instance, flair=None):
    subreddit = reddit.Subreddit(reddit_instance, display_name=sub_name)
    if subreddit.user_is_banned:
        remove_from_json(sub_name, True)
        print(f"User is banned in {sub_name}, moved to banned_in")
    else:
        if flair is not None:
            flairs = list(subreddit.flair.link_templates.user_selectable())
            for flair_data in flairs:
                if flair_data["flair_text"].lower().startswith(flair):
                    flair_id = flair_data["flair_template_id"]
        else:
            flair_id = None
        submission = subreddit.submit(
            title=TITLE, url=URL, nsfw=True, flair_id=flair_id)
        return submission


def reply_to_post(submission):
    submission.reply(COMMENT)


def remove_from_json(sub_name, move_to_banned, json_location=SUBREDDIT_JSON):
    with open(SUBREDDIT_JSON, "r+", encoding="utf-8") as file:
        file_dict = json.loads(file.read())
        file.seek(0)
        flair = file_dict["working_subreddits"].pop(sub_name)
        if move_to_banned:
            file_dict["banned_in"][sub_name] = flair
        file.write(json.dumps(file_dict, indent=2))
        file.truncate()


bot = Reddit(client_id=CLIENT_ID, client_secret=SECRET, username=USERNAME,
             password=PASSWORD, user_agent=USER_AGENT, ratelimit_seconds=120)

with open(SUBREDDIT_JSON, encoding="utf-8") as file:
    subs = json.loads(file.read())["working_subreddits"]

for sub in subs:
    try:
        post = post_to_sub(sub, bot, subs[sub])
        reply_to_post(post)
    except Exception as e:
        remove_from_json(sub, False)
        print(f"{sub} either banned or privated, removed from working_subreddits")

