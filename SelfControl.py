# Understand how python and website interactive together,
# Understand how to do more complicated jobs with the control of python
from datetime import datetime


# limit_time = input("請問要封鎖到什麼時候?:").split()
end_time = datetime(2023,10,5,22)

sites_to_block = ['instagram.com','https://www.youtube.com/']

# host_path = "/etc/hosts"
host_path_for_windows = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1" # The website to redirect to after blocking action

def block_sites():
    if datetime.now() < end_time:
        print("block sites")
        with open(host_path_for_windows, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n") # 寫進去代表說就是你已經不能在存取這個網站了

    else:
        print("unblock sites")
        with open(host_path_for_windows, 'r+') as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)
            hostsfile.truncate()

if __name__ == '__main__':
    # 1. run manually
    # 2. cron job
    # 3. while True
    block_sites()