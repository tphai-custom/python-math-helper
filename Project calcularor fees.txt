import math
start_hour = int(input("Starting hour: "))
start_minute = int(input("Starting minute: "))
stop_hour = int(input("Stopping hour: "))
stop_minute = int(input("Stopping minute: "))
hourly_rate = float(input("Hourly rate: "))
start_total_minutes = start_hour * 60 + start_minute
stop_total_minutes = stop_hour * 60 + stop_minute
worked_minutes = stop_total_minutes - start_total_minutes
worked_hours = worked_minutes / 60  
payment = worked_hours * hourly_rate

print(f"Worked {start_hour}:{start_minute:02d} to {stop_hour}:{stop_minute:02d}")
print(f"Total hours: {worked_hours:.1f}")
print(f"Payment: ${payment:.2f}")