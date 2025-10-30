'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import psutil
import time

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

    if cpu > CPU_THRESHOLD:
        print("⚠️ ALERT: High CPU usage!")
    if memory > MEM_THRESHOLD:
        print("⚠️ ALERT: High Memory usage!")
    if disk > DISK_THRESHOLD:
        print("⚠️ ALERT: Low Disk Space!")

while True:
    check_system_health()
    time.sleep(10)
