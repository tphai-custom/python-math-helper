import math
def nhap_cau_khong_trung(da_chon):
    while True:
        try:
            x = int(input("Nhap so cau ban chon de tra loi(1 - 20) "))
            if not (1 <= x <= 20):
                print("Nhap sai! Chi duoc 1 toi 20.")
            elif x in da_chon:
                print("Ban da chon cau nay roi, hay chon cau khac.")
            else:
                da_chon.add(x)
                return x
        except:
            print("Nhap sai! Hay nhap so.")


def print_intro():
    print("MATH HELPER - QUIZ + SCOREBOARD")
    print("Muc tieu: Luyen Toan bang quiz, cham diem, va luu diem vao score.txt")
    print("Huong dan:")
    print("- Chon chu de")
    print("- Tra loi cau hoi.")
    print("- Nhan diem + xem ket qua")
    print("- Diem se duoc luu tu dong\n")


def print_topic_menu():
    print("CHON CHU DE QUIZ")
    print("1) Phuong trinh bac 2 (ax^2 + bx + c = 0)")
    print("2) UCLN / BCNN")
    print("3) So nguyen to (prime)")
    print("0) Thoat")


def pt2(n):
    # Cau 1
    if (n == 1):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 - (m + 1)x + (m - 2) = 0 co nghiem x = 2")
        print()
        print("A. -2")
        print("B. 0")
        print("C. 2")
        print("D. 4")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    # Cau 2
    if (n == 2):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: 2x^2 - (m + 4)x + 2m = 0 co nghiem kep")
        print()
        print("A. 0")
        print("B. 2")
        print("C. 4")
        print("D. 8")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    # Cau 3
    if (n == 3):
        print("Chon A, B, C ,D")
        print("Tim k de phuong trinh: x^2 - 6x + k = 0 co x1^2 + x2^2 = 20")
        print()
        print("A. 5")
        print("B. 8")
        print("C. 10")
        print("D. 16")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    # Cau 4
    if (n == 4):
        print("Chon A, B, C ,D")
        print("Tim c de phuong trinh: x^2 + 4x + c = 0 co nghiem kep")
        print()
        print("A. 0")
        print("B. 2")
        print("C. 4")
        print("D. 8")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    # Cau 5
    if (n == 5):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 - 5x + m = 0 thoa 1/x1 + 1/x2 = 5/6")
        print()
        print("A. 5")
        print("B. 6")
        print("C. 10")
        print("D. 12")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    # Cau 6
    if (n == 6):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 + (m - 3)x + 2 = 0 co tong hai nghiem bang 1")
        print()
        print("A. 0")
        print("B. 1")
        print("C. 2")
        print("D. 3")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    # Cau 7
    if (n == 7):
        print("Chon A, B, C ,D")
        print("(m > 0) Tim m de phuong trinh: 3x^2 + mx + 3 = 0 co nghiem kep")
        print()
        print("A. 3")
        print("B. 6")
        print("C. 9")
        print("D. 12")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    # Cau 8
    if (n == 8):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 - (2m + 1)x + m(m + 1) = 0 co hai nghiem la 3 va 4")
        print()
        print("A. 2")
        print("B. 3")
        print("C. 4")
        print("D. 5")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    # Cau 9
    if (n == 9):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 - 8x + m = 0 co nghiem nho la 2")
        print()
        print("A. 8")
        print("B. 10")
        print("C. 12")
        print("D. 16")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    # Cau 10
    if (n == 10):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 + 2x + m = 0 thoa x1x2 = x1 + x2")
        print()
        print("A. -2")
        print("B. -1")
        print("C. 0")
        print("D. 2")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'A')

    # Cau 11
    if (n == 11):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 - 2x + m = 0 co x1^2 + x2^2 = 2")
        print()
        print("A. 0")
        print("B. 1")
        print("C. 2")
        print("D. 3")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    # Cau 12
    if (n == 12):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: 2x^2 + 5x + m = 0 co mot nghiem x = -2")
        print()
        print("A. -2")
        print("B. 0")
        print("C. 1")
        print("D. 2")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'D')

    # Cau 13
    if (n == 13):
        print("Chon A, B, C ,D")
        print("(m > 0) Tim m de phuong trinh: x^2 + (m + 2)x + 4 = 0 co nghiem kep")
        print()
        print("A. 2")
        print("B. 4")
        print("C. 6")
        print("D. 8")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'A')

    # Cau 14
    if (n == 14):
        print("Chon A, B, C ,D")
        print("(m > 0) Tim m de phuong trinh: x^2 + mx + 9 = 0 co tong hai nghiem bang -8")
        print()
        print("A. 6")
        print("B. 7")
        print("C. 8")
        print("D. 9")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    # Cau 15
    if (n == 15):
        print("Chon A, B, C ,D")
        print("(m > 0) Tim m de phuong trinh: x^2 - mx + 16 = 0 co nghiem kep")
        print()
        print("A. 4")
        print("B. 6")
        print("C. 8")
        print("D. 10")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    # Cau 16
    if (n == 16):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 - (m + 4)x + m = 0 co nghiem x = 4")
        print()
        print("A. -4")
        print("B. -2")
        print("C. 0")
        print("D. 2")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    # Cau 17
    if (n == 17):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 - 3x + m = 0 co hai nghiem x1, x2 va x1 = 2x2")
        print()
        print("A. 1")
        print("B. 2")
        print("C. 3")
        print("D. 4")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    # Cau 18
    if (n == 18):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 - (m + 2)x + (2m - 3) = 0 co nghiem x = 3")
        print()
        print("A. -1")
        print("B. 0")
        print("C. 1")
        print("D. 3")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    # Cau 19
    if (n == 19):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 - 7x + m = 0 co hai nghiem nguyen va hieu hai nghiem bang 1")
        print()
        print("A. 10")
        print("B. 11")
        print("C. 12")
        print("D. 13")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    # Cau 20
    if (n == 20):
        print("Chon A, B, C ,D")
        print("Tim m de phuong trinh: x^2 + (m - 1)x + (m - 2) = 0 co nghiem x = 1")
        print()
        print("A. -1")
        print("B. 0")
        print("C. 1")
        print("D. 2")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

