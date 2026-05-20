a = "REMEMBER NOVEMBER"        # 문자열 a 선언
b = a[:3] + a[12:15]           # b는 a에서 부분 문자열 추출 후 합치기
c = "R AND %s" % "STR"         # 문자열 포맷팅: %s 자리에 "STR" 삽입

print(b + c)                   # b와 c를 이어붙여 출력