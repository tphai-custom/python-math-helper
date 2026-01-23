import random
from datetime import datetime

SCORE_FILE = "score.txt"
BEST_FILE = "best_score.txt"


def input_int_in_range(prompt: str, lo: int, hi: int) -> int:
    while True:
        try:
            x = int(input(prompt).strip())
            if lo <= x <= hi:
                return x
            print(f"Nhap sai! Chi duoc {lo} toi {hi}.")
        except ValueError:
            print("Nhap sai! Hay nhap so.")


def input_choice_abcd(prompt: str) -> str:
    while True:
        s = input(prompt).strip().upper()
        if s in ("A", "B", "C", "D"):
            return s
        print("Nhap sai! Chi duoc A, B, C, D.")


def print_intro() -> None:
    print("MATH HELPER - QUIZ + SCOREBOARD")
    print("Muc tieu: Luyen Toan bang quiz, cham diem, va luu diem vao score.txt")
    print("Huong dan:")
    print("- Chon chu de")
    print("- Tra loi 10 cau (random)")
    print("- Neu sai: hien dap an dung")
    print("- Diem se duoc luu tu dong\n")


def print_topic_menu() -> None:
    print("CHON CHU DE QUIZ")
    print("1) Phuong trinh bac 2 (ax^2 + bx + c = 0)")
    print("2) UCLN / BCNN")
    print("3) So nguyen to (prime)")
    print("0) Thoat")


def ask_question(q: dict) -> bool:
    print("Chon A, B, C, D")
    print(q["title"])
    print()
    for k in ("A", "B", "C", "D"):
        print(f"{k}. {q['options'][k]}")

    a = input_choice_abcd("Nhap cau tra loi: ")
    if a == q["ans"]:
        return True

    ans = q["ans"]
    print(f"Dap an dung: {ans}. {q['options'][ans]}")
    return False


