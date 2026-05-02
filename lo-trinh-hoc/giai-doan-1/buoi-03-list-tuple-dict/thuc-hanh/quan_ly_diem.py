# === BÀI THỰC HÀNH: QUẢN LÝ ĐIỂM SINH VIÊN ===

diem_lop = []

# Nhập điểm
so_sv = int(input("Nhập số sinh viên: "))

for i in range(so_sv):
    print(f"\n--- Sinh viên {i + 1} ---")
    ten = input("Họ tên: ")
    diem = float(input("Điểm TB: "))
    diem_lop.append({"ten": ten, "diem": diem})

# Hiển thị bảng điểm
print("\n" + "=" * 45)
print("   BẢNG ĐIỂM LỚP")
print("=" * 45)

for i, sv in enumerate(diem_lop):
    if sv["diem"] >= 8.0:
        loai = "Giỏi ⭐"
    elif sv["diem"] >= 6.5:
        loai = "Khá 👍"
    elif sv["diem"] >= 5.0:
        loai = "TB 😊"
    else:
        loai = "Yếu 😟"
    print(f"  {i + 1}. {sv['ten']:<15} | Điểm: {sv['diem']:.1f} | {loai}")

# Thống kê
tat_ca_diem = [sv["diem"] for sv in diem_lop]
print(f"\n--- Thống kê ---")
print(f"  Điểm cao nhất: {max(tat_ca_diem):.1f}")
print(f"  Điểm thấp nhất: {min(tat_ca_diem):.1f}")
print(f"  Điểm TB lớp: {sum(tat_ca_diem) / len(tat_ca_diem):.1f}")
