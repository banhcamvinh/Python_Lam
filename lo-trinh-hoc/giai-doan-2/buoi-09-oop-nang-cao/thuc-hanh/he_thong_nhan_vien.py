# === BÀI THỰC HÀNH: HỆ THỐNG NHÂN VIÊN ===

class NhanVien:
    def __init__(self, ten, ma_nv, luong_co_ban):
        self.ten = ten
        self.ma_nv = ma_nv
        self.luong_co_ban = luong_co_ban

    def tinh_luong(self):
        return self.luong_co_ban

    def __str__(self):
        return f"{self.ma_nv} | {self.ten:<15} | Lương: {self.tinh_luong():>12,.0f}đ"


class NhanVienFullTime(NhanVien):
    def __init__(self, ten, ma_nv, luong_co_ban, phu_cap=0):
        super().__init__(ten, ma_nv, luong_co_ban)
        self.phu_cap = phu_cap

    def tinh_luong(self):
        return self.luong_co_ban + self.phu_cap


class NhanVienPartTime(NhanVien):
    def __init__(self, ten, ma_nv, luong_gio, so_gio):
        super().__init__(ten, ma_nv, 0)
        self.luong_gio = luong_gio
        self.so_gio = so_gio

    def tinh_luong(self):
        return self.luong_gio * self.so_gio


# --- Sử dụng ---
nhan_vien = [
    NhanVienFullTime("Minh", "NV001", 15000000, 2000000),
    NhanVienFullTime("Lan", "NV002", 12000000, 1500000),
    NhanVienPartTime("Hùng", "NV003", 50000, 80),
    NhanVienPartTime("Mai", "NV004", 45000, 60),
]

print("=" * 55)
print("   BẢNG LƯƠNG NHÂN VIÊN")
print("=" * 55)
for nv in nhan_vien:
    print(f"  {nv}")

tong_luong = sum(nv.tinh_luong() for nv in nhan_vien)
print(f"\nTổng quỹ lương: {tong_luong:,.0f}đ")
