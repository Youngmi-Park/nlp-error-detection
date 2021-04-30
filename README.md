# nlp-error-detection

### 1. 위키피디아 영어 덤프 파일 다운로드
wiki english
link: https://dumps.wikimedia.org/enwiki/

enwiki-latest-pages-articles.xml.bz2 파일 사용
해당 파일은 xml 파일이기 때문에 텍스트 형식의 파일로 변환 필요하다.
*일반 문서의 최신 버전만이 묶여 있고, 전체 편집 역사는 들어있지 않습니다. 대부분 이 파일을 이용하면 된다.*

### 2. 위키 덤프파일 파싱
덤프 파일을 다운로드 받고 위키피디아 덤프 파일을 텍스트 형식으로 변환시켜주는 오픈소스인 ‘위키피디아 익스트랙터’를 사용하여 데이터 전처리 과정을 거친다.
git hub: https://github.com/nawnoes/WikiExtractor

위키피디아 익스트랙터와 위키피디아 한국어 덤프 파일을 동일한 디렉토리 경로에 두고, 아래 명령어를 실행시키면 위키피디아 덤프 파일이 텍스트 파일로 변환된다.


```shell
$ python wikiextractor/WikiExtractor.py enwiki-latest-pages-articles.xml.bz2
```
- html 태그 제거
- 본문에 아무것도 없는 경우 건너뛰기



텍스트 파일로 변환된 위키피디아 덤프는 총 15개의 디렉토리로 구성
아티클 수:
67456047 The Underdog (1943 film)



 AA ~ GB 디렉토리로 각 디렉토리 내에는 wiki_00 ~ wiki_99라는 파일들이 들어있다. 각 파일들을 열어보면 이와 같은 구성이 반복되고 있다.
AA ~ AF 안의 wiki_00 ~ wiki_99 파일들을 word2vec의 편의를 위해 하나의 텍스트 파일로 통합할 것이다. (만약, 더 간단히 하고 싶다면 모든 디렉토리를 통합하지 않고, 하나의 디렉토리 내의 파일들에 대해서만 해도 통합 작업을 진행하면 속도를 단축시킬 수 있다. 하지만 보통 학습 데이터의 양이 많을 수록 Word2Vec의 성능이 올라가기 때문에 성능은 전체 파일에 대해서 진행한 경우보다 좋지 않을 수 있다.)
그럼 이제 AA ~ AG 안의 모든 wiki_00 ~ wiki_99 파일들을 하나의 텍스트 파일로 모으는 작업을 진행해보도록 하자. 작업은 각 디렉토리의 파일에 대해서 우선적으로 하나의 파일로 만든 다음에, 그렇게 생긴 7개의 파일을 하나의 파일로 만드는 순서로 진행할 것이다.

find . -name 'wiki*' -type f -exec cat {} + > output.txt
현재 디렉토리 경로 기준으로 하위 디렉토리 포함 경로 내 모든 텍스트 파일을 출력하는 명령어
output.txt 에 출력한 모든 텍스트가 저장되어 하나로 합쳐지게 된다.

 | xargs cat > [결과파일명]
이제 모든 텍스트 파일을 하나로 만든 훈련 데이터가 완성되었다.


3.vocab 만들기
BERT 학습을 위한 vocab을 만들기

https://blog.nerdfactory.ai/2019/04/25/learn-bert-with-colab.html





BERT참고자료
https://ebbnflow.tistory.com/151
https://velog.io/@jinml/BERT
https://codlingual.tistory.com/98
https://blog.nerdfactory.ai/2019/04/25/learn-bert-with-colab.html
https://dacon.io/codeshare/1918
https://tutorials.pytorch.kr/intermediate/dynamic_quantization_bert_tutorial.html
http://blog.naver.com/PostView.nhn?blogId=jeanmy1102&logNo=221749234951

python WikiExtractor.py enwiki-latest-pages-articles.xml.bz2
