import os
import dotenv
from sanic import Sanic
from urllib.parse import urljoin
from typing import Text, Dict, Any, Optional

from facebook import FacebookInput


# loading the .env file
dotenv.load_dotenv()


def handler(message: Text, metadata: Optional[Dict[Text, Any]]) -> None:
    return f"This is auto answer for question: {message}"


app = Sanic(__name__)

facebook = FacebookInput(
    fb_verify=os.getenv("FB_VERIFY"), 
    fb_secret=os.getenv("FB_SECRET"), 
    fb_access_token=os.getenv("FB_ACCESS_TOKEN"),
)

p = urljoin("/webhooks/", facebook.url_prefix())
app.blueprint(facebook.blueprint(handler), url_prefix=p)