def read_best_score() -> int:
    try:
        with open(BEST_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except Exception:
        return 0


def write_best_score(best: int) -> None:
    with open(BEST_FILE, "w", encoding="utf-8") as f:
        f.write(str(best))


def append_score(topic_name: str, score: int, total: int) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{ts} | topic={topic_name} | score={score}/{total}\n"
    with open(SCORE_FILE, "a", encoding="utf-8") as f:
        f.write(line)


PT2 = [
    None,
    {"title": "Tim m de phuong trinh: x^2 - (m + 1)x + (m - 2) = 0 co nghiem x = 2",
     "options": {"A": "-2", "B": "0", "C": "2", "D": "4"}, "ans": "B"},
    {"title": "Tim m de phuong trinh: 2x^2 - (m + 4)x + 2m = 0 co nghiem kep",
     "options": {"A": "0", "B": "2", "C": "4", "D": "8"}, "ans": "C"},
    {"title": "Tim k de phuong trinh: x^2 - 6x + k = 0 co x1^2 + x2^2 = 20",
     "options": {"A": "5", "B": "8", "C": "10", "D": "16"}, "ans": "B"},
    {"title": "Tim c de phuong trinh: x^2 + 4x + c = 0 co nghiem kep",
     "options": {"A": "0", "B": "2", "C": "4", "D": "8"}, "ans": "C"},
    {"title": "Tim m de phuong trinh: x^2 - 5x + m = 0 thoa 1/x1 + 1/x2 = 5/6",
     "options": {"A": "5", "B": "6", "C": "10", "D": "12"}, "ans": "B"},
    {"title": "Tim m de phuong trinh: x^2 + (m - 3)x + 2 = 0 co tong hai nghiem bang 1",
     "options": {"A": "0", "B": "1", "C": "2", "D": "3"}, "ans": "C"},
    {"title": "(m > 0) Tim m de phuong trinh: 3x^2 + mx + 3 = 0 co nghiem kep",
     "options": {"A": "3", "B": "6", "C": "9", "D": "12"}, "ans": "B"},
    {"title": "Tim m de phuong trinh: x^2 - (2m + 1)x + m(m + 1) = 0 co hai nghiem la 3 va 4",
     "options": {"A": "2", "B": "3", "C": "4", "D": "5"}, "ans": "B"},
    {"title": "Tim m de phuong trinh: x^2 - 8x + m = 0 co nghiem nho la 2",
     "options": {"A": "8", "B": "10", "C": "12", "D": "16"}, "ans": "C"},
    {"title": "Tim m de phuong trinh: x^2 + 2x + m = 0 thoa x1x2 = x1 + x2",
     "options": {"A": "-2", "B": "-1", "C": "0", "D": "2"}, "ans": "A"},
    {"title": "Tim m de phuong trinh: x^2 - 2x + m = 0 co x1^2 + x2^2 = 2",
     "options": {"A": "0", "B": "1", "C": "2", "D": "3"}, "ans": "B"},
    {"title": "Tim m de phuong trinh: 2x^2 + 5x + m = 0 co mot nghiem x = -2",
     "options": {"A": "-2", "B": "0", "C": "1", "D": "2"}, "ans": "D"},
    {"title": "(m > 0) Tim m de phuong trinh: x^2 + (m + 2)x + 4 = 0 co nghiem kep",
     "options": {"A": "2", "B": "4", "C": "6", "D": "8"}, "ans": "A"},
    {"title": "(m > 0) Tim m de phuong trinh: x^2 + mx + 9 = 0 co tong hai nghiem bang -8",
     "options": {"A": "6", "B": "7", "C": "8", "D": "9"}, "ans": "C"},
    {"title": "(m > 0) Tim m de phuong trinh: x^2 - mx + 16 = 0 co nghiem kep",
     "options": {"A": "4", "B": "6", "C": "8", "D": "10"}, "ans": "C"},
    {"title": "Tim m de phuong trinh: x^2 - (m + 4)x + m = 0 co nghiem x = 4",
     "options": {"A": "-4", "B": "-2", "C": "0", "D": "2"}, "ans": "C"},
    {"title": "Tim m de phuong trinh: x^2 - 3x + m = 0 co hai nghiem x1, x2 va x1 = 2x2",
     "options": {"A": "1", "B": "2", "C": "3", "D": "4"}, "ans": "B"},
    {"title": "Tim m de phuong trinh: x^2 - (m + 2)x + (2m - 3) = 0 co nghiem x = 3",
     "options": {"A": "-1", "B": "0", "C": "1", "D": "3"}, "ans": "B"},
    {"title": "Tim m de phuong trinh: x^2 - 7x + m = 0 co hai nghiem nguyen va hieu hai nghiem bang 1",
     "options": {"A": "10", "B": "11", "C": "12", "D": "13"}, "ans": "C"},
    {"title": "Tim m de phuong trinh: x^2 + (m - 1)x + (m - 2) = 0 co nghiem x = 1",
     "options": {"A": "-1", "B": "0", "C": "1", "D": "2"}, "ans": "C"},
]

UCBC = [
    None,
    {"title": "Tim UCLN(84, 126)",
     "options": {"A": "14", "B": "21", "C": "42", "D": "63"}, "ans": "C"},
    {"title": "Tim BCNN(18, 24)",
     "options": {"A": "36", "B": "48", "C": "72", "D": "96"}, "ans": "C"},
    {"title": "Tim UCLN(210, 330)",
     "options": {"A": "10", "B": "15", "C": "30", "D": "60"}, "ans": "C"},
    {"title": "Tim BCNN(36, 90)",
     "options": {"A": "120", "B": "180", "C": "240", "D": "360"}, "ans": "B"},
    {"title": "Tim UCLN(48, 180)",
     "options": {"A": "6", "B": "12", "C": "18", "D": "24"}, "ans": "B"},
    {"title": "Tim BCNN(45, 60)",
     "options": {"A": "90", "B": "120", "C": "150", "D": "180"}, "ans": "D"},
    {"title": "Tim UCLN(96, 144)",
     "options": {"A": "24", "B": "36", "C": "48", "D": "72"}, "ans": "C"},
    {"title": "Tim BCNN(14, 35)",
     "options": {"A": "49", "B": "70", "C": "105", "D": "140"}, "ans": "B"},
    {"title": "Neu UCLN(a, b) = 6 va BCNN(a, b) = 180 thi a*b bang bao nhieu?",
     "options": {"A": "540", "B": "720", "C": "1080", "D": "2160"}, "ans": "C"},
    {"title": "Tim a (<72) biet UCLN(a, 72) = 9 va a la boi cua 27",
     "options": {"A": "27", "B": "36", "C": "54", "D": "63"}, "ans": "A"},
    {"title": "Tim x (30 < x < 60) biet UCLN(x, 60) = 15",
     "options": {"A": "30", "B": "35", "C": "45", "D": "50"}, "ans": "C"},
    {"title": "Tim x biet BCNN(x, 20) = 60; x la uoc cua 60; x chan va khong chia het cho 5",
     "options": {"A": "10", "B": "12", "C": "15", "D": "30"}, "ans": "B"},
    {"title": "Biet UCLN(56, b) = 8 va BCNN(56, b) = 280. Tim b",
     "options": {"A": "32", "B": "40", "C": "56", "D": "80"}, "ans": "B"},
    {"title": "Biet UCLN(a, 48) = 16 va BCNN(a, 48) = 240. Tim a",
     "options": {"A": "64", "B": "72", "C": "80", "D": "96"}, "ans": "C"},
    {"title": "Tim UCLN(405, 1125)",
     "options": {"A": "15", "B": "25", "C": "45", "D": "75"}, "ans": "C"},
    {"title": "Tim BCNN(72, 108)",
     "options": {"A": "144", "B": "216", "C": "324", "D": "432"}, "ans": "B"},
    {"title": "Tim UCLN(125, 200)",
     "options": {"A": "5", "B": "10", "C": "25", "D": "50"}, "ans": "C"},
    {"title": "Tim BCNN(75, 120)",
     "options": {"A": "300", "B": "450", "C": "600", "D": "900"}, "ans": "C"},
    {"title": "So nho nhat chia het cho ca 12 va 18 la",
     "options": {"A": "24", "B": "30", "C": "36", "D": "48"}, "ans": "C"},
    {"title": "Biet UCLN(a, b) = 14, a + b = 98, a > b va BCNN(a, b) = 140. Tim a",
     "options": {"A": "56", "B": "70", "C": "84", "D": "98"}, "ans": "B"},
]

SNT = [
    None,
    {"title": "So nao la so nguyen to?",
     "options": {"A": "21", "B": "29", "C": "35", "D": "49"}, "ans": "B"},
    {"title": "So nao khong phai so nguyen to?",
     "options": {"A": "2", "B": "3", "C": "17", "D": "21"}, "ans": "D"},
    {"title": "So nguyen to nho nhat lon hon 50",
     "options": {"A": "51", "B": "53", "C": "55", "D": "57"}, "ans": "B"},
    {"title": "So nao la hop so?",
     "options": {"A": "31", "B": "37", "C": "39", "D": "41"}, "ans": "C"},
    {"title": "Trong cac so sau, so nao la so nguyen to?",
     "options": {"A": "51", "B": "57", "C": "59", "D": "63"}, "ans": "C"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "91", "B": "93", "C": "97", "D": "99"}, "ans": "C"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "121", "B": "127", "C": "129", "D": "133"}, "ans": "B"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "143", "B": "149", "C": "155", "D": "161"}, "ans": "B"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "169", "B": "173", "C": "175", "D": "177"}, "ans": "B"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "187", "B": "191", "C": "195", "D": "201"}, "ans": "B"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "203", "B": "207", "C": "211", "D": "213"}, "ans": "C"},
    {"title": "So nao khong phai so nguyen to?",
     "options": {"A": "101", "B": "103", "C": "107", "D": "111"}, "ans": "D"},
    {"title": "Neu p la so nguyen to lon hon 2 thi p la so",
     "options": {"A": "Chan", "B": "Le", "C": "Vua chan vua le", "D": "Khong xac dinh"}, "ans": "B"},
    {"title": "Trong cac cap so sau, cap nao deu la so nguyen to?",
     "options": {"A": "(9, 11)", "B": "(13, 15)", "C": "(17, 19)", "D": "(21, 23)"}, "ans": "C"},
    {"title": "Tong cua hai so nguyen to le bat ky la",
     "options": {"A": "So nguyen to", "B": "So hop", "C": "So chan", "D": "So le"}, "ans": "C"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "221", "B": "223", "C": "225", "D": "231"}, "ans": "B"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "247", "B": "251", "C": "253", "D": "259"}, "ans": "B"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "289", "B": "293", "C": "297", "D": "299"}, "ans": "B"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "301", "B": "307", "C": "309", "D": "315"}, "ans": "B"},
    {"title": "So nao la so nguyen to?",
     "options": {"A": "319", "B": "331", "C": "333", "D": "341"}, "ans": "B"},
]


