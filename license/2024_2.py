def fnCalculation(x, y):               # 문자열 x에서 부분 문자열 y의 등장 횟수를 계산
    result = 0                         # 결과 카운트 초기화
    for i in range(len(x)):            # 문자열 x의 모든 인덱스를 순회
        temp = x[i:i+len(y)]           # x의 현재 위치부터 y의 길이만큼 슬라이스
        if temp == y:                  # 슬라이스가 y와 일치하면
            result += 1                # 카운트 증가
    return result                      # 총 횟수 반환

a = "abdcabcabca"                      # 전체 문자열
p1 = "ab"                              # 찾을 첫 번째 패턴
p2 = "ca"                              # 찾을 두 번째 패턴

out = f"ab{fnCalculation(a, p1)}ca{fnCalculation(a, p2)}" # f-string으로 포맷팅
print(out)                             # 결과 출력