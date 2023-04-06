from konlpy.tag import Komoran
from youtube_info import comment_threads

# 모든 댓글 저장
comments = []
for comment_thread in comment_threads:
    comment = comment_thread["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    comments.append(comment)

# 형태소 분석
Komoran = Komoran()
words = []
for c in comments:
    try:
        words += Komoran.nouns(c)
    except: # nouns 함수 내에서 에러 발생한 경우
        continue

# 빈도수 세기
frequency = {}
for w in words:
    try:
        frequency[w] += 1
    except:
        frequency[w] = 1

print(frequency)