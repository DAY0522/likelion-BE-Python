from googleapiclient.discovery import build
from konlpy.tag import Okt
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import pprint
import googleapiclient.discovery
import os

f = open('./멋사플젝중요.txt','r', encoding='UTF-8')

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = f.read()


# API 클라이언트 객체 생성
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

# 가져올 동영상의 ID 입력
video_id = "MAfpmKrAejs"

# 동영상 정보 가져오기
video_response = youtube.videos().list(
    part="snippet, statistics",
    id=video_id
).execute()

# 조회수, 좋아요, 댓글 수 가져오기
view_count = video_response["items"][0]["statistics"]["viewCount"]
like_count = video_response["items"][0]["statistics"]["likeCount"]
comment_count = video_response["items"][0]["statistics"]["commentCount"]

# 영상 제목, 영상 설명, 채널명 가져오기
video_title = video_response["items"][0]["snippet"]["title"]
video_description = video_response["items"][0]["snippet"]["description"]
channel_title = video_response["items"][0]["snippet"]["channelTitle"]

# 최상위 댓글 100개 가져오기
comment_threads = []
nextPageToken = ''
while len(comment_threads) < 100:
    results = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        pageToken=nextPageToken,
        maxResults=100
    ).execute()

    for item in results["items"]:
        comment_threads.append(item)

    if 'nextPageToken' in results:
        nextPageToken = results['nextPageToken']
    else:
        break

# 최상위 댓글 출력
for comment_thread in comment_threads:
    comment = comment_thread["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    author = comment_thread["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
    print("작성자:", author)
    print("내용:", comment)
    print("----------------------------------------")


# 결과 출력
print("제목:", video_title)
print("조회수:", view_count)
print("좋아요:", like_count)
print("댓글 수:", comment_count)
print("설명:", video_description)
print("채널명:", channel_title)

f.close()