# Buổi 8: OOP Nâng Cao - Kế Thừa & Đa Hình

## Mục tiêu buổi học
- Hiểu kế thừa (inheritance): class con kế thừa từ class cha
- Hiểu đa hình (polymorphism): cùng phương thức, hành vi khác nhau
- Biết cách đóng gói (encapsulation) dữ liệu

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-30 phút | Kế thừa |
| 30-50 phút | Đa hình |
| 50-60 phút | Đóng gói |
| 60-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Phần 1: Kế Thừa (25 phút)

### Kế thừa là gì?
Giống như con cái thừa hưởng đặc điểm từ cha mẹ. Class con kế thừa thuộc tính và phương thức từ class cha, đồng thời có thể thêm hoặc thay đổi.

```python
# Class cha
class DongVat:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def keu(self):
        print("...")

    def __str__(self):
        return f"{self.ten} ({self.tuoi} tuổi)"

# Class con - kế thừa từ DongVat
class Cho(DongVat):
    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi)  # Gọi __init__ của class cha
        self.giong = giong           # Thuộc tính riêng

    def keu(self):  # Ghi đè (override) phương thức cha
        print(f"{self.ten}: Gâu gâu! 🐕")

class Meo(DongVat):
    def keu(self):
        print(f"{self.ten}: Meo meo! 🐱")

# Sử dụng
cho = Cho("Buddy", 3, "Corgi")
meo = Meo("Mimi", 2)

cho.keu()   # Buddy: Gâu gâu! 🐕
meo.keu()   # Mimi: Meo meo! 🐱
print(cho)  # Buddy (3 tuổi) - kế thừa __str__ từ cha
```

### super() - Gọi phương thức của class cha

```python
class NhanVien:
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong

    def hien_thi(self):
        print(f"Tên: {self.ten}, Lương: {self.luong:,.0f}đ")

class QuanLy(NhanVien):
    def __init__(self, ten, luong, phong_ban):
        super().__init__(ten, luong)  # Gọi __init__ cha
        self.phong_ban = phong_ban

    def hien_thi(self):
        super().hien_thi()  # Gọi hien_thi() cha
        print(f"Phòng ban: {self.phong_ban}")  # Thêm thông tin

nv = NhanVien("Minh", 10000000)
ql = QuanLy("Lan", 20000000, "IT")

nv.hien_thi()
print()
ql.hien_thi()
```

---

## Phần 2: Đa Hình (20 phút)

### Đa hình là gì?
Cùng một phương thức nhưng mỗi class thực hiện khác nhau. Giống như "kêu" - chó kêu gâu gâu, mèo kêu meo meo.

```python
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

# Đa hình: cùng gọi tinh_dien_tich() nhưng kết quả khác nhau
cac_hinh = [
    HinhTron(5),
    HinhChuNhat(4, 6),
    HinhVuong(3)
]

for hinh in cac_hinh:
    print(f"{hinh.mo_ta()}: S = {hinh.tinh_dien_tich():.2f}")
```

---

## Phần 3: Đóng Gói (10 phút)

### Đóng gói là gì?
Bảo vệ dữ liệu bên trong object, không cho bên ngoài truy cập trực tiếp. Dùng dấu `_` hoặc `__` trước tên thuộc tính.

```python
class TaiKhoan:
    def __init__(self, ten, so_du):
        self.ten = ten
        self.__so_du = so_du  # __ = private, không truy cập trực tiếp từ ngoài

    def xem_so_du(self):
        """Cách đúng để xem số dư"""
        return self.__so_du

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien

    def rut_tien(self, so_tien):
        if 0 < so_tien <= self.__so_du:
            self.__so_du -= so_tien
            return True
        return False

tk = TaiKhoan("Minh", 1000000)
# print(tk.__so_du)  # ❌ Lỗi! Không truy cập được
print(tk.xem_so_du())  # ✅ Dùng phương thức
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (20 phút)

### Bài thực hành: Hệ thống nhân viên

```python
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

# Sử dụng
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
```

---

## Bài Tập Về Nhà

### Bài 1: Hệ thống phương tiện
Tạo class cha `PhuongTien` và các class con: `XeMay`, `OTo`, `XeDap`
- Mỗi loại có cách tính phí gửi xe khác nhau

### Bài 2: Game nhân vật đơn giản
Tạo class `NhanVat` (cha) và các class con: `Chien Binh`, `Phap Su`, `Cung Thu`
- Mỗi loại có cách tấn công và phòng thủ khác nhau

---

## Tóm tắt buổi học
- **Kế thừa**: Class con thừa hưởng từ class cha, dùng `super()`
- **Đa hình**: Cùng phương thức, hành vi khác nhau tùy class
- **Đóng gói**: Dùng `__` để bảo vệ dữ liệu private
- **Buổi sau**: Module & Package - tổ chức code thành nhiều file
