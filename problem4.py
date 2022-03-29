x=int(input("줄 수를 입력하시오 : "))
for i in range(1,x+1):
    print("*"*i)

for i in range(x):
    print("*"*(x-i-1))