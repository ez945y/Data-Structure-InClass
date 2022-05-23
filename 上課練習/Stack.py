class stack():
    def __init__(self, max=10):
        self.max = max
        self.array = [''] * self.max
        self.size = -1

    def push(self, x):
        if self.isEmpty():
            self.size += 1
            self.array[self.size] = x
        else:
            print("it's full")

    def pop(self):
        if self.size >= 0:
            self.size -= 1
            return self.array[self.size+1]
        else:
            print("我沒了")

    def top(self):
        return self.array[self.size]

    def isEmpty(self):
        return self.size < self.max


"""
lis = ["red", "orange", "yellow", "green", "blue",
       "purple", "black",  "陳一中", "資財二乙", "109AB0716"]
sk = stack()

for i in range(10):
    sk.push(lis[i])
for _ in range(10):
    print(sk.pop())"""


def hanoi(n, a, b, c):
    if n == 1:
        print(a+"->"+c)
    else:
        hanoi(n-1)


def hanoi(n, pile_a, pile_b, pile_c):
    if n == 1:
        print(pile_a, '-->', pile_c)  # 如果到最後一層，便印出相對應的句子
    else:
        hanoi(n - 1, pile_a, pile_c, pile_b)  # 將前一層的A移動到B
        hanoi(1, pile_a, pile_b, pile_c)  # 將這一層的A移動到C
        hanoi(n - 1, pile_b, pile_a, pile_c)  # 將前一層的B移動到C
    number = int(input('Number of plates：'))  # 印出盤子數量
    hanoi(number, 'A', 'B', 'C')  # 開始進行遞歸
    print('The action needs to be executed %d times!' %
          (2**number-1))  # 共要2的n-2次方次
