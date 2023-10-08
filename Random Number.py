### Project Name: Guess Number Game
### Creator: Jay Chen
### Create date: 2017/6/3

import random

guess_number = random.randint(1,20)

times = 0

while times < 5:
    num = int(input("請輸入你猜的數字(範圍是1~20):"))
    tmp = num

    if num < guess_number:
        print("太小了！ 你還只剩{}次機會".format(5-times))
    elif num > guess_number:
        print("太大了！ 你還只剩{}次機會".format(5-times))
    else:
        print("正確答案！")
    times += 1

if times == 5:
    print("遊戲結束！, 答案是{}".format(guess_number))


