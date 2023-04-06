from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
from api_key import key

DEVELOPER_KEY = key # 유튜브 API 키 값
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
    q="달라스튜디오", # 채널 이름 입력
    order="relevance",
    part="snippet",
    maxResults=50
).execute()

channel_id = search_response['items'][0]['id']['channelId']

playlists = youtube.playlists().list(
    channelId=channel_id,
    part="snippet",
    maxResults=20
).execute()

ids = []
titles = []
for i in playlists['items']:
    ids.append(i['id'])
    titles.append(i['snippet']['title'])

df = pd.DataFrame([ids, titles]).T
df.columns = ['PlayLists', 'Titles']

print(df)

nego = df['PlayLists'][2]
playlist_videos = youtube.playlistItems().list(
    playlistId=nego,
    part="snippet",
    maxResults=50,
)
playlistitems_list_response = playlist_videos.execute()

video_names = []
video_ids = []
date = []

for v in playlistitems_list_response['items']:
    video_names.append(v['snippet']['title'])
    video_ids.append(v['snippet']['resourceId']['videoId'])
    date.append(v['snippet']['publishedAt'])

vdf = pd.DataFrame([date, video_names, video_ids]).T
vdf.columns = ['Date', 'Title', 'IDS']

print(vdf['Title'])