def input_positive_float(prompt: str) -> float:
    while True:
        try:
            x = float(input(prompt))
            if x <= 0:
                print("Vui long nhap so > 0.")
                continue
            return x
        except ValueError:
            print("Sai dinh dang. Vui long nhap so.")

# Dien tich: S = (d1 * d2) / 2
d1 = input_positive_float("Nhap do dai duong cheo 1 (cm): ")
d2 = input_positive_float("Nhap do dai duong cheo 2 (cm): ")
dien_tich = (d1 * d2) / 2
print(f"Dien tich hinh thoi = {dien_tich} cm^2")

# Chu vi: P = 4 * a
a = input_positive_float("Nhap do dai canh hinh thoi (cm): ")
chu_vi = 4 * a
print(f"Chu vi hinh thoi = {chu_vi} cm")