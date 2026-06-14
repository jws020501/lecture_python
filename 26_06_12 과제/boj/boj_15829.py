len = int(input()) 
str = input() 
r = 31  
m = 1234567891  
hash = 0 

for i in range(len):
    cur = ord(str[i]) - 96  # 문자를 숫자로 변환
    hash += cur * (r ** i)  # 다항식 해시 계산

print(hash % m)  # 최종 해시 값 출력