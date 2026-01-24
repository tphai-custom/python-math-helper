def input_positive_float(prompt: str) -> float:
    while True:
        try:
            x = float(input(prompt))
            if x <= 0:
                print("Vui long nhap so > 0.")
                continue
            return x
        except ValueError:
            print("Sai dinh dang. Vui long nhap so (vi du: 12.5).")

# Dien tich: S = day * chieu cao
day = input_positive_float("Nhap canh day cua hinh binh hanh (cm): ")
cao = input_positive_float("Nhap chieu cao tuong ung voi day (cm): ")
dien_tich = day * cao
print(f"Dien tich hinh binh hanh = {dien_tich} cm^2")

# Chu vi: P = 2 * (day + canh ben)
canh_ben = input_positive_float("Nhap do dai canh ben (cm): ")
chu_vi = 2 * (day + canh_ben)
print(f"Chu vi hinh binh hanh = {chu_vi} cm")
