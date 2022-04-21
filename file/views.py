import json
import requests
from flask import request, current_app

from file import file_blue
from utils import get_header

limit = 10
select = "id,name,size,folder,image,video,lastModifiedDateTime"
graph_url = 'https://graph.microsoft.com/v1.0/'


@file_blue.route('/')
def file_list():
    path = request.values.get("path")
    if path:
        drive = current_app.config.get('DRIVE_ID')
        path = "drives/{}/root:/{}:/children".format(drive, path)
    else:
        path = "me/drive/root/children"
    url = graph_url + path
    url = "{}?$top={}&$select={}".format(url, limit, select)
    data = requests.get(url, headers=get_header()).json()
    items = []
    for item in data["value"]:
        result = {}
        if "folder" in item:
            result["type"] = "folder"
            result["childCount"] = item["folder"]["childCount"]
        elif "image" in item:
            result["type"] = "picture"
        elif "video" in item:
            result["type"] = "play-square"
        else:
            result["type"] = "file"
        result["id"] = item["id"]
        result["name"] = item["name"]
        result["size"] = item["size"]
        result["time"] = item["lastModifiedDateTime"]
        items.append(result)
    response = {"data": items, "next": data.get("@odata.nextLink")}
    return json.dumps(response)
