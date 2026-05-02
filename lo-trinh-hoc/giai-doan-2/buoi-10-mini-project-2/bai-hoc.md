# Buổi 10: Mini Project 2 - Quản Lý Sinh Viên (OOP + File)

## Mục tiêu buổi học
- Tổng hợp kiến thức OOP: class, kế thừa, đóng gói
- Kết hợp OOP với đọc/ghi file JSON
- Xây dựng ứng dụng có cấu trúc rõ ràng

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-10 phút | Phân tích yêu cầu, thiết kế class |
| 10-30 phút | Code class SinhVien và LopHoc |
| 30-55 phút | Code lưu/đọc JSON và menu |
| 55-75 phút | Hoàn thiện và test |
| 75-90 phút | Review, gợi ý cải tiến |

---

## Yêu Cầu Ứng Dụng

### Chức năng
1. Thêm sinh viên (tên, mã SV, điểm các môn)
2. Xem danh sách sinh viên
3. Tìm kiếm theo tên hoặc mã SV
4. Xóa sinh viên
5. Thống kê (điểm TB lớp, SV giỏi nhất, phân loại)
6. Lưu/đọc dữ liệu từ file JSON

---

## Code Hoàn Chỉnh

```python
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
            "ten": self.ten,
            "ma_sv": self.ma_sv,
            "diem_toan": self.diem_toan,
            "diem_ly": self.diem_ly,
            "diem_hoa": self.diem_hoa
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["ten"], data["ma_sv"],
            data["diem_toan"], data["diem_ly"], data["diem_hoa"]
        )

    def __str__(self):
        return (f"{self.ma_sv} | {self.ten:<15} | "
                f"T:{self.diem_toan} L:{self.diem_ly} H:{self.diem_hoa} | "
                f"TB:{self.diem_tb():.1f} | {self.xep_loai()}")


class QuanLySinhVien:
    FILE_DU_LIEU = "sinh_vien.json"

    def __init__(self):
        self.danh_sach = []
        self.doc_file()

    def doc_file(self):
        if os.path.exists(self.FILE_DU_LIEU):
            try:
                with open(self.FILE_DU_LIEU, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.danh_sach = [SinhVien.from_dict(sv) for sv in data]
            except (json.JSONDecodeError, KeyError):
                self.danh_sach = []

    def luu_file(self):
        with open(self.FILE_DU_LIEU, "w", encoding="utf-8") as f:
            data = [sv.to_dict() for sv in self.danh_sach]
            json.dump(data, f, ensure_ascii=False, indent=2)

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

        sv = SinhVien(ten, ma_sv, toan, ly, hoa)
        self.danh_sach.append(sv)
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
        tu_khoa = input("Nhập tên hoặc mã SV: ").strip().lower()
        ket_qua = [sv for sv in self.danh_sach
                    if tu_khoa in sv.ten.lower() or tu_khoa in sv.ma_sv.lower()]

        if not ket_qua:
            print(f"🔍 Không tìm thấy '{tu_khoa}'")
        else:
            print(f"\n🔍 Tìm thấy {len(ket_qua)} kết quả:")
            for sv in ket_qua:
                print(f"  {sv}")

    def xoa_sv(self):
        ma = input("Nhập mã SV cần xóa: ").strip()
        for i, sv in enumerate(self.danh_sach):
            if sv.ma_sv == ma:
                xn = input(f"Xóa {sv.ten} ({sv.ma_sv})? (c/k): ")
                if xn.lower() == "c":
                    self.danh_sach.pop(i)
                    self.luu_file()
                    print("🗑️ Đã xóa!")
                return
        print(f"🔍 Không tìm thấy mã '{ma}'")

    def thong_ke(self):
        if not self.danh_sach:
            print("📭 Chưa có dữ liệu!")
            return

        diem_tb_list = [sv.diem_tb() for sv in self.danh_sach]
        gioi = sum(1 for sv in self.danh_sach if sv.xep_loai() == "Giỏi")
        kha = sum(1 for sv in self.danh_sach if sv.xep_loai() == "Khá")
        tb = sum(1 for sv in self.danh_sach if sv.xep_loai() == "TB")
        yeu = sum(1 for sv in self.danh_sach if sv.xep_loai() == "Yếu")

        sv_gioi_nhat = max(self.danh_sach, key=lambda sv: sv.diem_tb())

        print(f"\n📊 THỐNG KÊ")
        print(f"  Tổng SV: {len(self.danh_sach)}")
        print(f"  Điểm TB lớp: {sum(diem_tb_list) / len(diem_tb_list):.1f}")
        print(f"  SV giỏi nhất: {sv_gioi_nhat.ten} (TB: {sv_gioi_nhat.diem_tb():.1f})")
        print(f"\n  Phân loại:")
        print(f"    Giỏi: {gioi} | Khá: {kha} | TB: {tb} | Yếu: {yeu}")

    def chay(self):
        print("=" * 40)
        print("   🎓 QUẢN LÝ SINH VIÊN")
        print("=" * 40)

        while True:
            print("\n1. ➕ Thêm sinh viên")
            print("2. 📋 Xem danh sách")
            print("3. 🔍 Tìm kiếm")
            print("4. 🗑️  Xóa sinh viên")
            print("5. 📊 Thống kê")
            print("0. 🚪 Thoát")

            chon = input("\nChọn: ")

            if chon == "1":
                self.them_sv()
            elif chon == "2":
                self.hien_thi()
            elif chon == "3":
                self.tim_kiem()
            elif chon == "4":
                self.xoa_sv()
            elif chon == "5":
                self.thong_ke()
            elif chon == "0":
                print("Tạm biệt! 👋")
                break
            else:
                print("⚠️ Lựa chọn không hợp lệ!")


# Chạy chương trình
QuanLySinhVien().chay()
```

---

## Gợi Ý Cải Tiến (Bài Tập Về Nhà)

### Mức 1
- Thêm chức năng sửa thông tin sinh viên
- Sắp xếp danh sách theo điểm TB hoặc tên

### Mức 2
- Thêm nhiều môn học (không cố định 3 môn)
- Xuất báo cáo ra file text đẹp

### Mức 3
- Tách code thành nhiều file (models/, utils/)
- Thêm chức năng import/export CSV

---

## Tóm tắt Giai đoạn 2
- **OOP**: Class, Object, kế thừa, đa hình, đóng gói
- **Module**: Import, tạo module riêng, pip, venv
- **JSON**: Lưu trữ dữ liệu có cấu trúc
- **Giai đoạn 3**: Làm việc với dữ liệu - Database, API, xử lý dữ liệu nâng cao
