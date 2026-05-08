# === BÀI THỰC HÀNH: PHÂN TÍCH DỮ LIỆU BÁN HÀNG ===

don_hang = [
    {"sp": "Laptop", "gia": 15000000, "sl": 2, "thang": 1},
    {"sp": "Chuột", "gia": 200000, "sl": 10, "thang": 1},
    {"sp": "Laptop", "gia": 15000000, "sl": 1, "thang": 2},
    {"sp": "Bàn phím", "gia": 500000, "sl": 5, "thang": 2},
    {"sp": "Chuột", "gia": 200000, "sl": 8, "thang": 2},
    {"sp": "Màn hình", "gia": 5000000, "sl": 3, "thang": 3},
    {"sp": "Laptop", "gia": 15000000, "sl": 3, "thang": 3},
]

print("=" * 45)
print("   📊 BÁO CÁO BÁN HÀNG")
print("=" * 45)

# 1. Tổng doanh thu
tong_dt = sum(d["gia"] * d["sl"] for d in don_hang)
print(f"\n💰 Tổng doanh thu: {tong_dt:,.0f}đ")

# 2. Doanh thu theo tháng
print("\n📅 Theo tháng:")
for thang in sorted(set(d["thang"] for d in don_hang)):
    dt = sum(d["gia"] * d["sl"] for d in don_hang if d["thang"] == thang)
    thanh = "█" * int(dt / tong_dt * 30)
    print(f"  Tháng {thang}: {dt:>14,.0f}đ {thanh}")

# 3. Sản phẩm bán chạy nhất
sp_sl = {}
for d in don_hang:
    sp_sl[d["sp"]] = sp_sl.get(d["sp"], 0) + d["sl"]

sp_sorted = sorted(sp_sl.items(), key=lambda x: x[1], reverse=True)
print("\n🏆 Xếp hạng bán chạy:")
for i, (sp, sl) in enumerate(sp_sorted):
    print(f"  {i + 1}. {sp}: {sl} cái")

# 4. Đơn hàng lớn nhất
don_lon = max(don_hang, key=lambda d: d["gia"] * d["sl"])
print(f"\n📦 Đơn lớn nhất: {don_lon['sp']} x{don_lon['sl']} = "
      f"{don_lon['gia'] * don_lon['sl']:,.0f}đ")

# 5. Doanh thu theo sản phẩm
print("\n📈 Doanh thu theo SP:")
sp_dt = {}
for d in don_hang:
    sp_dt[d["sp"]] = sp_dt.get(d["sp"], 0) + d["gia"] * d["sl"]

for sp, dt in sorted(sp_dt.items(), key=lambda x: x[1], reverse=True):
    print(f"  {sp:<12}: {dt:>14,.0f}đ")
