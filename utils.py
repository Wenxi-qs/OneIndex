from flask import current_app


def get_header():
    access_token = current_app.config.get('ACCESS_TOKEN')
    return {
        "Authorization": "bearer {}".format(access_token),
        "Content-Type": "application/json"
    }
