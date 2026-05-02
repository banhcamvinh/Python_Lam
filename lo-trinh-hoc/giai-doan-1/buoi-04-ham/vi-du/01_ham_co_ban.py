# === BUỔI 4: HÀM CƠ BẢN ===

# --- Hàm không tham số ---
def chao():
    print("Xin chào các bạn! 👋")
    print("Chào mừng đến với buổi học Python\n")

chao()

# --- Hàm có tham số ---
def chao_ten(ten):
    print(f"Xin chào {ten}!")

chao_ten("Minh")
chao_ten("Lan")

# --- Hàm có return ---
def tinh_dien_tich(dai, rong):
    return dai * rong

dt1 = tinh_dien_tich(5, 4)
dt2 = tinh_dien_tich(3, 2.5)
print(f"\nPhòng khách: {dt1} m²")
print(f"Bếp: {dt2} m²")

# --- Hàm trả về nhiều giá trị ---
def tinh_toan(a, b):
    return a + b, a - b, a * b

tong, hieu, tich = tinh_toan(10, 3)
print(f"\n10 và 3: tổng={tong}, hiệu={hieu}, tích={tich}")

# --- Giá trị mặc định ---
def tinh_gia(gia_goc, giam=0):
    return gia_goc - gia_goc * giam / 100

print(f"\nGiá gốc: {tinh_gia(100000):,.0f}đ")
print(f"Giảm 10%: {tinh_gia(100000, 10):,.0f}đ")
print(f"Giảm 25%: {tinh_gia(100000, 25):,.0f}đ")
