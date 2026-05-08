# === MINI PROJECT 2: QUẢN LÝ SINH VIÊN (OOP + JSON) ===
import json
import os


class SinhVien:
    def __init__(self, ten, ma_sv, diem_toan=0, diem_ly=0, diem_hoa=0):
        self.ten = ten
        self.ma_sv = ma_sv
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def diem_tb(self):
        return (self.diem_toan + self.diem_ly + self.diem_hoa) / 3

    def xep_loai(self):
        dtb = self.diem_tb()
        if dtb >= 8.0:
            return "Giỏi"
        elif dtb >= 6.5:
            return "Khá"
        elif dtb >= 5.0:
            return "TB"
        return "Yếu"

    def to_dict(self):
        return {
            "ten": self.ten, "ma_sv": self.ma_sv,
            "diem_toan": self.diem_toan,
            "diem_ly": self.diem_ly,
            "diem_hoa": self.diem_hoa
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["ten"], data["ma_sv"],
                   data["diem_toan"], data["diem_ly"], data["diem_hoa"])

    def __str__(self):
        return (f"{self.ma_sv} | {self.ten:<15} | "
                f"T:{self.diem_toan} L:{self.diem_ly} H:{self.diem_hoa} | "
                f"TB:{self.diem_tb():.1f} | {self.xep_loai()}")


class QuanLySinhVien:
    FILE = "sinh_vien.json"

    def __init__(self):
        self.danh_sach = []
        self.doc_file()

    def doc_file(self):
        if os.path.exists(self.FILE):
            try:
                with open(self.FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.danh_sach = [SinhVien.from_dict(sv) for sv in data]
            except (json.JSONDecodeError, KeyError):
                self.danh_sach = []

    def luu_file(self):
        with open(self.FILE, "w", encoding="utf-8") as f:
            json.dump([sv.to_dict() for sv in self.danh_sach],
                      f, ensure_ascii=False, indent=2)

    def them_sv(self):
        ten = input("Họ tên: ").strip()
        ma_sv = input("Mã SV: ").strip()

        for sv in self.danh_sach:
            if sv.ma_sv == ma_sv:
                print(f"⚠️ Mã {ma_sv} đã tồn tại!")
                return
        try:
            toan = float(input("Điểm Toán: "))
            ly = float(input("Điểm Lý: "))
            hoa = float(input("Điểm Hóa: "))
        except ValueError:
            print("⚠️ Điểm phải là số!")
            return

        self.danh_sach.append(SinhVien(ten, ma_sv, toan, ly, hoa))
        self.luu_file()
        print(f"✅ Đã thêm {ten}")

    def hien_thi(self):
        if not self.danh_sach:
            print("📭 Chưa có sinh viên!")
            return
        print(f"\n📋 Danh sách ({len(self.danh_sach)} SV):")
        print("-" * 65)
        for sv in self.danh_sach:
            print(f"  {sv}")
        print("-" * 65)

    def tim_kiem(self):
        kw = input("Nhập tên hoặc mã SV: ").strip().lower()
        kq = [sv for sv in self.danh_sach
              if kw in sv.ten.lower() or kw in sv.ma_sv.lower()]
        if not kq:
            print(f"🔍 Không tìm thấy '{kw}'")
        else:
            for sv in kq:
                print(f"  {sv}")

    def xoa_sv(self):
        ma = input("Mã SV cần xóa: ").strip()
        for i, sv in enumerate(self.danh_sach):
            if sv.ma_sv == ma:
                if input(f"Xóa {sv.ten}? (c/k): ").lower() == "c":
                    self.danh_sach.pop(i)
                    self.luu_file()
                    print("🗑️ Đã xóa!")
                return
        print(f"🔍 Không tìm thấy '{ma}'")

    def thong_ke(self):
        if not self.danh_sach:
            print("📭 Chưa có dữ liệu!")
            return

        dtb_list = [sv.diem_tb() for sv in self.danh_sach]
        top = max(self.danh_sach, key=lambda s: s.diem_tb())

        print(f"\n📊 THỐNG KÊ")
        print(f"  Tổng: {len(self.danh_sach)} SV")
        print(f"  Điểm TB lớp: {sum(dtb_list) / len(dtb_list):.1f}")
        print(f"  Giỏi nhất: {top.ten} (TB: {top.diem_tb():.1f})")

        for loai in ["Giỏi", "Khá", "TB", "Yếu"]:
            sl = sum(1 for sv in self.danh_sach if sv.xep_loai() == loai)
            print(f"    {loai}: {sl}")

    def chay(self):
        print("=" * 40)
        print("   🎓 QUẢN LÝ SINH VIÊN")
        print("=" * 40)

        while True:
            print("\n1. ➕ Thêm  2. 📋 Xem  3. 🔍 Tìm")
            print("4. 🗑️  Xóa  5. 📊 Thống kê  0. Thoát")
            chon = input("Chọn: ")

            if chon == "1": self.them_sv()
            elif chon == "2": self.hien_thi()
            elif chon == "3": self.tim_kiem()
            elif chon == "4": self.xoa_sv()
            elif chon == "5": self.thong_ke()
            elif chon == "0":
                print("Tạm biệt! 👋")
                break


QuanLySinhVien().chay()
