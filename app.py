"""Mostly a copy of https://help.pythonanywhere.com/pages/RedirectWebApp/."""
import os
from urllib.parse import urlparse, urlunparse

from flask import Flask, redirect, request
from waitress import serve

TO_DOMAIN = "online.sqlfluff.com"

app = Flask(__name__)


@app.before_request
def redirect_to_new_domain():
    """Do the redirection."""
    urlparts = urlparse(request.url)
    urlparts_list = list(urlparts)
    urlparts_list[1] = TO_DOMAIN
    return redirect(urlunparse(urlparts_list), code=301)


if __name__ == "__main__":
    print("Serving production!")
    serve(app, host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
