# nlp-error-detection

BERT를 활용한 오타 감지 및 수정 작업<br>
음성인식 결과를 단순 NLP로 보고 처리해보자!

<hr>

### 1. 위키피디아 영어 덤프 파일 다운로드
[wiki english](https://dumps.wikimedia.org/enwiki/)

enwiki-latest-pages-articles.xml.bz2 사용

해당 파일은 xml 파일이기 때문에 텍스트 형식의 파일로 변환 필요하다.
<small>*일반 문서의 최신 버전만이 묶여 있고, 전체 편집 역사는 들어있지 않다. 대부분 이 파일을 이용하면 된다.*</small>
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
in
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
<img width="55%" src="https://user-images.githubusercontent.com/53163222/118373803-a1bb0200-b5f3-11eb-86a6-965e1c933930.png">
</p>
어떤 문장이 입력으로 들어오면 공백을 기준으로 자르고 각각의 단어를 Bert 모델에서 인식하는 [Mask] 토큰으로 바꿔서 문장 세트를 만든다. 
<p align="center">
각 단어를 Masking 처리한 문장 세트<br><br>
<img width="38%" src="https://user-images.githubusercontent.com/53163222/118373831-cca55600-b5f3-11eb-9e69-e518ec3c50d2.png">
<br>
<img width="30%" src="https://user-images.githubusercontent.com/53163222/118373869-f5c5e680-b5f3-11eb-85ad-9f8e8782b405.png"><br>
</p>

학습 데이터: Book corpus, English Wikipedia<br>
<small>*이 모델에 사용된 학습 데이터가 상당히 중립적이라 할 수 있더라도 편향된 예측을 가질 수 있다*</small>
<p align="center">
<img width="40%" src="https://user-images.githubusercontent.com/53163222/118373885-0c6c3d80-b5f4-11eb-92a3-bf5a2290012d.png">
</p>

### Spell Checker

<p align="center">
<img width="90%" src="https://user-images.githubusercontent.com/53163222/118373919-3aea1880-b5f4-11eb-8c83-8edaadfc5586.png"><br>
<img width="50%" src="https://user-images.githubusercontent.com/53163222/118373923-3de50900-b5f4-11eb-9cf7-28912189a7a7.png"><br>
<img width="90%" src="https://user-images.githubusercontent.com/53163222/118373925-3faecc80-b5f4-11eb-9575-2a985a9903e7.png"><br>
<img width="90%" src="https://user-images.githubusercontent.com/53163222/118373929-42112680-b5f4-11eb-8013-4e64d12b0a60.png"><br>
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

두단어의 유사도는

(longerLength - getDistance(longer, shorter)) / (double) longerLength; 이다.

두 단어 s1, s2를 비교할 때 두 개의 For문을 돌면서 문자열을 비교하는데, 만약 s1[n] == s2[m] 이라면 변경에 필요한 거리는 0이 된다.
아니라면, 대체, 삽입, 수정 중에서 가장 최소의 비용이 되는 방법을 고른다. 이렇게 해서 쌓은 코스트를 배열에 저장하고 맨마지막 값을 리턴한다.

### Spell checker와 Masked LM 결합
- Method1: Spell Checker 에서 오타가 발견되면 문장을  Masked LM에 넣고 spell checker에서 나온 옳은 단어 후보 세트를 찾아  score를 확인
- Method2: masked language model의 결과에서 input word와 edit distance와 score를 고려하여 단어 찾기

![image](https://user-images.githubusercontent.com/53163222/118665891-ad920880-b82d-11eb-9603-48889e25341f.png)

이 방법은 문장에서 한 개의 단어에만 오타가 있는 경우에는 문제가 없지만, 2개 이상의 단어에 오타가 있는 경우, Masked LM에서 주변의 틀린 단어로 [MASK]에 들어갈 단어를 예측하기 때문에 잘못된 결과가 도출될 가능성이 있다.

**= 우선 1개의 단어에 오타가 있는 경우만 해결하는 것 부터 진행**


### 테스트 문장
발음이 헷갈릴 법한 단어 위주로 선정
동음이자 (Homophone, Heterograph): 동일한 발음을 가졌지만 철자가 다른 단어


### 실제 음성 인식 결과 돌려보기
#### 1. 유튜브 자동 생성 자막
유튜브 음성을 텍스트로 변환하는 작업(자동 자막)
TED 강연이 원본 script를 제공하기 때문에 처리한 텍스트와 비교가 용이할 것으로 생각함.
TED 강연 영상 중 하나를 임의로 선택해서 유튜브에서 제공하고 있는 기존 자동 생성 자막 서비스를 이용해 텍스트로 변환(자막 다운로드 사이트 이용)

→ 원본 스크립트, 자동생성 자막 다운(txt 파일

#### 2. Deep Speech 결과 
[Libri speech](https://www.openslr.org/12) 2620개 음성으로 테스트(test-clean)


<hr>

## 수정 사항

### 1. Deep Speech 결과로 먼저 테스트 진행
### 2. edit distance에서 sound base edit distance로 변경
- eudex와 soudex 중에서 eudex 선택
<p>
굳이 같은 항목을 비교하는데 여러 method를 사용하지말고 한 가지만 선택하여 비교해도 될 것으로 판단하였고,  eudex가 soudnex보다 구체적인 비교가 가능하기 때문에 eudex를 선택함.<br>
 sound distance는 eudex와 soundex 인코딩 결과를 이진수로 변환하고 각자리를 비교했을 때 다르면 1 같으면 0으로 계산
  <img width="50%" src="https://user-images.githubusercontent.com/53163222/128687041-0fb830c3-9082-4a5c-930f-78a66f48d565.png">
 <img width="50%" src="https://user-images.githubusercontent.com/53163222/128687405-b71aa6fc-b4a9-474a-b9a7-62bafe68bf6a.png">
 </p>
 
- score 순위와 eudex 순위 merge
  - index base, 평균으로 1차 merge
  - 추후 가중치를 주어 세부 조정하여 성능을 개선할 예정

### 3. 테스트 문장 선택
테스트하는데 vocab자체에 없는 단어라면 masked language model이 찾지못한다는 문제가 있고 wer측정에 오차가 있을 가능성이 있다..
테스트할 문장을 거르기위해서 테스트 문장의 단어들이 vocab에 있는 단어인지 아닌지 찾는 작업을 진행한다.

### 4. 사전에 없는 단어 처리



### To Do
- it's, won't와 같은 축약형태 처리
- 학습되지 않은 단어들


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