def run_quiz(topic_id: int, best: int) -> int:
    if topic_id == 1:
        topic_name = "PT2"
        bank = PT2
    elif topic_id == 2:
        topic_name = "UCBC"
        bank = UCBC
    else:
        topic_name = "SNT"
        bank = SNT

    all_ids = list(range(1, 21))
    random.shuffle(all_ids)
    chosen_ids = all_ids[:10]

    diem = 0
    stop_now = False

    print("He thong se tu dong chon ngau nhien 10 cau (khong trung).")

    for i, qid in enumerate(chosen_ids, start=1):
        print(f"---- Cau {i}/10 ----")
        ok = ask_question(bank[qid])

        if ok:
            diem += 1
            print("Ban lam dung roi\n")
        else:
            print("Ban lam sai roi\n")
            stop = input("Neu ban muon dung som va coi ket qua bay gio hay nhap 0: ").strip()
            if stop == "0":
                stop_now = True

        if stop_now:
            break

    if diem > best:
        print(f"So diem cuoi cung ban dat duoc (tren thang 10) la {diem} (ket qua tot nhat)")
        best = diem
        write_best_score(best)
    else:
        print(f"So diem cuoi cung ban dat duoc (tren thang 10) la {diem}")

    append_score(topic_name, diem, 10)
    print(f"(Da luu vao {SCORE_FILE})\n")
    return best


def main() -> None:
    print_intro()
    best = read_best_score()

    while True:
        print_topic_menu()
        try:
            n = int(input("Nhap lua chon: ").strip())
        except ValueError:
            print("Nhap sai! Hay nhap so.\n")
            continue

        if n == 0:
            break
        elif n in (1, 2, 3):
            best = run_quiz(n, best)
        else:
            print("Lua chon khong hop le. Hay chon lai.\n")


if __name__ == "__main__":
    main()