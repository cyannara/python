# for i in range(5) :   # [0,1,2,3,4]
#   print(i)

# for i in [1,3,5,7,9] :  # js의 for of와 같음
#   print(i)

# for i in ["hello", "hi", "bye"] :
#   print(i)  

def print_list(arr) :
  for i in arr :
    print(i)

def sum(a,b) :    
  return a+b

print(sum(3,5)) 

print_list([1,3,5,7,9])
print_list(range(5))
