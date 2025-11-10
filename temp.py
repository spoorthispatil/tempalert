import sys
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    temp = float(sys.argv[1])
    print("User provided temperature:")
else:
    script_name = sys.argv[0]
    temp = 30.0  # default temperature
    print("No input given - using default temperature:")
if temp < 20:
    status = "Cold"
elif 20 <= temp <= 35:
    status = "Normal"
else:
    status = "Hot"
print("Script Name:", script_name)
print("Temperature:", temp)
print("Weather Condition:", status)
