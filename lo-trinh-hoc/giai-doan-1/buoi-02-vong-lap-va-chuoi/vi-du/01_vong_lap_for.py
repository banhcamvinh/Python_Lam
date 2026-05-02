# === BUỔI 2: VÒNG LẶP FOR ===

# --- range() cơ bản ---
print("--- Đếm từ 0 đến 4 ---")
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()  # Xuống dòng

print("\n--- Đếm từ 1 đến 10 ---")
for i in range(1, 11):
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9 10
print()

print("\n--- Số chẵn từ 0 đến 20 ---")
for i in range(0, 21, 2):
    print(i, end=" ")  # 0 2 4 6 8 10 12 14 16 18 20
print()

print("\n--- Đếm ngược ---")
for i in range(10, 0, -1):
    print(i, end=" ")
print("🚀 Phóng!")

# --- Bảng cửu chương ---
so = int(input("\nNhập số cần in bảng cửu chương: "))
print(f"\n--- Bảng cửu chương {so} ---")
for i in range(1, 11):
    print(f"{so} x {i:>2} = {so * i:>3}")

# --- Tính tổng ---
n = int(input("\nTính tổng từ 1 đến n. Nhập n: "))
tong = 0
for i in range(1, n + 1):
    tong += i
print(f"Tổng từ 1 đến {n} = {tong}")

# Kiểm tra: công thức n*(n+1)/2
print(f"Kiểm tra bằng công thức: {n * (n + 1) // 2}")
