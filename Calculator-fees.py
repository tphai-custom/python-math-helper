def input_int_in_range(prompt: str, lo: int, hi: int) -> int:
    while True:
        try:
            x = int(input(prompt))
            if lo <= x <= hi:
                return x
            print(f"Vui long nhap so trong [{lo}..{hi}].")
        except ValueError:
            print("Sai dinh dang. Vui long nhap so nguyen.")

def input_nonnegative_float(prompt: str) -> float:
    while True:
        try:
            x = float(input(prompt))
            if x < 0:
                print("Vui long nhap so >= 0.")
                continue
            return x
        except ValueError:
            print("Sai dinh dang. Vui long nhap so.")

start_hour = input_int_in_range("Nhap gio bat dau (0-23): ", 0, 23)
start_minute = input_int_in_range("Nhap phut bat dau (0-59): ", 0, 59)

stop_hour = input_int_in_range("Nhap gio ket thuc (0-23): ", 0, 23)
stop_minute = input_int_in_range("Nhap phut ket thuc (0-59): ", 0, 59)

hourly_rate = input_nonnegative_float("Nhap luong theo gio: ")

start_total = start_hour * 60 + start_minute
stop_total = stop_hour * 60 + stop_minute

# Neu lam qua dem: cong them 24h
if stop_total < start_total:
    stop_total += 24 * 60

worked_minutes = stop_total - start_total
worked_hours = worked_minutes / 60
payment = worked_hours * hourly_rate

# Hien thi
print(f"Worked {start_hour}:{start_minute:02d} to {stop_hour}:{stop_minute:02d}")
print(f"Total hours: {worked_hours:.2f}")
print(f"Payment: {payment:.2f}")