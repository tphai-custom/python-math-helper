#Tinh dien tinh hinh tron
import math
bankinh= float(input("Nhap do dai ban kinh cua hinh tron(cm) "))
number = float(input("Nhap so chu cai lam tron(cm) "))
x = bankinh * bankinh
x = x*math.pi
y = int(number)
print(round(x,y))

#Tinh chu vi hinh tron
import math
bankinh= float(input("Nhap do dai ban kinh cua hinh tron(cm) "))
number = float(input("Nhap so chu cai lam tron(cm) "))
x = bankinh * 2
x = x*math.pi
y = int(number)
print(round(x,y))