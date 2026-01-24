def input_int_in_range(prompt: str, lo: int, hi: int) -> int:
    while True:
        try:
            x = int(input(prompt))
            if lo <= x <= hi:
                return x
            print(f"Vui long nhap so trong [{lo}..{hi}].")
        except ValueError:
            print("Nhap sai. Vui long nhap so nguyen.")

def input_positive_float(prompt: str) -> float:
    while True:
        try:
            x = float(input(prompt))
            if x <= 0:
                print("Vui long nhap so > 0.")
                continue
            return x
        except ValueError:
            print("Nhap sai. Vui long nhap so (vi du: 12.5).")

def input_nonempty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Khong duoc de trong.")

def print_menu() -> None:
    print("\nWelcome to the Daily Expense Tracker!")
    print("Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")

def main() -> None:
    expenses = []  # list of dict: {"desc": str, "amount": float}

    while True:
        print_menu()
        choice = input_int_in_range("Nhap lua chon (1-5): ", 1, 5)

        if choice == 5:
            print("Exiting the Daily Expense Tracker. Goodbye!")
            break

        elif choice == 1:
            desc = input_nonempty("Nhap mo ta chi tieu (vd: an sang, mua sach): ")
            amount = input_positive_float("Nhap so tien chi (vd: 25.5): ")
            expenses.append({"desc": desc, "amount": amount})
            print("Expense added successfully!")

        elif choice == 2:
            if len(expenses) == 0:
                print("No expenses recorded yet.")
            else:
                print("Your expenses:")
                for i, item in enumerate(expenses, start=1):
                    print(f"{i}. {item['desc']} - {item['amount']}")

        elif choice == 3:
            if len(expenses) == 0:
                print("No expenses recorded yet.")
            else:
                total = sum(item["amount"] for item in expenses)
                average = total / len(expenses)
                print(f"Total expense: {total}")
                print(f"Average expense: {average}")

        elif choice == 4:
            if len(expenses) == 0:
                print("No expenses to clear.")
            else:
                confirm = input("Ban chac chan muon xoa het? (y/n): ").strip().lower()
                if confirm == "y":
                    expenses.clear()
                    print("All expenses cleared.")
                else:
                    print("Canceled. Expenses not cleared.")

if __name__ == "__main__":
    main()