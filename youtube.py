#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import pprint

from apiclient.discovery import build
from apiclient.errors import HttpError

try:
    from settings_api import DEVELOPER_KEY
except:
    DEVELOPER_KEY = '' # Устанавливаем свой ключ

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(search_query, max_result=50):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )
    search_parts = [
        'id',
    ]
    details_parts = [
        'snippet',
        'contentDetails',
        # 'fileDetails',
        # 'player',
        # 'processingDetails',
        # 'recordingDetails',
        'statistics',
        'status',
        # 'suggestions',
        # 'topicDetails',
    ]
    search_response = youtube.search(

    ).list(
        q=search_query,
        part=",".join(search_parts),
        maxResults=max_result,
        type='video'
    ).execute()

    for search_result in search_response.get("items", []):

        video_id = search_result['id']['videoId']
        item = youtube.videos().list(
            id=video_id,
            part=','.join(details_parts)
        ).execute()

        # comments = youtube.comment().list(
        #     id=video_id
        # ).execute()
        # pprint.pprint(comments)

        yield item



if __name__ == "__main__":
    for item in youtube_search(
        search_query='Как стараться?',
        max_result=1
    ):
        pprint.pprint(item)