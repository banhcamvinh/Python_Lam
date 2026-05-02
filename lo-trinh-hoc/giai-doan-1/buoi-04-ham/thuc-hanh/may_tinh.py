# === BÀI THỰC HÀNH: MÁY TÍNH BỎ TÚI ===

def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Lỗi: không thể chia cho 0!"
    return a / b

def hien_menu():
    print("\n=== MÁY TÍNH ===")
    print("1. Cộng (+)")
    print("2. Trừ (-)")
    print("3. Nhân (×)")
    print("4. Chia (÷)")
    print("0. Thoát")

# Chương trình chính
while True:
    hien_menu()
    chon = input("Chọn phép tính: ")

    if chon == "0":
        print("Tạm biệt! 👋")
        break

    if chon not in ["1", "2", "3", "4"]:
        print("⚠️ Lựa chọn không hợp lệ!")
        continue

    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))

    if chon == "1":
        print(f"Kết quả: {a} + {b} = {cong(a, b)}")
    elif chon == "2":
        print(f"Kết quả: {a} - {b} = {tru(a, b)}")
    elif chon == "3":
        print(f"Kết quả: {a} × {b} = {nhan(a, b)}")
    elif chon == "4":
        print(f"Kết quả: {a} ÷ {b} = {chia(a, b)}")