def ucbc(q):
    if (q == 1):
        print("Chon A, B, C ,D")
        print("Tim UCLN(84, 126)")
        print()
        print("A. 14")
        print("B. 21")
        print("C. 42")
        print("D. 63")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 2):
        print("Chon A, B, C ,D")
        print("Tim BCNN(18, 24)")
        print()
        print("A. 36")
        print("B. 48")
        print("C. 72")
        print("D. 96")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 3):
        print("Chon A, B, C ,D")
        print("Tim UCLN(210, 330)")
        print()
        print("A. 10")
        print("B. 15")
        print("C. 30")
        print("D. 60")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 4):
        print("Chon A, B, C ,D")
        print("Tim BCNN(36, 90)")
        print()
        print("A. 120")
        print("B. 180")
        print("C. 240")
        print("D. 360")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 5):
        print("Chon A, B, C ,D")
        print("Tim UCLN(48, 180)")
        print()
        print("A. 6")
        print("B. 12")
        print("C. 18")
        print("D. 24")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 6):
        print("Chon A, B, C ,D")
        print("Tim BCNN(45, 60)")
        print()
        print("A. 90")
        print("B. 120")
        print("C. 150")
        print("D. 180")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'D')

    if (q == 7):
        print("Chon A, B, C ,D")
        print("Tim UCLN(96, 144)")
        print()
        print("A. 24")
        print("B. 36")
        print("C. 48")
        print("D. 72")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 8):
        print("Chon A, B, C ,D")
        print("Tim BCNN(14, 35)")
        print()
        print("A. 49")
        print("B. 70")
        print("C. 105")
        print("D. 140")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 9):
        print("Chon A, B, C ,D")
        print("Neu UCLN(a, b) = 6 va BCNN(a, b) = 180 thi a*b bang bao nhieu?")
        print()
        print("A. 540")
        print("B. 720")
        print("C. 1080")
        print("D. 2160")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 10):
        print("Chon A, B, C ,D")
        print("Tim a (<72) biet UCLN(a, 72) = 9 va a la boi cua 27")
        print()
        print("A. 27")
        print("B. 36")
        print("C. 54")
        print("D. 63")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'A')

    if (q == 11):
        print("Chon A, B, C ,D")
        print("Tim x (30 < x < 60) biet UCLN(x, 60) = 15")
        print()
        print("A. 30")
        print("B. 35")
        print("C. 45")
        print("D. 50")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 12):
        print("Chon A, B, C ,D")
        print("Tim x biet BCNN(x, 20) = 60; x la uoc cua 60; x chan va khong chia het cho 5")
        print()
        print("A. 10")
        print("B. 12")
        print("C. 15")
        print("D. 30")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 13):
        print("Chon A, B, C ,D")
        print("Biet UCLN(56, b) = 8 va BCNN(56, b) = 280. Tim b")
        print()
        print("A. 32")
        print("B. 40")
        print("C. 56")
        print("D. 80")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 14):
        print("Chon A, B, C ,D")
        print("Biet UCLN(a, 48) = 16 va BCNN(a, 48) = 240. Tim a")
        print()
        print("A. 64")
        print("B. 72")
        print("C. 80")
        print("D. 96")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 15):
        print("Chon A, B, C ,D")
        print("Tim UCLN(405, 1125)")
        print()
        print("A. 15")
        print("B. 25")
        print("C. 45")
        print("D. 75")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 16):
        print("Chon A, B, C ,D")
        print("Tim BCNN(72, 108)")
        print()
        print("A. 144")
        print("B. 216")
        print("C. 324")
        print("D. 432")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 17):
        print("Chon A, B, C ,D")
        print("Tim UCLN(125, 200)")
        print()
        print("A. 5")
        print("B. 10")
        print("C. 25")
        print("D. 50")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 18):
        print("Chon A, B, C ,D")
        print("Tim BCNN(75, 120)")
        print()
        print("A. 300")
        print("B. 450")
        print("C. 600")
        print("D. 900")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 19):
        print("Chon A, B, C ,D")
        print("So nho nhat chia het cho ca 12 va 18 la")
        print()
        print("A. 24")
        print("B. 30")
        print("C. 36")
        print("D. 48")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 20):
        print("Chon A, B, C ,D")
        print("Biet UCLN(a, b) = 14, a + b = 98, a > b va BCNN(a, b) = 140. Tim a")
        print()
        print("A. 56")
        print("B. 70")
        print("C. 84")
        print("D. 98")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

