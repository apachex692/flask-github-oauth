# Author: Sakthi Santhosh
# Created on: 08/09/2023
from flask import render_template, redirect, request, session, url_for
from os import getenv
from requests import get, post

from lib import app_handle

@app_handle.route('/')
def index_handle():
    return render_template("index.html")

@app_handle.route("/oauth/request")
def oauth_request_handle():
    return redirect(
        f"""https://github.com/login/oauth/authorize?client_id={getenv('GITHUB_OAUTH_CLIENT_ID')}&scope=repo"""
    )

@app_handle.route("/oauth/callback")
def oauth_callback_handle():
    code = request.args.get(key="code")
    with post(
        url="https://github.com/login/oauth/access_token",
        data={
            "client_id": getenv("GITHUB_OAUTH_CLIENT_ID"),
            "client_secret": getenv("GITHUB_OAUTH_CLIENT_SECRET"),
            "code": code
        },
        headers={"Accept": "application/json"}
    ) as request_handle:
        session["access_token"] = request_handle.json()["access_token"]

    return redirect(url_for("list_pub_repos_handle"))

@app_handle.route("/pub_repos")
def list_pub_repos_handle():
    with get(
        url=f"https://api.github.com/repos/{getenv('GITHUB_USERNAME')}/{getenv('GITHUB_REPOSITORY')}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {session['access_token']}",
        }
    ) as request_handle:
        response = request_handle.json()

    session.pop("access_token")
    return response
