import easygui

def price(km):
    if(km <= 20):
        return easygui.msgbox("0元")
    elif(km <= 200):
        return easygui.msgbox(str((km-20)*1.2) + "元")
    else:
        return easygui.msgbox(str((km-40)*1.2 + (km-200)*0.8) + "元")
# 將使用者輸入的公里數做計算
easygui.msgbox(price(easygui.integerbox("請輸入公里數:",upperbound=1000,lowerbound=0)))
    
