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

chieu_dai = input_positive_float("Nhap chieu dai (cm): ")
chieu_rong = input_positive_float("Nhap chieu rong (cm): ")

dien_tich = chieu_dai * chieu_rong
chu_vi = 2 * (chieu_dai + chieu_rong)

print(f"Dien tich = {dien_tich} cm^2")
print(f"Chu vi    = {chu_vi} cm")

