import math

def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Nhap sai. Vui long nhap so (vi du: 2.5).")

def input_int_nonnegative(prompt: str) -> int:
    while True:
        try:
            x = int(input(prompt).strip())
            if x >= 0:
                return x
            print("Vui long nhap so nguyen >= 0.")
        except ValueError:
            print("Nhap sai. Vui long nhap so nguyen.")

a = input_float("Nhap he so a (cho x^2): ")
b = input_float("Nhap he so b (cho x): ")
c = input_float("Nhap he so c (hang so tu do): ")
digits = input_int_nonnegative("Nhap so chu so sau dau phay muon lam tron (vi du 2): ")

# Neu a = 0 thi thanh phuong trinh bac 1: bx + c = 0
eps = 1e-12
if abs(a) < eps:
    if abs(b) < eps:
        if abs(c) < eps:
            print("Phuong trinh vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
    else:
        x = -c / b
        print(f"Phuong trinh bac 1 co nghiem: x = {x:.{digits}f}")
else:
    delta = b * b - 4 * a * c

    if abs(delta) < eps:
        x = -b / (2 * a)
        print(f"Phuong trinh co nghiem kep: x = {x:.{digits}f}")
    elif delta < 0:
        print("Phuong trinh vo nghiem (khong co nghiem thuc).")
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b - sqrt_delta) / (2 * a)
        x2 = (-b + sqrt_delta) / (2 * a)
        print(f"x1 = {x1:.{digits}f}")
        print(f"x2 = {x2:.{digits}f}") 
    