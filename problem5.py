choice = input("섭시인가 화씨인가 : ")

def cf(c_temp):
    return 9.0/5.0 * c_temp+32

def fc(f_temp):
    return (f_temp-32.0) * 5.0 / 9.0

if (choice=="c") or (choice=="C"):
    temp = float(input("섭씨 : "))
    print("화씨: ", cf(temp))

if (choice=="F") or (choice=="f"):
    temp = float(input("화씨: "))
    print("섭씨 : ", fc(temp))