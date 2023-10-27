import os
from sanic import Sanic
from urllib.parse import urljoin
from facebook import FacebookInput


async def handler(message) -> None:
    return message.upper()


app = Sanic(__name__)

facebook = FacebookInput(
    fb_verify=os.getenv("FB_VERIFY"), 
    fb_secret=os.getenv("FB_SECRET"), 
    fb_access_token=os.getenv("FB_ACCESS_TOKEN"),
)

p = urljoin("/webhooks/", facebook.url_prefix())
app.blueprint(facebook.blueprint(handler), url_prefix=p)
