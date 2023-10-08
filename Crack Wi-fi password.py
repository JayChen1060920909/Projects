import subprocess

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.check_output(['netsh','wlan','show','profile','key=clear',f'name="{i}"']).decode('utf-8').split("\n")
    try:
        print("{:<30} | {:<}".format(i, results[0]))
    except:
        print("{:<30} | {:<}".format(i, ""))