a = 100                     # 초기값 설정
result = 0                  # 결과 변수 초기화

for i in range(1, 3):       # i = 1부터 2까지 반복 (range는 끝 제외)
    result = a >> i         # a를 i만큼 오른쪽으로 비트 시프트
    result = result + 1     # 시프트 결과에 1 더하기

print(result)               # 마지막 반복의 결과 출력