lol = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]   # 2차원 리스트 생성

print(lol[0])                          # 첫 번째 리스트 출력: [1, 2, 3]
print(lol[2][1])                       # 세 번째 리스트의 두 번째 요소 출력: 7

for sub in lol:                        # lol의 각 하위 리스트 순회
    for item in sub:                   # 하위 리스트 내의 각 요소 순회
        print(item, end='')            # 요소 출력, 줄바꿈 없이
    print()                            # 각 하위 리스트마다 줄바꿈