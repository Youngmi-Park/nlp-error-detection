# 두 문자열 길이비교
global M
def compareLength(s1, s2):
    if len(s1) >= len(s2):
        longstr, shortstr = s1, s2
    else:
        longstr, shortstr = s2, s1
    return longstr, shortstr

def getDistance(s1, s2):
    long = len(s1)
    short = len(s2)
    for i in range(long):
        M[i][0] = i
    for j in range(short):
        M[0][j] = j
    for i in range(1, long):
        for j in range(1, short):
            if s1[i-1] == s2[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j], M[i-1][j-1], M[i][j-1]) + 1
    print(s2, "와(과)", s1, "의 최소 편집 거리는", M[long- 1][short - 1] , "입니다.")
 
def getTrace(m, s1, s2):
    print("[", s2, "을(를)", s1, "로 바꾸는 과정 ]")
    i = len(s1) - 1
    j = len(s2) - 1
    while not(i < 0 and j < 0):
        s = min(m[i-1][j], m[i-1][j-1], m[i][j-1])
        if s == m[i][j]:
            i -= 1
            j -= 1
        elif s == m[i][j-1]:
            print(s1[i] + "을(를) 삭제")
            j -= 1
        elif s == m[i-1][j-1]:
            print(s2[j-1] + "을(를) " +s1[i-1]  + "(으)로 변경")
            i -= 1
            j -= 1
        else:
            print(s1[i-1] + "을(를) 추가")
            i -= 1

# 비교할 문자열 s1, s2
s1="caert"
s2="dadrt"
#문자열의 길이를 비교해서 s1에 긴문자열, s2에 짧은 문자열을 넣는다.
s1, s2 = compareLength(s1, s2)
# 길이가 긴 문자열을 기준으로 2차원 리스트 초기화
M = [[0] * (len(s1)+1) for _ in range(len(s1)+1)]
getDistance(s1, s2)
getTrace(M, s1, s2)
