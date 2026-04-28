TestList = [1, 2, 3, 4, 5]                             # 초기 리스트
TestList = list(map(lambda num: num + 100, TestList))  # 각 요소에 100 더하기

print(TestList)                                        # 변환된 리스트 출력