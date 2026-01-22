# Tinh dien tich hinh chu nhat + hinh vuong
import math
def calculate_area(length, width):
    area = float(length * width )
    return area

length = float(input())
width = float(input())
calculate_area(length, width)
a = calculate_area(length, width)
print(a)

# Tinh chu vi hinh chu nhat + hinh vuong
import math
a = float(input("Nhap do dai chieu dai cua hinh chu nhat(cm) "))
b = float(input("Nhap do dai chieu rong cua hinh chu nhat(cm) "))
calculate_perimeter = (a+b)*2
print(calculate_perimeter)