def snt(q):
    if (q == 1):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 21")
        print("B. 29")
        print("C. 35")
        print("D. 49")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 2):
        print("Chon A, B, C ,D")
        print("So nao khong phai so nguyen to?")
        print()
        print("A. 2")
        print("B. 3")
        print("C. 17")
        print("D. 21")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'D')

    if (q == 3):
        print("Chon A, B, C ,D")
        print("So nguyen to nho nhat lon hon 50")
        print()
        print("A. 51")
        print("B. 53")
        print("C. 55")
        print("D. 57")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 4):
        print("Chon A, B, C ,D")
        print("So nao la hop so?")
        print()
        print("A. 31")
        print("B. 37")
        print("C. 39")
        print("D. 41")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 5):
        print("Chon A, B, C ,D")
        print("Trong cac so sau, so nao la so nguyen to?")
        print()
        print("A. 51")
        print("B. 57")
        print("C. 59")
        print("D. 63")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 6):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 91")
        print("B. 93")
        print("C. 97")
        print("D. 99")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 7):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 121")
        print("B. 127")
        print("C. 129")
        print("D. 133")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 8):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 143")
        print("B. 149")
        print("C. 155")
        print("D. 161")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 9):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 169")
        print("B. 173")
        print("C. 175")
        print("D. 177")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 10):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 187")
        print("B. 191")
        print("C. 195")
        print("D. 201")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 11):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 203")
        print("B. 207")
        print("C. 211")
        print("D. 213")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 12):
        print("Chon A, B, C ,D")
        print("So nao khong phai so nguyen to?")
        print()
        print("A. 101")
        print("B. 103")
        print("C. 107")
        print("D. 111")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'D')

    if (q == 13):
        print("Chon A, B, C ,D")
        print("Neu p la so nguyen to lon hon 2 thi p la so")
        print()
        print("A. Chan")
        print("B. Le")
        print("C. Vua chan vua le")
        print("D. Khong xac dinh")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 14):
        print("Chon A, B, C ,D")
        print("Trong cac cap so sau, cap nao deu la so nguyen to?")
        print()
        print("A. (9, 11)")
        print("B. (13, 15)")
        print("C. (17, 19)")
        print("D. (21, 23)")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 15):
        print("Chon A, B, C ,D")
        print("Tong cua hai so nguyen to le bat ky la")
        print()
        print("A. So nguyen to")
        print("B. So hop")
        print("C. So chan")
        print("D. So le")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'C')

    if (q == 16):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 221")
        print("B. 223")
        print("C. 225")
        print("D. 231")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 17):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 247")
        print("B. 251")
        print("C. 253")
        print("D. 259")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 18):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 289")
        print("B. 293")
        print("C. 297")
        print("D. 299")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 19):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 301")
        print("B. 307")
        print("C. 309")
        print("D. 315")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')

    if (q == 20):
        print("Chon A, B, C ,D")
        print("So nao la so nguyen to?")
        print()
        print("A. 319")
        print("B. 331")
        print("C. 333")
        print("D. 341")
        a1 = str(input("Nhap cau tra loi: ")).strip().upper()
        return (a1 == 'B')


best = 0

