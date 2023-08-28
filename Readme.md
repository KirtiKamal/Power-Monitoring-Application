
# Power Monitoring Application Documentation

## Overview
This Python application monitors the power consumption of a specified process on a computer. It calculates power usage based on CPU and memory utilization.

## Code Explanation

### Imports
```python
import psutil
import time
```

The `psutil` library is used to get system utilization metrics. `time` is used for delaying between readings.

### Configuration
```python 
process_name = "chrome"
```

The `process_name` variable specifies the process to monitor. This can be changed to any running process. 

### Power Calculation Function
```python
def get_process_power(process_name):

  process = psutil.Process(process_name)

  cpu_percent = process.cpu_percent()
  mem_percent = process.memory_percent()  

  power = (cpu_percent + mem_percent) / 200    

  return power
```

This function calculates power usage for a given process:

- Get CPU and memory percentage using `psutil.Process()`
- Add CPU and memory percentages 
- Divide by 200 to convert to Watts (configurable constant)
- Return estimated power

### Main Loop
```python
while True:

  power = get_process_power(process_name)
  
  print(f"Power consumption of {process_name}: {power} W")
  
  time.sleep(1)
```

In a loop, get power usage and print it every second.

## Usage

To use this app:

1. Install dependencies: `pip install psutil`
2. Update `process_name` 
3. Run: `python app.py`

Power usage will be printed to the console.
