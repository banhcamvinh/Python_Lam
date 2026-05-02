# === BÀI THỰC HÀNH: QUẢN LÝ LỚP HỌC ===

class SinhVien:
    def __init__(self, ten, ma_sv, diem):
        self.ten = ten
        self.ma_sv = ma_sv
        self.diem = diem

    def xep_loai(self):
        if self.diem >= 8.0:
            return "Giỏi"
        elif self.diem >= 6.5:
            return "Khá"
        elif self.diem >= 5.0:
            return "TB"
        return "Yếu"

    def __str__(self):
        return f"{self.ma_sv} | {self.ten:<15} | Điểm: {self.diem:.1f} | {self.xep_loai()}"


class LopHoc:
    def __init__(self, ten_lop):
        self.ten_lop = ten_lop
        self.danh_sach = []

    def them_sv(self, sv):
        self.danh_sach.append(sv)
        print(f"✅ Đã thêm {sv.ten}")

    def hien_thi(self):
        print(f"\n📋 Lớp {self.ten_lop} ({len(self.danh_sach)} SV):")
        print("-" * 50)
        for sv in self.danh_sach:
            print(f"  {sv}")
        print("-" * 50)

    def diem_trung_binh(self):
        if not self.danh_sach:
            return 0
        return sum(sv.diem for sv in self.danh_sach) / len(self.danh_sach)

    def sv_gioi_nhat(self):
        if not self.danh_sach:
            return None
        return max(self.danh_sach, key=lambda sv: sv.diem)


# --- Sử dụng ---
lop = LopHoc("CNTT01")
lop.them_sv(SinhVien("Minh", "SV001", 8.5))
lop.them_sv(SinhVien("Lan", "SV002", 7.0))
lop.them_sv(SinhVien("Hùng", "SV003", 9.2))
lop.them_sv(SinhVien("Mai", "SV004", 6.0))

lop.hien_thi()
print(f"\nĐiểm TB lớp: {lop.diem_trung_binh():.1f}")
print(f"SV giỏi nhất: {lop.sv_gioi_nhat()}")
