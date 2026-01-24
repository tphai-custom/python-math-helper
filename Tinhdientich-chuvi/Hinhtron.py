import math

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

def input_nonnegative_int(prompt: str) -> int:
    while True:
        try:
            x = int(input(prompt))
            if x < 0:
                print("Vui long nhap so nguyen >= 0.")
                continue
            return x
        except ValueError:
            print("Sai dinh dang. Vui long nhap so nguyen.")

ban_kinh = input_positive_float("Nhap do dai ban kinh (cm): ")
so_chu_so = input_nonnegative_int("Nhap so chu so sau dau phay muon lam tron (vi du 2): ")

dien_tich = math.pi * ban_kinh * ban_kinh
chu_vi = 2 * math.pi * ban_kinh

print(f"Dien tich hinh tron = {dien_tich:.{so_chu_so}f} cm^2")
print(f"Chu vi hinh tron    = {chu_vi:.{so_chu_so}f} cm")