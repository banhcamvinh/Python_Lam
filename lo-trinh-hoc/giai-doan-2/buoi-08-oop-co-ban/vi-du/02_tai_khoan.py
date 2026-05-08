# === BUỔI 7: VÍ DỤ TÀI KHOẢN NGÂN HÀNG ===

class TaiKhoan:
    def __init__(self, chu_tai_khoan, so_du=0):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.so_du += so_tien
            print(f"✅ Nạp {so_tien:,.0f}đ. Số dư: {self.so_du:,.0f}đ")
        else:
            print("⚠️ Số tiền phải > 0!")

    def rut_tien(self, so_tien):
        if so_tien > self.so_du:
            print(f"❌ Không đủ tiền! Số dư: {self.so_du:,.0f}đ")
        elif so_tien <= 0:
            print("⚠️ Số tiền phải > 0!")
        else:
            self.so_du -= so_tien
            print(f"✅ Rút {so_tien:,.0f}đ. Số dư: {self.so_du:,.0f}đ")

    def xem_so_du(self):
        print(f"💰 {self.chu_tai_khoan}: {self.so_du:,.0f}đ")


# --- Sử dụng ---
print("=== NGÂN HÀNG PYTHON ===\n")

tk = TaiKhoan("Minh", 1000000)
tk.xem_so_du()

print()
tk.nap_tien(500000)
tk.rut_tien(200000)
tk.rut_tien(2000000)  # Không đủ

print()
tk.xem_so_du()
