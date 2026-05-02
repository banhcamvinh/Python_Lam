# === BUỔI 2: WHILE, BREAK, CONTINUE ===

# --- while cơ bản ---
print("--- Đếm từ 1 đến 5 bằng while ---")
dem = 1
while dem <= 5:
    print(dem, end=" ")
    dem += 1  # Nhớ tăng biến đếm!
print()

# --- while với điều kiện ---
print("\n--- Nhập mật khẩu ---")
mat_khau_dung = "python123"
so_lan_thu = 0
gioi_han = 3

while so_lan_thu < gioi_han:
    mat_khau = input(f"Nhập mật khẩu (còn {gioi_han - so_lan_thu} lần): ")
    so_lan_thu += 1

    if mat_khau == mat_khau_dung:
        print("✅ Đăng nhập thành công!")
        break
else:
    # else của while chạy khi vòng lặp kết thúc bình thường (không bị break)
    print("❌ Đã hết lượt thử. Tài khoản bị khóa!")

# --- break ---
print("\n--- Tìm bội số của 13 đầu tiên > 100 ---")
for so in range(101, 200):
    if so % 13 == 0:
        print(f"Tìm thấy: {so}")
        break

# --- continue ---
print("\n--- In số lẻ từ 1 đến 20 (dùng continue) ---")
for i in range(1, 21):
    if i % 2 == 0:
        continue  # Bỏ qua số chẵn
    print(i, end=" ")
print()

# --- Menu chương trình ---
print("\n=== CHƯƠNG TRÌNH TÍNH TOÁN ===")
while True:
    print("\n1. Tính diện tích hình tròn")
    print("2. Tính diện tích hình chữ nhật")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        r = float(input("Nhập bán kính: "))
        print(f"Diện tích = {3.14159 * r ** 2:.2f}")
    elif chon == "2":
        dai = float(input("Nhập chiều dài: "))
        rong = float(input("Nhập chiều rộng: "))
        print(f"Diện tích = {dai * rong:.2f}")
    elif chon == "0":
        print("Tạm biệt! 👋")
        break
    else:
        print("⚠️ Lựa chọn không hợp lệ!")
