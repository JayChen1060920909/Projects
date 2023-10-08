# In this project, I'm going to desgin a user infterface for translating difference languages in real time
# Library Used: google trans, textblob

import googletrans
import textblob
import customtkinter
from tkinter import END



# Adding languages
language = googletrans.LANGUAGES
translator = googletrans.Translator()

lang_value = list(language.values())
lang_short = language.keys()

def Translate():
    # Get the language to translate
    to_language = to_language_menu.get()


    # Perform the translation
    from_text = from_language_input_box.get(1.0,END)
    for idx, val in language.items():
        if val == to_language:
            lan_ = idx


    words = translator.translate(from_text, dest=lan_)

    # Show the translation
    to_language_input_box.delete(0.0, END)
    to_language_input_box.insert(0.0,words.text)



# 使用者介面


# 設定系統相關參數
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# APP 整體框架
app = customtkinter.CTk()
app.title("Jay's Translator")
app.geometry("750x500")


# From-language selector
from_language_menu = customtkinter.CTkLabel(master=app,text="Please Enter any language:")
from_language_menu.grid(row=0, column=0,
                  padx=50, pady=20,
                  )

# To-language selector
to_language_menu = customtkinter.CTkOptionMenu(master=app,values=lang_value)
to_language_menu.grid(row=0, column=1,
                  padx=50, pady=20,
                  )

# to-language input box(Inputbox)
to_language_input_box = customtkinter.CTkTextbox(app, width=150, height=150)
to_language_input_box.grid(row=1, column=1,
                             padx=50, pady=20,
                             )

# from-language input box(Inputbox)
from_language_input_box = customtkinter.CTkTextbox(app, width=150, height=150)
from_language_input_box.grid(row=1, columns=1,
                           padx=50, pady=20,
                           )

# translate button
translate_button = customtkinter.CTkButton(app, text='Translate',command=Translate)
translate_button.grid(row=2, column=0,
                      padx=(180,0), pady=20, sticky='w',columnspan=3)




app.mainloop()

