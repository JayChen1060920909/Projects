import shutil
import os

screenshot_dir = '/Users/Jay/Desktop/Screenshots'
desktop_dir = '/Users/Jay/Desktop'
months = {'01':'Jan',
          '02':"Feb",
          '03':"Mar",
          "04":"Apr",
          "05":"May",
          "06":"Jun",
          "07":"Jul",
          "08":"Aug",
          "09":"Sep",
          "10":"Oct",
          "11":"Nov",
          "12":"Dec"}

# You can change it if you want
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
    print("Creating ScreenShots folder...")

# Check all files on desktop, if this is a screenshot file, then move it
files_on_desktop = os.listdir(desktop_dir)
for file in files_on_desktop:
    if file.startswith("Screenshot") and file.endswith(".png"):
        file_path = desktop_dir + '/' + file

        # Create a month folder
        file_year = file[11:15]
        file_month = file[16:18]
        extension = '/' + months[file_month] + " " + file_year

        # detect if month folder already exist, if not, then create one
        if not os.path.exists(screenshot_dir + extension):
            os.makedirs(screenshot_dir + extension)
            print(f"Creating folder {screenshot_dir + extension}")

        shutil.move(file_path, screenshot_dir+extension)
        print(f"Moving {file} to \n{screenshot_dir + extension}")