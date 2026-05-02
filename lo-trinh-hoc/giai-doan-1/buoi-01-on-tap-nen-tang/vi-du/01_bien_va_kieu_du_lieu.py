# === BUỔI 1: BIẾN VÀ KIỂU DỮ LIỆU ===

# --- Tạo biến ---
ten = "Minh"
tuoi = 18
diem = 8.5
dang_hoc = True

print("--- Thông tin sinh viên ---")
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Điểm TB: {diem}")
print(f"Đang học: {dang_hoc}")

# --- Kiểm tra kiểu dữ liệu ---
print("\n--- Kiểu dữ liệu ---")
print(f"ten là kiểu: {type(ten)}")
print(f"tuoi là kiểu: {type(tuoi)}")
print(f"diem là kiểu: {type(diem)}")
print(f"dang_hoc là kiểu: {type(dang_hoc)}")

# --- Chuyển đổi kiểu ---
print("\n--- Chuyển đổi kiểu ---")
so_text = "42"
so = int(so_text)
print(f'"{so_text}" (chuỗi) -> {so} (số nguyên)')
print(f"Cộng thêm 8: {so + 8}")

# --- Toán tử ---
print("\n--- Toán tử ---")
a = 17
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}  (chia lấy phần nguyên)")
print(f"{a} % {b} = {a % b}   (chia lấy dư)")
print(f"{a} ** {b} = {a ** b} (lũy thừa)")