if __name__ == "__main__":
    print_intro()
    print_topic_menu()

    while True:
        try:
            n = int(input("Nhap lua chon: "))
        except:
            print("Nhap sai! Hay nhap so.")
            continue

        if n == 0:
            break

        elif n == 1:
            da_chon = set()
            diem = 0
            print("Chon 10 so bat ky tu 1 den 20")

            stop_now = False

            q1 = nhap_cau_khong_trung(da_chon)
            if (pt2(q1) == True):
                diem += 1
                print("Ban lam dung roi")
                print()
            else:
                print("Ban lam sai roi")
            stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
            if (stop == "0"):
                stop_now = True

            if (stop_now == False):
                q2 = nhap_cau_khong_trung(da_chon)
                if (pt2(q2) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q3 = nhap_cau_khong_trung(da_chon)
                if (pt2(q3) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q4 = nhap_cau_khong_trung(da_chon)
                if (pt2(q4) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q5 = nhap_cau_khong_trung(da_chon)
                if (pt2(q5) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q6 = nhap_cau_khong_trung(da_chon)
                if (pt2(q6) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q7 = nhap_cau_khong_trung(da_chon)
                if (pt2(q7) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q8 = nhap_cau_khong_trung(da_chon)
                if (pt2(q8) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q9 = nhap_cau_khong_trung(da_chon)
                if (pt2(q9) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q10 = nhap_cau_khong_trung(da_chon)
                if (pt2(q10) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()

            if (diem > best):
                print(f"So diem cuoi cung ban dat duoc(tren thang 10) la {diem} (ket qua tot nhat) ")
                best = diem
            else:
                print(f"So diem cuoi cung ban dat duoc(tren thang 10) la {diem}")

        elif n == 2:
            da_chon = set()
            diem = 0
            print("Chon 10 so bat ky tu 1 den 20")

            stop_now = False

            q1 = nhap_cau_khong_trung(da_chon)
            if (ucbc(q1) == True):
                diem += 1
                print("Ban lam dung roi")
                print()
            else:
                print("Ban lam sai roi")
            stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
            if (stop == "0"):
                stop_now = True

            if (stop_now == False):
                q2 = nhap_cau_khong_trung(da_chon)
                if (ucbc(q2) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q3 = nhap_cau_khong_trung(da_chon)
                if (ucbc(q3) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q4 = nhap_cau_khong_trung(da_chon)
                if (ucbc(q4) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q5 = nhap_cau_khong_trung(da_chon)
                if (ucbc(q5) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q6 = nhap_cau_khong_trung(da_chon)
                if (ucbc(q6) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q7 = nhap_cau_khong_trung(da_chon)
                if (ucbc(q7) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q8 = nhap_cau_khong_trung(da_chon)
                if (ucbc(q8) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q9 = nhap_cau_khong_trung(da_chon)
                if (ucbc(q9) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q10 = nhap_cau_khong_trung(da_chon)
                if (ucbc(q10) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()

            if (diem > best):
                print(f"So diem cuoi cung ban dat duoc(tren thang 10) la {diem} (ket qua tot nhat) ")
                best = diem
            else:
                print(f"So diem cuoi cung ban dat duoc(tren thang 10) la {diem}")

        elif n == 3:
            da_chon = set()
            diem = 0
            print("Chon 10 so bat ky tu 1 den 20")

            stop_now = False

            q1 = nhap_cau_khong_trung(da_chon)
            if (snt(q1) == True):
                diem += 1
                print("Ban lam dung roi")
                print()
            else:
                print("Ban lam sai roi")
            stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
            if (stop == "0"):
                stop_now = True

            if (stop_now == False):
                q2 = nhap_cau_khong_trung(da_chon)
                if (snt(q2) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q3 = nhap_cau_khong_trung(da_chon)
                if (snt(q3) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q4 = nhap_cau_khong_trung(da_chon)
                if (snt(q4) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q5 = nhap_cau_khong_trung(da_chon)
                if (snt(q5) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q6 = nhap_cau_khong_trung(da_chon)
                if (snt(q6) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q7 = nhap_cau_khong_trung(da_chon)
                if (snt(q7) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q8 = nhap_cau_khong_trung(da_chon)
                if (snt(q8) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q9 = nhap_cau_khong_trung(da_chon)
                if (snt(q9) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()
                if (stop == "0"):
                    stop_now = True

            if (stop_now == False):
                q10 = nhap_cau_khong_trung(da_chon)
                if (snt(q10) == True):
                    diem += 1
                    print("Ban lam dung roi")
                    print()
                else:
                    print("Ban lam sai roi")
                stop = input("Neu ban muon coi ket qua bay gio hay nhap 0: ").strip()

            if (diem > best):
                print(f"So diem cuoi cung ban dat duoc(tren thang 10) la {diem} (ket qua tot nhat) ")
                best = diem
            else:
                print(f"So diem cuoi cung ban dat duoc(tren thang 10) la {diem}")
    
        else:
            print("Lua chon khong hop le. Hay chon lai.")

        print()
        print_topic_menu()
