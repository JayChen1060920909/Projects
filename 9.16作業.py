import datetime
import easygui
def day(year,month,day,year2,month2,day2):     
    day = datetime.date(year,month,day)
    other_day = datetime.date(year2,month2,day2)
    easygui.msgbox(day-other_day)
easygui.msgbox(day(int(easygui.integerbox("年:",upperbound=10000,lowerbound=0)),int(easygui.integerbox("月:",upperbound=10000,lowerbound=0)),int(easygui.integerbox("日:",upperbound=10000,lowerbound=0)),int(easygui.integerbox("年:",upperbound=10000,lowerbound=0)),int(easygui.integerbox("月:",upperbound=10000,lowerbound=0)),int(easygui.integerbox("年:",upperbound=10000,lowerbound=0))))

