# === BUỔI 5: XỬ LÝ NGOẠI LỆ (TRY/EXCEPT) ===

# --- ValueError ---
print("--- Xử lý nhập sai kiểu ---")
try:
    tuoi = int(input("Nhập tuổi: "))
    print(f"Tuổi: {tuoi}")
except ValueError:
    print("⚠️ Bạn phải nhập số nguyên!")

# --- FileNotFoundError ---
print("\n--- Xử lý file không tồn tại ---")
try:
    with open("khong_co.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("❌ File không tồn tại!")

# --- ZeroDivisionError ---
print("\n--- Xử lý chia cho 0 ---")
try:
    a = int(input("Nhập số bị chia: "))
    b = int(input("Nhập số chia: "))
    print(f"{a} / {b} = {a / b:.2f}")
except ValueError:
    print("⚠️ Phải nhập số!")
except ZeroDivisionError:
    print("⚠️ Không thể chia cho 0!")

# --- try/except/else/finally ---
print("\n--- Đầy đủ: try/except/else/finally ---")
try:
    with open("ket_qua.txt", "r", encoding="utf-8") as f:
        noi_dung = f.read()
except FileNotFoundError:
    print("❌ File không tồn tại")
else:
    print(f"✅ Đọc thành công! ({len(noi_dung)} ký tự)")
finally:
    print("🏁 Hoàn tất xử lý")

# --- Hàm nhập số an toàn ---
print("\n--- Hàm nhập số an toàn ---")

def nhap_so(thong_bao="Nhập số: "):
    """Hỏi cho đến khi nhập đúng số"""
    while True:
        try:
            return float(input(thong_bao))
        except ValueError:
            print("⚠️ Vui lòng nhập số!")

diem = nhap_so("Nhập điểm: ")
print(f"Điểm: {diem}")
