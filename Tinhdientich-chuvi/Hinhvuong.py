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

canh = input_positive_float("Nhap chieu dai canh (cm): ")

dien_tich = canh * canh
chu_vi = 4 * canh

print(f"Dien tich = {dien_tich} cm^2")
print(f"Chu vi    = {chu_vi} cm")
