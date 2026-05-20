countries = {'일본', '중국', '한국'}       # 초기 국가 집합 생성
countries.add('베트남')                   # '베트남' 추가
countries.add('중국')                     # '중국'은 이미 있으므로 추가되지 않음
countries.remove('일본')                  # '일본' 제거
countries.update(['홍콩', '한국', '태국']) # '홍콩', '한국', '태국' 추가 (중복은 무시)
print(countries)                         # 최종 집합 출력

# '중국', '한국', '베트남','홍콩', '태국'