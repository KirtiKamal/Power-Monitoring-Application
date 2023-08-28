# Power Monitoring Application For Internship Greenie Web

import psutil
import time

app = input("Enter application name: ")

# Get initial power usage 
power = psutil.cpu_percent(interval=1, percpu=True)
print(f"Initial power usage: {power}%")

# Start measuring time
start = time.time()

# Loop will run until the application is closed     
while True:
    for proc in psutil.process_iter():
        if proc.name() == app:
            # Get power usage for this app only
            power = proc.cpu_percent(interval=1)

    # Print power usage every second     
    print(f"{app} power usage: {power}%") 

    time.sleep(1)

# Calculate total time and power consumed    
end = time.time()     
total_time = end - start
total_power = sum(power)

print(f"Total time: {total_time} seconds")     
print(f"Total power consumed: {total_power}%")