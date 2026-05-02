# === BÀI THỰC HÀNH: MÁY TÍNH TIỀN TRÀ SỮA ===

print("=" * 30)
print("   MENU TRÀ SỮA")
print("=" * 30)
print("1. Trà sữa trân châu: 35,000đ")
print("2. Trà sữa matcha:    40,000đ")
print("3. Trà đào:           30,000đ")
print("=" * 30)

# Nhập số lượng
tra_sua = int(input("Số ly trà sữa trân châu: "))
matcha = int(input("Số ly trà sữa matcha: "))
tra_dao = int(input("Số ly trà đào: "))

# Tính toán
tong_ly = tra_sua + matcha + tra_dao
tong_tien = tra_sua * 35000 + matcha * 40000 + tra_dao * 30000

print(f"\n--- HÓA ĐƠN ---")
print(f"Trà sữa trân châu x{tra_sua}: {tra_sua * 35000:>10,}đ")
print(f"Trà sữa matcha    x{matcha}: {matcha * 40000:>10,}đ")
print(f"Trà đào           x{tra_dao}: {tra_dao * 30000:>10,}đ")
print(f"{'':->30}")

# Giảm giá nếu mua từ 5 ly
if tong_ly >= 5:
    giam_gia = tong_tien * 0.1
    print(f"Giảm 10% (mua {tong_ly} ly): -{giam_gia:>8,.0f}đ")
    tong_tien = tong_tien - giam_gia

print(f"TỔNG CỘNG:         {tong_tien:>10,.0f}đ")
