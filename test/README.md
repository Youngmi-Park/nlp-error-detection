### Libiri speech test-clean 12 files
libri speech dataset sentence toy sample 

**원본 Transcript** 대문자로 되어있어 소문자로 바꿈

![image](https://user-images.githubusercontent.com/53163222/122710013-5b179200-d29a-11eb-96d0-2d92ce38fc21.png)


**Deep Speech 결과**

![image](https://user-images.githubusercontent.com/53163222/122710027-623ea000-d29a-11eb-9586-6d7eb7c9fe98.png)


![image](https://user-images.githubusercontent.com/53163222/122710172-b9447500-d29a-11eb-83a0-458f1ea060ba.png)


![image](https://user-images.githubusercontent.com/53163222/122710200-c5c8cd80-d29a-11eb-8203-2f8119be7783.png)


![image](https://user-images.githubusercontent.com/53163222/122710212-d0836280-d29a-11eb-9a51-981c90d6e5af.png)

단어 한개의 오류는 잘 수정하지만 띄어쓰기나 입력 단어개수자체가 다른경우 해결이 어려운 문제가 발생


### Libiri speech test-other 17 files

**원본 Transcript** 대문자로 되어있어 소문자로 바꿈

![image](https://user-images.githubusercontent.com/53163222/122710447-37a11700-d29b-11eb-8358-5781bd095a1a.png)

**Deep Speech 결과**

![image](https://user-images.githubusercontent.com/53163222/122710417-28ba6480-d29b-11eb-9036-a2eabbd8a740.png)

21.06.18

![원래문장_1](https://user-images.githubusercontent.com/53163222/129481967-e4cf2456-414e-4603-93e6-adf56c11d364.png)
![원래문장_2](https://user-images.githubusercontent.com/53163222/129481969-69aa5dd6-fd20-4729-ae93-8585c03d0806.png)
![원래문장_3](https://user-images.githubusercontent.com/53163222/129481971-b1d5dc5d-a141-4188-b68a-6a46c09edaaf.png)
![원래문장_4](https://user-images.githubusercontent.com/53163222/129481974-e4dd5d4b-6a62-4796-8866-9ae45bf56447.png)
![원래문장_5](https://user-images.githubusercontent.com/53163222/129481975-78a314fd-29e2-4a5d-ae43-6f5cff44dff3.png)
![원래문장_6](https://user-images.githubusercontent.com/53163222/129481977-e1e5fcba-9050-46dd-8e7b-4ecbf16d88ec.png)
![원래문장_7](https://user-images.githubusercontent.com/53163222/129481956-1f63e838-2681-4b9b-a670-a9d23e322412.png)
![원래문장_8](https://user-images.githubusercontent.com/53163222/129481959-536fc741-33d7-4ede-8501-814cd4f7ad6e.png)
![원래문장_9](https://user-images.githubusercontent.com/53163222/129481961-cf20bde9-28f8-4075-bbfe-edb6f8262307.png)
![원래문장_10](https://user-images.githubusercontent.com/53163222/129481962-3900fc70-70c5-483d-a41d-12ba898b5bc4.png)
![원래문장_11](https://user-images.githubusercontent.com/53163222/129481963-6f7134cf-d5d4-43e0-bf38-efe4fa6aad5a.png)
![원래문장_12](https://user-images.githubusercontent.com/53163222/129481964-cc6ba1ff-2b5c-4b59-a205-90770dfc881b.png)

### 1. Soundex 검증
#### 1) 구체적인 알고리즘 내용
SOUNDEX는 영어로 문자열을 말할 때 어떻게 들리는지에 따라 영숫자 문자열을 4자의 코드로 변환한다. 
코드의 첫 번째 문자는 character_expression의 첫 번째 문자이며 대문자로 변환된다. 코드의 두 번째부터 네 번째 문자까지의 문자는 식의 문자를 나타내는 숫자다. 문자 A, E, I, O, U, H, W 및 Y는 문자열의 첫 문자가 아닌 경우 무시된다. 4자로 된 코드를 생성하기 위해 필요한 경우 끝에 0이 추가된다.

1: b, f, v, p - 입술(+치아)을 이용한 소리 (m)제외
2: c, g, j, k, q, s, x, z
3: d, t - 언어학적으로 alveolar(치경, 윗앞니 뒤쪽 잇몸) 위치에 있는 소리
4: l - 그냥('L')하나
5: m, n - 비음
6: r -그냥 'r' 하나
 
- 문자 A, E, I, O, U, H, W 및 Y는 무시한다.
- 동일한 Soundex 코드 번호를 가진 문자들은 하나로 정규화 한다.
Pfister 는 P-236으로 코딩된다 (P, F 무시 됨, S는 2, T는 3, R은 6). 
Jackson 은 J-250으로 코딩된다 (J, C는 2, K는 무시, S는 무시, 5는 N, 0은 추가됨).
- 최종적으로 4글자 코드가 되어야 하기에 코드의 길이가 4글자 미만인 경우 0을 채워준다.

##### 단점
영어 이름을 기반으로 작성된 알고리즘이고, 분류 코드도 4글자로 짧은 데다가 자세한 언어적 분석이나 광범위한 데이터를 기반으로 한 알고리즘이 아닌 것 같아 한계가 있는 것으로 보인다.

#### 2) 단어 몇 개를 선정해서 비교
Binary로 치환하는 과정에서 생기는 오류인지, Library 자체의 문제인지 확인

![image](https://user-images.githubusercontent.com/53163222/129482332-7c04b389-a11d-4723-898f-48679e5aaef5.png)
![image](https://user-images.githubusercontent.com/53163222/129482352-70c2e13c-3408-484c-b0ef-ed10c3cd4af8.png)
![image](https://user-images.githubusercontent.com/53163222/129482381-db64d969-9f3a-444d-94b2-7cf4c88e5bd0.png)
![image](https://user-images.githubusercontent.com/53163222/129482389-e0d9a9f6-3bc6-4c3c-a2fb-7ef74f8d0aa6.png)
![image](https://user-images.githubusercontent.com/53163222/129482411-5afddc99-7109-4b05-b46d-9a26abb80122.png)
![image](https://user-images.githubusercontent.com/53163222/129482406-753383d3-52cf-43ee-a9ea-ed9e6d5e9e80.png)


### 2. Merge 가중치 고려한 순위 - score자체는 크게 중요하지 않은 것으로 보임.


+ 참고
Soundex, Metaphone 및 Match Rating Codex와 같은 단어의 소리를 계산하는 여러 가지 방법이 있다.
  
![image](https://user-images.githubusercontent.com/53163222/129482514-a5b40229-62a4-4a8f-bacc-765b7464fe2e.png)

codeList 1과 codeList 2는 서로 다른 두 단어의 음성 코드를 나타낸다. codeList 3은 알고리즘 가중치를 나타내며 0과 1 사이의 값을 포함하며 3의 단일 값의 합계는 1이다.

두 단어 사이의 유사도는 음성 별 계산을 기반으로 하는 10 진수 값입니다. 각 부분합은 codeList1과 codeList2의 특정 음성 표현 사이의 Levenshtein 거리와 특정 음성 알고리즘에 대한 가중치의 곱이다.

예시) NYSIIS 계산

![image](https://user-images.githubusercontent.com/53163222/129482510-e46eae25-78b6-4512-b658-feabcbacdf8a.png)

[여기](https://stackabuse.com/phonetic-similarity-of-words-a-vectorized-approach-in-python)에 설명된 접근 방식은 다양한 음성 유사도를 균형있게 조정하는 솔루션을 찾는데 도움된다. 지금까지 이 결과는 유망하지만 최적이 아닐 수 있다. 가중치 벡터는 각 특정 음성 알고리즘의 영향을 조절하는 데 사용된다. 언어 별 적절한 가중치 분포를 찾으려면 추가 연구가 필요하며, 또한 고려되는 알고리즘 목록을 쉽게 확장할 수 있다.

2020.09.01