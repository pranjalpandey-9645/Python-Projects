import datetime
import os
import platform

def get_boot_time():
    if platform.system() == "Windows":
        output = os.popen('systeminfo | find "System Boot Time"').read()
        if "System Boot Time" in output:
            boot_time_str = output.strip().split("System Boot Time:")[1].strip()
            boot_time = datetime.datetime.strptime(boot_time_str, '%d-%m-%Y, %H:%M:%S')

            return boot_time
        else:
            return None
    else:
        print("This script is only for Windows.")
        return None

def main():
    boot_time = get_boot_time()
    if boot_time:
        now = datetime.datetime.now()
        uptime = now - boot_time

        days, seconds = uptime.days, uptime.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        print(f"🕒 System Last Booted: {boot_time.strftime('%d %B %Y, %I:%M:%S %p')}")
        print(f"⏱️ Uptime: {days} days, {hours} hours, {minutes} minutes")

        if days >= 1:
            print(f"✅ You haven't shut down your PC for {days}+ days.")
        else:
            print("✅ Your PC was cleanly shut down within the last 24 hours.")
    else:
        print("⚠️ Couldn't find boot time. Try running this script with admin privileges.")

if __name__ == "__main__":
    main()
