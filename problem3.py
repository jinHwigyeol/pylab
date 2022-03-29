a = int(input("팩토리얼을 구할 숫자를 입력하세요 : "))
result = 1
for item in range(1, a+1, 1):
    result *= item
print(result)