# nlp-error-detection

### 1. 위키피디아 영어 덤프 파일 다운로드
wiki english
link: https://dumps.wikimedia.org/enwiki/

enwiki-latest-pages-articles.xml.bz2 파일 사용

해당 파일은 xml 파일이기 때문에 텍스트 형식의 파일로 변환 필요하다.
*일반 문서의 최신 버전만이 묶여 있고, 전체 편집 역사는 들어있지 않다. 대부분 이 파일을 이용하면 된다.*

<br>

### 2. 위키 덤프파일 파싱

덤프 파일을 다운로드 받고 위키피디아 덤프 파일을 텍스트 형식으로 변환시켜주는 오픈소스인 ‘위키피디아 익스트랙터’를 사용하여 데이터 전처리 과정을 거친다.
git hub: https://github.com/nawnoes/WikiExtractor

위키피디아 익스트랙터와 위키피디아 한국어 덤프 파일을 동일한 디렉토리 경로에 두고, 아래 명령어를 실행시키면 위키피디아 덤프 파일이 텍스트 파일로 변환된다.

```shell
$ python wikiextractor/WikiExtractor.py enwiki-latest-pages-articles.xml.bz2
```

- html 태그 제거
- 본문에 아무것도 없는 경우 건너뛰기

<wikipedia 구성><br>
Directory: 15(AA ~ GB)<br>
File: wiki_00 ~ wiki_99<br>
Article: 67456047<br>

각 디렉토리 내에 있는 wiki_00 ~ wiki_99 파일들을 편의를 위해 하나의 텍스트 파일로 통합한다.

```shell
$ find . -name 'wiki*' -type f -exec cat {} + > enwiki.txt
```

현재 디렉토리 경로 기준으로 하위 디렉토리 포함 경로 내 모든 텍스트 파일을 출력하는 명령어<br>
enwiki.txt 에 출력한 모든 텍스트가 저장되어 하나로 합쳐지게 된다.

<br>

### 3.vocab 만들기

BERT 학습을 위한 vocab을 만들기<br>

https://blog.nerdfactory.ai/2019/04/25/learn-bert-with-colab.html



