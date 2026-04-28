a = ["Seoul", "Kyeonggi", "Incheon", "Daejun", "Daegu", "Pusan"]  # 지역 이름 리스트
str = "S"                                                        # 초기 문자열

for i in a:                  # 리스트 a를 순회
    str = str + i[1]         # 각 단어의 두 번째 글자를 str에 추가 (i[1])

print(str)                   # 결과 출력