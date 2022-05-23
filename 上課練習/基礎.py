def calculate():
    a, b = 5, 3
    n1 = a+b
    n2 = a-b
    n3 = a*b
    n4 = a/b
    n5 = a//b
    n6 = a % b
    n7 = a**b
    print(
        f"a+b={n1}, a-b={n2}, a*b={n3}, a/b={n4}, a//b={n5}, a%b={n6}, a**b={n7}")


def ab():
    a, b = 5, 3
    print(a > b, a < b, a >= b, a <= b, a == b, a != b)


def season():
    season = int(input("輸入月份: "))
    if season in (2, 3, 4):
        print("春天")
    elif season in (5, 6, 7):
        print("夏天")
    elif season in (8, 9, 10):
        print("秋天")
    elif season in (11, 12, 1):
        print("冬天")
    else:
        print("輸入錯誤")


def count():
    num = int(input("輸入1~10的數字: "))
    if num >= 0 and num < 11:
        sum = 0
        for i in range(1, num+1):
            sum += i
            print(i, "+", end=" ")
        print(f"= {sum}")
    else:
        print("超出範圍內")


def conti():
    print("請輸入成績，若要結束請輸入-1")
    sum = 0
    while(True):
        note = int(input("加總-> "))
        if note == -1:
            break
        else:
            sum += note
    print("總分為:", sum)


if __name__ == "__main__":
    count()
