import pandas as pd

# Series : 1차원 데이터 구조
s= pd.Series([10,20,30,40,50])
#print(s)

# 데이터프레임(DataFrame)= 시리즈가 모여서 만들어진 2차원 데이터 구조=엑셀시트
data = {
    '이름': ['철수', '영희', '민수', '지민'],
    '나이': [25, 23, 28, 26],
    '성별': ['남', '여', '남', '여']
}

df = pd.DataFrame(data)
#print(df)

# 열 선택하기
#print(df['이름'])

# 여러 열(리스트 형식)
#print(df[['이름','나이']])

# 행선택
print(df.iloc[0])
print()
print("-" * 20)
print(df.loc[[1,3]])