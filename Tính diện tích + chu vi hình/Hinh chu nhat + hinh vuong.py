# Tinh dien tich hinh chu nhat + hinh vuong
import math
import time
def calculate_area(length, width):
    area = float(length * width )
    return area

length = float(input("Nhap chieu dai cua hinh chu nhat/ hinh vuong: "))
width = float(input("Nhap chieu dai cua hinh chu nhat/ hinh vuong: "))
calculate_area(length, width)
dthcn = calculate_area(length, width)
print(dthcn)


time.sleep(2)