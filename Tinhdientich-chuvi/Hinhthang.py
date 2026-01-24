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

# Dien tich: S = (day_lon + day_be) * cao / 2
day_be = input_positive_float("Nhap do dai day be (cm): ")
day_lon = input_positive_float("Nhap do dai day lon (cm): ")
cao = input_positive_float("Nhap chieu cao (cm): ")

dien_tich = (day_be + day_lon) * cao / 2
print(f"Dien tich hinh thang = {dien_tich} cm^2")

# Chu vi: P = day_be + day_lon + canh_ben_1 + canh_ben_2
canh_ben_1 = input_positive_float("Nhap do dai canh ben 1 (cm): ")
canh_ben_2 = input_positive_float("Nhap do dai canh ben 2 (cm): ")

chu_vi = day_be + day_lon + canh_ben_1 + canh_ben_2
print(f"Chu vi hinh thang = {chu_vi} cm")