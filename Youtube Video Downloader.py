import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObj = YouTube(ytLink,on_progress_callback=on_progress)
        video = ytObj.streams.get_highest_resolution()

        title.configure(text=ytObj.title, text_color='white')
        finishLabel.configure(text='')

        video.download()
        finishLabel.configure(text='Downloaded!')
    except:
        finishLabel.configure(text="Download Error!",text_color='red')

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    #更新Progress Bar
    pProgressBar.set(float(percentage_of_compeletion) / 100)


# 這裡使用現代化的customtkinter來呈現UI, 主題使用跟系統一樣的
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# APP 整體框架
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# 輸入標籤
title = customtkinter.CTkLabel(app, text="請輸入網址:")
title.pack(padx=10,pady=10)

# 輸入方塊
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# 成功下載標籤畫面
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

# 進度條
pPercentage = customtkinter.CTkLabel(app, text='0%')
pPercentage.pack()

pProgressBar = customtkinter.CTkProgressBar(app, width=400)
pProgressBar.set(0)
pProgressBar.pack(padx=10, pady=10)


# 下載按鈕
download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack(padx=20, pady=10)




# Run App
app.mainloop()