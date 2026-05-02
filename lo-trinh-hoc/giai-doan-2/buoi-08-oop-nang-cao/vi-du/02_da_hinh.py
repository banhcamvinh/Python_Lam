# === BUỔI 8: ĐA HÌNH ===

class HinhHoc:
    def tinh_dien_tich(self):
        return 0

    def mo_ta(self):
        return "Hình học"


class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return 3.14159 * self.ban_kinh ** 2

    def mo_ta(self):
        return f"Hình tròn (r={self.ban_kinh})"


class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def mo_ta(self):
        return f"HCN ({self.dai}x{self.rong})"


class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

    def mo_ta(self):
        return f"Hình vuông (a={self.dai})"


# --- Đa hình: cùng gọi nhưng kết quả khác ---
print("=== TÍNH DIỆN TÍCH ===\n")

cac_hinh = [
    HinhTron(5),
    HinhChuNhat(4, 6),
    HinhVuong(3),
    HinhTron(10),
]

for hinh in cac_hinh:
    print(f"  {hinh.mo_ta():<25} S = {hinh.tinh_dien_tich():.2f}")
