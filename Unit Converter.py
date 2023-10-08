# Project Name: Unit Converter
# Creator: Jay Chen
# Create Date: 2017/8/18

import customtkinter


def converter():
    try:
        val = int(input_value_button.get())
        from_unit = from_listbox.get()
        to_unit = to_listbox.get()

        conversion = {
            ("Miles", 'Kilometers'): 1.60934,
            ("Kilometers", "Miles"): 0.621371,
            ('Pounds', 'Kilograms'): 0.453592,
            ('Kilograms', 'Pounds'): 2.20462,
            ('Inches', 'Centimeters'): 2.54,
            ('Centimeters', 'Inches'): 0.393701
        }


        result = val * conversion[(from_unit,to_unit)]
        output.configure(text=f"{result} {to_unit}", text_color="white")
    except:
        output.configure(text="Please Enter a Number!", text_color="red")

# 設定系統相關參數
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# APP 整體框架
app = customtkinter.CTk()
app.title("Unit Converter")
app.geometry("720x480")

# 輸入數字
input_value_label = customtkinter.CTkLabel(app, text="Value:")
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
                                         values=["Miles", "Kilometers",'Pounds','Kilograms','Inches','Centimeters'],
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
                       values=["Miles", "Kilometers",'Pounds','Kilograms','Inches','Centimeters'])

to_listbox.grid(row=2, column=1,
                padx=20, pady=10,
                sticky='ew')

# Convert(Button)
convert = customtkinter.CTkButton(app, text='Convert', command=converter)
convert.grid(row=3, column=1,
             padx=20, pady=10,
             sticky='ew')
# Output
output = customtkinter.CTkLabel(app, text='')
output.grid(row=4, column=1,
            padx=20, pady=10,
            sticky='ew')


app.mainloop()

