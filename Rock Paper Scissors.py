# Project Name: Rock Paper Scissors game
# Creator: Jay Chen
# Create Date: 2017/6/3
import random

options = ['rock','paper','scissors']

user_wins = 0
computer_wins = 0


while True:
    user_choice = input("打rock/paper/scissors 或選擇q來退出遊戲:")

    if user_choice == 'q':
        print("遊戲退出！")
        break

    if user_choice not in options:
        print("請在確認一次有沒有打錯！ 然後再輸入一次！")
        continue

    random_number = random.randint(0,2)
    computer_choice = options[random_number]

    print("你的選擇:{} 敵方的選擇:{}".format(user_choice, computer_choice))

    if user_choice == "rock" and computer_choice == "scissors":
        print("你贏了！")
        user_wins += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("你贏了！")
        user_wins += 1
    elif user_choice == 'paper' and computer_choice == "rock":
        print("你贏了！")
        user_wins += 1
    else:
        print('你輸了!')
        computer_wins += 1


print("你總共玩了{}局, 贏了{}次, 輸了{}次".format(user_wins + computer_wins, user_wins, computer_wins))
