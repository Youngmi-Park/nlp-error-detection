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



### 4. Edit Distance (Levenshtein distance)
두 String의 유사도를 측정해보자

두 개의 String이 있을때, 그 두개를 비교하는 작업은 어떻게 할 수 있을까? str.equalsOf(str2) 이런 것이 아니라, 두 단어의 비슷한 정도를 말하는 것이다.

![image](https://user-images.githubusercontent.com/53163222/118350804-a3ed7400-b593-11eb-9487-35ca3f9503e9.png)
나의 저질 발음으로 인해, 안타깝게도 toast를 인식하지 못하고 저렇게 다섯 개의 후보를 주고 말았다. 그렇다면 나는, 내가 가지고 있는 DB의 데이터 중에서 가장 post와 유사한 단어를 찾아서 돌려줘야 한다.

그렇다면, 내가 가지고 있는 DB의 단어와 구글이 return한 단어는 어떻게 비교할 수 있을까? 정확히 말하면, 두개의 String의 유사도는 어떻게 판단할 수 있을까?

Levenshtein Distance : The minimum number of single-character edits required to change one word into the other. Strings do not have to be the same length
– 한 글자 글자의 차이(삽입, 삭제, 대체) 를 거리로 계산한다.
Hamming Distance : The number of characters that are different in two equal length strings.
– 길이가 같은 두 단어에서 몇개를 대체하면 같아지는지 계산한다. 근데 이미 길이가 같아야 한다는 전재가 있으므로 글러먹음.
Smith–Waterman : A family of algorithms for computing variable sub-sequence similarities.
– 배열들의 가능한 모든 길이로 쪼개서 비교하는 방식
Sørensen–Dice Coefficient : A similarity algorithm that computes difference coefficients of adjacent character pairs.
– 배열들의 쌍을 묶어보면서 비교하는 방식
정도가 있다.  그중에서 가장 접근하고 이해하기 쉬운 Levenshtein distance 에 대해 알아보고자 한다.

두 배열을 비교하기위해서는, 두 배열이 같아지는 과정이 얼마나 필요한지 (거리가 어떻게 되는지) 구하는 과정을 거치면 된다.

그 과정은 딱 3개다. 새로운걸 삽입(insertion), 기존의 원소를 삭제(deletion), 기존의 원소를 다른 것으로 대체(substitution) 예를 들어보자.

ghost > toast

g를 t로 대체한다 (subsitution) thost > toast
h를 o로 대체한다 (subsitution) toost > toast
o를 a로 대체한다 (subsitution) toast = toast!
이런 과정을 거치면, ghost와 toast의 거리는 3이 되는 것이다.

이제 느낌을 보면 알겠지만, 두 단어의 거리는 둘 중에 가장 긴 단어의 거리가 최대다. (zzz > effoooooooooooort를 비교한다고 생각해보자)

그렇기 때문에, 두단어의 유사도는

return (longerLength - getDistance(longer, shorter)) / (double) longerLength;

이렇게 나올 것이다.

그렇다면 이것을 알고리즘으로 구현하기 위해선 어떻게 해야할까?

이것을 알고리즘으로 구성하기 위한 단계를 다시 한번 생각해보자.

임의로 이렇게 한다고 치자.

두 단어 = s1, s2

길이 = s1.length, s2.length

두 단어 중에 0인게 있다면, 당연한 말이겠지만, 다른 단어의 길이를 리턴한다.
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