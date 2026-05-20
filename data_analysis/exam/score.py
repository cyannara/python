import pandas as pd

data_score = { '과목': ['수학', '영어', '국어'], '점수': [90, 85, 95], '학급': ['A', 'B', 'A'] }
df = pd.DataFrame(data_score)

# 점수열만 출력
#print(df['점수'])

# 과목과 학급열 모두 출력
#print(df[['과목','학급']])

# 'A'학급의 성적
print(df.loc[2]['점수'])

print(df[df['과목'] == '영어']['점수'])