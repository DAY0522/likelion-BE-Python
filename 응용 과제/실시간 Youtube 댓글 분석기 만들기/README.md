# 실시간 유튜브 댓글 분석기

파이썬 파일 이름과 라이브러리 이름이 같아서 파일을 실행하는데 오류가 발생
해결 방법: 파일 이름을 라이브러리 이름과 다르게 수정 (wordcloud -> word_cloud)

파일 실행 순서
: youtube_info.py -> comments_frequency.py -> wordcloud.py

youtube_info.py : 유튜브 정보 불러오는 파일
comments_frequency.py : 댓글을 불러와 형태소 분석을 하여, 빈도수를 세는 파일
word_cloud.py : wordcloud 라이브러리를 이용해 빈도수에 따른 이미지를 저장해주는 파일
