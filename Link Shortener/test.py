import dotenv, os
from praw import Reddit

dotenv.load_dotenv()


SECRET = os.getenv("CLIENT_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")


bot = Reddit()