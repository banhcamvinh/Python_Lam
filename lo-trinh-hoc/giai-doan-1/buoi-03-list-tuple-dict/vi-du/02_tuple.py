# === BUỔI 3: TUPLE (BỘ GIÁ TRỊ) ===

# --- Tạo tuple ---
toa_do = (10, 20)
mau_sac = ("đỏ", "xanh", "vàng")
ngay_sinh = (15, 8, 2005)

print("--- Tuple cơ bản ---")
print(f"Tọa độ: {toa_do}")
print(f"Màu sắc: {mau_sac}")
print(f"Ngày sinh: {ngay_sinh}")

# --- Truy cập ---
print(f"\nMàu đầu tiên: {mau_sac[0]}")
print(f"Màu cuối: {mau_sac[-1]}")
print(f"Số phần tử: {len(mau_sac)}")

# --- Unpacking ---
print("\n--- Unpacking ---")
x, y = toa_do
print(f"x = {x}, y = {y}")

ngay, thang, nam = ngay_sinh
print(f"Ngày sinh: {ngay}/{thang}/{nam}")

# --- Tuple không thể thay đổi ---
print("\n--- Tuple là bất biến ---")
print("Thử sửa tuple sẽ bị lỗi TypeError")
# mau_sac[0] = "tím"  # ❌ Lỗi! Không thể sửa tuple

# --- Duyệt tuple ---
print("\n--- Duyệt tuple ---")
for mau in mau_sac:
    print(f"  Màu: {mau}")

# --- So sánh List vs Tuple ---
print("\n--- So sánh ---")
ds = [1, 2, 3]    # List - thay đổi được
bo = (1, 2, 3)    # Tuple - không thay đổi được

ds[0] = 99
print(f"List sau khi sửa: {ds}")
print(f"Tuple giữ nguyên: {bo}")
