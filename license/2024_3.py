def func(lst):                                  # 리스트를 뒤집는 함수
    for i in range(len(lst) // 2):              # 절반만 순회
        lst[i], lst[-i-1] = lst[-i-1], lst[i]   # 앞뒤 요소를 swap

lst = [1, 2, 3, 4, 5, 6]                        # 원본 리스트
func(lst)                                       # 리스트를 뒤집음
print(lst)
print(lst[1::2])
print(sum(lst[::2]) - sum(lst[1::2]))           # 짝수 인덱스 합  - 홀수 인덱스 합