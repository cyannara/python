
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[2:5])  # Output: ['c', 'd', 'e']  
print(letters[-1])   # Output: 'g'
print(letters[1:7:2] )


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

#2를 출력
#print( x[1][1] )

#전체출력
for i in  x:
  for a in i:
    print(a,end=",")
  print()