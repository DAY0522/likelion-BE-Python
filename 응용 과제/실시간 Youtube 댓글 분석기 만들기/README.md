# 실시간 유튜브 댓글 분석기

파이썬 파일 이름과 라이브러리 이름이 같아서 파일을 실행하는데 오류가 발생
해결 방법: 파일 이름을 라이브러리 이름과 다르게 수정 (wordcloud -> word_cloud)

파일 실행 순서
: youtube_info.py -> comments_frequency.py -> wordcloud.py

youtube_info.py : 유튜브 정보 불러오는 파일
comments_frequency.py : 댓글을 불러와 형태소 분석을 하여, 빈도수를 세는 파일
word_cloud.py : wordcloud 라이브러리를 이용해 빈도수에 따른 이미지를 저장해주는 파일


Youtube_info.py
1.API 클라이언트 객체 생성(이때 api_key.py에 있는 내용을 가져와서 developerKey 할당) 
2.가져올 동영상의 ID 입력
3.동영상 정보 가져오기("videos.list" 메서드를 사용. 'snippet':문자열을 전달 'statistics': 통계)
4.조회수, 좋아요, 댓글 수 가져오기
5.영상 제목,영상 설명, 채널명 가져오기
6.최상위 댓글 100개 가져오기(commit_thread리스트 생성등)
7.결과 출력(최상위댓글 제외)

commets_frequency.py( Youtube_info.py 의 commit_thread 리스트 import )
1.모든 댓글 저장
2.형태소 분석
3.명사 빈도수 세기

word_cloud.py(commets_frequency.py의 frequency import)
빈도수의 따라 각 단어의 크기가 정해진
단어구름 생성!

!!개발 중 발견하게 된 오류사항 및 해결방법!!

1. worldcloud관련 ipmort에러가 발생! 
원인: 단어구름 생성파일이름을 wordcloud.py 로 이름지었는데 이것이 라이브러리 woldcloud 이름이 같아서 발생하는 문제!
해결방법: wordcloud.py ->word_cloud.py 로 바꿈 

