# Project Name: 匯率轉換GUI
# Creator: Jay Chen
# Create Date: 2017/8/9

import pandas as pd
import requests
import customtkinter

# Get the data from the website

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW").text
df = pd.read_html(html)

currency = df[0]

currency = currency.iloc[:, 0:3]

currency.columns = [u'國家',
                    u'現金匯率-本行買入',u'現金匯率-本行賣出']
currency[u'國家'] = currency[u'國家'].str.extract('\((\w+)\)')

countries_list = currency['國家'].tolist()



def converter():
    try:
        value = int(input_value_button.get())
        from_country = from_listbox.get()
        to_country = to_listbox.get()

        from_currency = float(currency[currency['國家'] == from_country]['現金匯率-本行賣出'].values[0])
        to_currency = float(currency[currency['國家'] == to_country]['現金匯率-本行賣出'].values[0])

        converted = round((value * from_currency) / to_currency, 3)

        output.configure(text=f"{converted} {to_country} dollars", text_color="white")
    except:
        output.configure(text="Please Enter a Number!", text_color="red")



# 使用者介面


# 設定系統相關參數
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# APP 整體框架
app = customtkinter.CTk()
app.title("各國幣別即時匯率轉換")
app.geometry("720x480")
# app.grid_columnconfigure((1,1),weight=1)

# 輸入數字
input_value_label = customtkinter.CTkLabel(app, text="請輸入金額:")
input_value_label.grid(row=0, column=0,
                  padx=20, pady=20,
                  sticky="ew")

input_value_button = customtkinter.CTkEntry(app,
                              placeholder_text="")
input_value_button.grid(row=0, column=1,
                    columnspan=3, padx=20,
                    pady=20, sticky="ew")
# From(Button)
from_label = customtkinter.CTkLabel(app, text="From:")
from_label.grid(row=1, column=0,
                padx=20, pady=20,
                sticky='ew')

from_listbox = customtkinter.CTkComboBox(master=app,
                                         values=countries_list,
                                         )

from_listbox.grid(row=1, column=1,
                  padx=20, pady=10,
                  sticky='ew')

# To(Button)
to_label = customtkinter.CTkLabel(app, text="To:")
to_label.grid(row=2, column=0,
                padx=20, pady=20,
                sticky='ew')

to_listbox = customtkinter.CTkComboBox(master=app,
                       values=countries_list)

to_listbox.grid(row=2, column=1,
                padx=20, pady=10,
                sticky='ew')

# Convert(Button)
convert = customtkinter.CTkButton(app, text='轉換', command=converter)
convert.grid(row=3, column=1,
             padx=20, pady=10,
             sticky='ew')
# Output
output = customtkinter.CTkLabel(app, text='')
output.grid(row=4, column=1,
            padx=20, pady=10,
            sticky='ew')

app.mainloop()