### 4. Masking Language Model using Bert base uncased - word prediction
[huggingface transformers](https://pytorch.org/hub/huggingface_pytorch-transformers/)
모델 가져오기 – 파이프라인으로 직접 사용가능
<p align="center">
<img width="60%" src="https://user-images.githubusercontent.com/53163222/118373803-a1bb0200-b5f3-11eb-86a6-965e1c933930.png">
</p>
어떤 문장이 입력으로 들어오면 공백을 기준으로 자르고 각각의 단어를 Bert 모델에서 인식하는 [Mask] 토큰으로 바꿔서 문장 세트를 만든다. 

<p align="center">
<img width="40%" src="https://user-images.githubusercontent.com/53163222/118373823-c1522a80-b5f3-11eb-8ac4-efd2671a2032.png">
</p>
<br>
<p align="center">
각 단어를 Masking 처리한 문장 세트<br><br>
<img width="38%" src="https://user-images.githubusercontent.com/53163222/118373831-cca55600-b5f3-11eb-9e69-e518ec3c50d2.png">
</p>

학습 데이터: Book corpus, English Wikipedia<br>
*이 모델에 사용된 학습 데이터가 상당히 중립적이라 할 수 있더라도 편향된 예측을 가질 수 있다*

<p style="display: inline" >
<img width="40%" src="https://user-images.githubusercontent.com/53163222/118373869-f5c5e680-b5f3-11eb-85ad-9f8e8782b405.png"><br>
<img width="40%" src="https://user-images.githubusercontent.com/53163222/118373885-0c6c3d80-b5f4-11eb-92a3-bf5a2290012d.png">
</p>
<p style="display: inline">
<img width="40%" src="https://user-images.githubusercontent.com/53163222/118373872-f8284080-b5f3-11eb-976c-c56bf6f3103b.png">
</p>

### Spell Checker
<p align="center">
<img src="https://user-images.githubusercontent.com/53163222/118373919-3aea1880-b5f4-11eb-8c83-8edaadfc5586.png"><br>
<img width="60%" src="https://user-images.githubusercontent.com/53163222/118373923-3de50900-b5f4-11eb-9cf7-28912189a7a7.png"><br>
<img src="https://user-images.githubusercontent.com/53163222/118373925-3faecc80-b5f4-11eb-9575-2a985a9903e7.png"><br>
<img src="https://user-images.githubusercontent.com/53163222/118373929-42112680-b5f4-11eb-8013-4e64d12b0a60.png"><br>

</p>


### Edit Distance (Levenshtein distance)
두 String의 유사도를 측정해보자

두 개의 String이 있을때, 그 두개를 비교하는 작업은 어떻게 할 수 있을까? str.equalsOf(str2) 이런 것이 아니라, 두 단어의 비슷한 정도를 말하는 것이다.
단어간 유사도 구하기
Levenshtein Distance (Edit Distance): 두 문자열 간의 차이를 거리로 계산하는 방법
하나의 문자열 S를 수정하여 다른 문자열 T로 변환시키고자 할 때,삽입(insert), 삭제(delete), 대체(substitute) 연산이 사용된다. S를 T로 변환시키는데 필요한 최소의 편집 연산 횟수를 편집 거리라고 한다.

다른 방식도 고려해보았으나 Hamming Distance의 경우 길이가 같은 두 단어에서 몇개를 대체하면 같아지는지 계산하기 때문에 적용하기 어려울 것으로 판단해 Edit Distance로 선택

<p align="center">
<img width="80%" src="https://user-images.githubusercontent.com/53163222/118350804-a3ed7400-b593-11eb-9487-35ca3f9503e9.png">
</p>
그 과정은 딱 3개다. 새로운걸 삽입(insertion), 기존의 원소를 삭제(deletion), 기존의 원소를 다른 것으로 대체(substitution) 

예를 들어

ghost > toast

g를 t로 대체한다 (subsitution) thost > toast
h를 o로 대체한다 (subsitution) toost > toast
o를 a로 대체한다 (subsitution) toast = toast!
이런 과정을 거치면, ghost와 toast의 거리는 3이 되는 것이다.

이제 느낌을 보면 알겠지만, 두 단어의 거리는 둘 중에 가장 긴 단어의 거리가 최대다. (zzz > effoooooooooooort를 비교한다고 생각해보자)

그렇기 때문에, 두단어의 유사도는

return (longerLength - getDistance(longer, shorter)) / (double) longerLength; 이렇게 나올 것이다.

이것을 알고리즘으로 구성하기 위한 단계를 다시 한번 생각해보자.

두 단어 = s1, s2

길이 = s1.length, s2.length

두개 배열의 For문을 같이 돈다.
만약 s1[n] == s2[m] 이라면 변경에 필요한 거리는 0이 된다.
그렇지 않다면, 대체, 삽입, 수정 중에서 가장 최소의 비용이 되는 방법을 고른다.
이렇게 해서 쌓은 코스트를 배열에 저장한다.
맨마지막 값을 리턴한다.


### Edit Distance 참고자료

https://en.wikipedia.org/wiki/Levenshtein_distance <br>
https://tomining.tistory.com/175 <br>
https://yceffort.kr/2018/05/31/Levenshtein-distance
https://stackoverflow.com/questions/2460177/edit-distance-in-python#


### BERT참고자료

https://ebbnflow.tistory.com/151 <br>
https://velog.io/@jinml/BERT <br>
https://codlingual.tistory.com/98 <br>
https://blog.nerdfactory.ai/2019/04/25/learn-bert-with-colab.html <br>
https://dacon.io/codeshare/1918 <br>
https://tutorials.pytorch.kr/intermediate/dynamic_quantization_bert_tutorial.html <br>
http://blog.naver.com/PostView.nhn?blogId=jeanmy1102&logNo=221749234951 <br>