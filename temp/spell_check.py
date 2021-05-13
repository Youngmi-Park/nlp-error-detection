#pip install pyspellchecker
from spellchecker import SpellChecker

spell = SpellChecker()

#문장 공백단위로 자르는 코드 짜기
#bert 사용하는 법 알아보기

# find those words that may be misspelled
misspelled = spell.unknown(['the', 'man', 'worked', 'as', 'a', 'watere'])

miss_word = []
candidate = {}
for  word in misspelled:
    print(word)
    #print(spell.known(word))
    # print(spell.unknown(word))
    miss_word.append(word)
    candidate[word] = list(spell.candidates(word))
    # Get the one `most likely` answer
    print("가장 가능성이 높은 결과:",spell.correction(word)) # 철자가 틀린 단어에 대해 가장 가능성이 높은 결과를 반환

    # Get a list of `likely` options
    print("철자가 단어에 대해 가능한 후보 세트:", spell.candidates(word)) # 철자가 틀린 단어에 대해 가능한 후보 세트를 반환

print(candidate.get('watere')[0])
# known([words]): word frequency list에 있는 단어 반환
#
# unknown([words]): frequency list에 없는 단어 반환
#
# word_probability(word): frequency list의 모든 단어 중 주어진 단어의 빈도