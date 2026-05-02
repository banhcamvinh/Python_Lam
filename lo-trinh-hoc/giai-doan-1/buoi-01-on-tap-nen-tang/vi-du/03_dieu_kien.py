# === BUỔI 1: CÂU ĐIỀU KIỆN ===

# --- Ví dụ 1: Xếp loại học lực ---
print("=== XẾP LOẠI HỌC LỰC ===")
diem = float(input("Nhập điểm trung bình: "))

if diem >= 9.0:
    xep_loai = "Xuất sắc"
elif diem >= 8.0:
    xep_loai = "Giỏi"
elif diem >= 6.5:
    xep_loai = "Khá"
elif diem >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print(f"Điểm: {diem} -> Xếp loại: {xep_loai}")

# --- Ví dụ 2: Kết hợp điều kiện ---
print("\n=== KIỂM TRA ĐĂNG KÝ MÔN HỌC ===")
so_tin_chi_da_hoc = int(input("Số tín chỉ đã hoàn thành: "))
diem_tb = float(input("Điểm trung bình tích lũy: "))

if so_tin_chi_da_hoc >= 30 and diem_tb >= 5.0:
    print("✅ Đủ điều kiện đăng ký môn chuyên ngành")
elif so_tin_chi_da_hoc >= 30:
    print("⚠️ Đủ tín chỉ nhưng điểm TB chưa đạt")
elif diem_tb >= 5.0:
    print("⚠️ Điểm TB đạt nhưng chưa đủ tín chỉ")
else:
    print("❌ Chưa đủ điều kiện")
