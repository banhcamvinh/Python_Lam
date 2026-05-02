# === BUỔI 4: SCOPE VÀ *ARGS ===

# --- Scope (phạm vi biến) ---
x = 10  # Biến toàn cục

def ham_a():
    y = 5  # Biến cục bộ
    print(f"Trong hàm: x={x}, y={y}")

ham_a()
print(f"Ngoài hàm: x={x}")
# print(y)  # ❌ Lỗi! y không tồn tại ngoài hàm

# --- Biến cục bộ "che" biến toàn cục ---
ten = "Minh"

def thay_doi():
    ten = "Lan"  # Biến cục bộ mới, không ảnh hưởng bên ngoài
    print(f"Trong hàm: {ten}")

thay_doi()
print(f"Ngoài hàm: {ten}")  # Vẫn là Minh

# --- *args: nhận nhiều tham số ---
print("\n--- *args ---")

def tinh_trung_binh(*diem):
    if len(diem) == 0:
        return 0
    return sum(diem) / len(diem)

print(f"TB(8, 7, 9) = {tinh_trung_binh(8, 7, 9):.1f}")
print(f"TB(8, 7, 9, 6, 10) = {tinh_trung_binh(8, 7, 9, 6, 10):.1f}")

def in_thong_tin(ten, *mon_hoc):
    print(f"\n{ten} đăng ký:")
    for i, mon in enumerate(mon_hoc):
        print(f"  {i + 1}. {mon}")

in_thong_tin("Minh", "Toán", "Lý", "Tin")
in_thong_tin("Lan", "Hóa", "Sinh")
