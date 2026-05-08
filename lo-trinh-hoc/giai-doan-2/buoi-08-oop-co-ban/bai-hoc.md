# Buổi 8: OOP Cơ Bản - Class & Object

## Mục tiêu buổi học
- Hiểu khái niệm lập trình hướng đối tượng (OOP) và tại sao cần dùng
- Biết cách tạo class, tạo object, viết __init__ và phương thức
- Phân biệt thuộc tính và phương thức

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Giới thiệu Giai đoạn 2 |
| 5-25 phút | Khái niệm OOP, Class và Object |
| 25-45 phút | __init__, thuộc tính, phương thức |
| 45-60 phút | Ví dụ thực tế |
| 60-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Phần 1: Khái Niệm OOP (20 phút)

### Tại sao cần OOP?
Trước giờ mình dùng biến rời rạc và hàm riêng lẻ. Khi chương trình lớn lên, code trở nên lộn xộn. OOP giúp gom dữ liệu và hành vi liên quan vào một "gói" gọn gàng.

```python
# KHÔNG dùng OOP - dữ liệu rời rạc
ten1 = "Minh"
tuoi1 = 18
diem1 = 8.5

ten2 = "Lan"
tuoi2 = 19
diem2 = 7.0

# Nếu có 100 sinh viên thì sao? 😱

# CÓ dùng OOP - gọn gàng
class SinhVien:
    def __init__(self, ten, tuoi, diem):
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem

sv1 = SinhVien("Minh", 18, 8.5)
sv2 = SinhVien("Lan", 19, 7.0)
```

### Class và Object
- **Class** (lớp): Bản thiết kế, khuôn mẫu. Ví dụ: bản vẽ ngôi nhà
- **Object** (đối tượng): Sản phẩm tạo ra từ bản thiết kế. Ví dụ: ngôi nhà thật

```python
# Class = bản thiết kế
class SinhVien:
    pass

# Object = tạo ra từ bản thiết kế
sv1 = SinhVien()  # Object 1
sv2 = SinhVien()  # Object 2 (khác sv1)
```

---

## Phần 2: __init__, Thuộc Tính, Phương Thức (20 phút)

### __init__ - Hàm khởi tạo

```python
class SinhVien:
    def __init__(self, ten, tuoi, diem):
        # self = chính object đang được tạo
        self.ten = ten      # Thuộc tính
        self.tuoi = tuoi    # Thuộc tính
        self.diem = diem    # Thuộc tính

# Tạo object - __init__ tự động chạy
sv = SinhVien("Minh", 18, 8.5)
print(sv.ten)    # Minh
print(sv.tuoi)   # 18
print(sv.diem)   # 8.5
```

### Phương thức (method) - Hành vi của object

```python
class SinhVien:
    def __init__(self, ten, tuoi, diem):
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem

    def gioi_thieu(self):
        """Phương thức - hành vi của sinh viên"""
        print(f"Xin chào! Tôi là {self.ten}, {self.tuoi} tuổi")

    def xep_loai(self):
        """Trả về xếp loại dựa trên điểm"""
        if self.diem >= 8.0:
            return "Giỏi"
        elif self.diem >= 6.5:
            return "Khá"
        elif self.diem >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"

    def hien_thi(self):
        """Hiển thị thông tin đầy đủ"""
        print(f"{self.ten} | Tuổi: {self.tuoi} | Điểm: {self.diem} | {self.xep_loai()}")

# Sử dụng
sv1 = SinhVien("Minh", 18, 8.5)
sv2 = SinhVien("Lan", 19, 6.0)

sv1.gioi_thieu()
sv2.gioi_thieu()

print()
sv1.hien_thi()
sv2.hien_thi()
```

### __str__ - Hiển thị đẹp khi print

```python
class SinhVien:
    def __init__(self, ten, tuoi, diem):
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem

    def __str__(self):
        return f"SinhVien({self.ten}, {self.tuoi} tuổi, điểm {self.diem})"

sv = SinhVien("Minh", 18, 8.5)
print(sv)  # SinhVien(Minh, 18 tuổi, điểm 8.5)
```

---

## Phần 3: Ví Dụ Thực Tế (15 phút)

### Ví dụ: Tài khoản ngân hàng

```python
class TaiKhoan:
    def __init__(self, chu_tai_khoan, so_du=0):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.so_du += so_tien
            print(f"✅ Nạp {so_tien:,.0f}đ. Số dư: {self.so_du:,.0f}đ")
        else:
            print("⚠️ Số tiền phải lớn hơn 0!")

    def rut_tien(self, so_tien):
        if so_tien > self.so_du:
            print(f"❌ Không đủ tiền! Số dư: {self.so_du:,.0f}đ")
        elif so_tien <= 0:
            print("⚠️ Số tiền phải lớn hơn 0!")
        else:
            self.so_du -= so_tien
            print(f"✅ Rút {so_tien:,.0f}đ. Số dư: {self.so_du:,.0f}đ")

    def xem_so_du(self):
        print(f"💰 {self.chu_tai_khoan}: {self.so_du:,.0f}đ")

# Sử dụng
tk = TaiKhoan("Minh", 1000000)
tk.xem_so_du()
tk.nap_tien(500000)
tk.rut_tien(200000)
tk.rut_tien(2000000)  # Không đủ tiền
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (20 phút)

### Bài thực hành: Quản lý lớp học

```python
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
        if len(self.danh_sach) == 0:
            return 0
        tong = sum(sv.diem for sv in self.danh_sach)
        return tong / len(self.danh_sach)

    def sv_gioi_nhat(self):
        if len(self.danh_sach) == 0:
            return None
        return max(self.danh_sach, key=lambda sv: sv.diem)

# Sử dụng
lop = LopHoc("CNTT01")
lop.them_sv(SinhVien("Minh", "SV001", 8.5))
lop.them_sv(SinhVien("Lan", "SV002", 7.0))
lop.them_sv(SinhVien("Hùng", "SV003", 9.2))
lop.them_sv(SinhVien("Mai", "SV004", 6.0))

lop.hien_thi()
print(f"\nĐiểm TB lớp: {lop.diem_trung_binh():.1f}")
print(f"SV giỏi nhất: {lop.sv_gioi_nhat()}")
```

---

## Bài Tập Về Nhà

### Bài 1: Class Sản phẩm
Tạo class `SanPham` với: tên, giá, số lượng tồn kho
- Phương thức: `ban(so_luong)`, `nhap_them(so_luong)`, `hien_thi()`

### Bài 2: Class Thú cưng
Tạo class `ThuCung` với: tên, loài, tuổi, mức năng lượng
- Phương thức: `cho_an()` (tăng năng lượng), `choi()` (giảm năng lượng), `trang_thai()`

### Bài 3 (Nâng cao): Hệ thống thư viện
Tạo class `Sach` và class `ThuVien`:
- Sách: tên, tác giả, đang_muon (True/False)
- Thư viện: danh sách sách, cho mượn, trả sách, tìm kiếm

---

## Tóm tắt buổi học
- **Class**: Bản thiết kế cho object
- **Object**: Thực thể tạo từ class
- **__init__**: Hàm khởi tạo, chạy khi tạo object
- **self**: Tham chiếu đến chính object hiện tại
- **Thuộc tính**: Dữ liệu của object (self.ten, self.tuoi)
- **Phương thức**: Hành vi của object (def gioi_thieu(self))
- **Buổi sau**: OOP nâng cao - Kế thừa, đa hình
