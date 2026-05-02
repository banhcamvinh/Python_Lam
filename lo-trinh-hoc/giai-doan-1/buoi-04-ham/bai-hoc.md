# Buổi 4: Hàm (Function)

## Mục tiêu buổi học
- Hiểu tại sao cần dùng hàm và lợi ích của việc chia code thành hàm
- Biết cách định nghĩa hàm, truyền tham số, trả về giá trị
- Hiểu scope (phạm vi) của biến trong và ngoài hàm
- Viết được chương trình có cấu trúc rõ ràng với hàm

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-25 phút | Hàm cơ bản: định nghĩa, gọi hàm |
| 25-45 phút | Tham số và giá trị trả về |
| 45-60 phút | Scope biến, giá trị mặc định, *args |
| 60-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập tự làm + giao bài về nhà |

---

## Phần 1: Hàm Cơ Bản (20 phút)

### Tại sao cần hàm?
Tưởng tượng bạn viết code tính diện tích hình chữ nhật ở 5 chỗ khác nhau. Nếu cần sửa công thức, phải sửa 5 chỗ! Hàm giúp viết một lần, dùng nhiều lần.

```python
# KHÔNG dùng hàm - lặp code nhiều lần 😫
print(f"Diện tích phòng khách: {5 * 4}")
print(f"Diện tích phòng ngủ: {3 * 4}")
print(f"Diện tích bếp: {3 * 2.5}")

# CÓ dùng hàm - gọn gàng, dễ sửa 😊
def tinh_dien_tich(dai, rong):
    return dai * rong

print(f"Diện tích phòng khách: {tinh_dien_tich(5, 4)}")
print(f"Diện tích phòng ngủ: {tinh_dien_tich(3, 4)}")
print(f"Diện tích bếp: {tinh_dien_tich(3, 2.5)}")
```

### Cú pháp định nghĩa hàm

```python
# Hàm đơn giản - không có tham số, không trả về
def chao():
    print("Xin chào các bạn!")
    print("Chào mừng đến với buổi học Python")

# Gọi hàm
chao()
chao()  # Gọi bao nhiêu lần cũng được
```

```python
# Hàm có tham số
def chao_ten(ten):
    print(f"Xin chào {ten}! 👋")

chao_ten("Minh")   # Xin chào Minh! 👋
chao_ten("Lan")    # Xin chào Lan! 👋
```

---

## Phần 2: Tham Số và Giá Trị Trả Về (20 phút)

### Tham số (parameter)

```python
# Hàm với nhiều tham số
def gioi_thieu(ten, tuoi, lop):
    print(f"Tôi là {ten}, {tuoi} tuổi, lớp {lop}")

gioi_thieu("Minh", 18, "CNTT01")
gioi_thieu("Lan", 19, "CNTT02")
```

### Giá trị trả về (return)

```python
# Hàm trả về kết quả
def tinh_dien_tich_tron(ban_kinh):
    dien_tich = 3.14159 * ban_kinh ** 2
    return dien_tich

# Lưu kết quả vào biến
dt = tinh_dien_tich_tron(5)
print(f"Diện tích hình tròn: {dt:.2f}")

# Hoặc dùng trực tiếp
print(f"Diện tích: {tinh_dien_tich_tron(3):.2f}")
```

```python
# Hàm trả về nhiều giá trị
def tinh_toan(a, b):
    tong = a + b
    hieu = a - b
    tich = a * b
    return tong, hieu, tich  # Trả về tuple

# Nhận nhiều giá trị
t, h, ti = tinh_toan(10, 3)
print(f"Tổng: {t}, Hiệu: {h}, Tích: {ti}")
```

### Ví dụ thực tế: Xếp loại học lực

```python
def xep_loai(diem):
    """Xếp loại học lực dựa trên điểm trung bình"""
    if diem >= 9.0:
        return "Xuất sắc"
    elif diem >= 8.0:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

# Sử dụng
diem_minh = 8.5
diem_lan = 6.0
print(f"Minh: {diem_minh} -> {xep_loai(diem_minh)}")
print(f"Lan: {diem_lan} -> {xep_loai(diem_lan)}")
```

---

## Phần 3: Scope, Giá Trị Mặc Định, *args (15 phút)

### Scope - Phạm vi biến

```python
x = 10  # Biến toàn cục (global)

def ham_vi_du():
    y = 5  # Biến cục bộ (local) - chỉ tồn tại trong hàm
    print(f"Trong hàm: x = {x}, y = {y}")

ham_vi_du()
print(f"Ngoài hàm: x = {x}")
# print(y)  # ❌ Lỗi! y không tồn tại ngoài hàm
```

```python
# Cẩn thận: biến cục bộ "che" biến toàn cục
ten = "Minh"  # Biến toàn cục

def thay_doi():
    ten = "Lan"  # Tạo biến CỤC BỘ mới, KHÔNG sửa biến toàn cục
    print(f"Trong hàm: {ten}")  # Lan

thay_doi()
print(f"Ngoài hàm: {ten}")  # Vẫn là Minh
```

### Giá trị mặc định cho tham số

```python
# Tham số có giá trị mặc định
def chao(ten, loi_chao="Xin chào"):
    print(f"{loi_chao}, {ten}!")

chao("Minh")                    # Xin chào, Minh!
chao("Minh", "Hello")           # Hello, Minh!
chao("Minh", "Chào buổi sáng")  # Chào buổi sáng, Minh!
```

```python
# Ví dụ thực tế: Hàm tính giá sau giảm
def tinh_gia(gia_goc, giam_phan_tram=0):
    gia_giam = gia_goc * giam_phan_tram / 100
    return gia_goc - gia_giam

print(f"Không giảm: {tinh_gia(100000):,.0f}đ")
print(f"Giảm 10%: {tinh_gia(100000, 10):,.0f}đ")
print(f"Giảm 25%: {tinh_gia(100000, 25):,.0f}đ")
```

### *args - Nhận số lượng tham số không cố định

```python
# Hàm nhận bao nhiêu tham số cũng được
def tinh_trung_binh(*diem):
    if len(diem) == 0:
        return 0
    return sum(diem) / len(diem)

print(tinh_trung_binh(8, 7, 9))        # 8.0
print(tinh_trung_binh(8, 7, 9, 6, 10)) # 8.0
print(tinh_trung_binh(10, 10))          # 10.0
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (20 phút)

### Bài thực hành 1: Máy tính bỏ túi

```python
# === MÁY TÍNH BỎ TÚI ===

def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Lỗi: không thể chia cho 0!"
    return a / b

def hien_menu():
    print("\n=== MÁY TÍNH ===")
    print("1. Cộng (+)")
    print("2. Trừ (-)")
    print("3. Nhân (×)")
    print("4. Chia (÷)")
    print("0. Thoát")

# Chương trình chính
while True:
    hien_menu()
    chon = input("Chọn phép tính: ")

    if chon == "0":
        print("Tạm biệt! 👋")
        break

    if chon not in ["1", "2", "3", "4"]:
        print("⚠️ Lựa chọn không hợp lệ!")
        continue

    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))

    if chon == "1":
        print(f"Kết quả: {a} + {b} = {cong(a, b)}")
    elif chon == "2":
        print(f"Kết quả: {a} - {b} = {tru(a, b)}")
    elif chon == "3":
        print(f"Kết quả: {a} × {b} = {nhan(a, b)}")
    elif chon == "4":
        print(f"Kết quả: {a} ÷ {b} = {chia(a, b)}")
```

### Bài thực hành 2: Hệ thống kiểm tra mật khẩu

```python
# === KIỂM TRA MẬT KHẨU ===

def kiem_tra_do_dai(mat_khau, do_dai_toi_thieu=8):
    """Kiểm tra mật khẩu có đủ dài không"""
    return len(mat_khau) >= do_dai_toi_thieu

def co_chu_hoa(mat_khau):
    """Kiểm tra có ít nhất 1 chữ hoa"""
    for ky_tu in mat_khau:
        if ky_tu.isupper():
            return True
    return False

def co_chu_thuong(mat_khau):
    """Kiểm tra có ít nhất 1 chữ thường"""
    for ky_tu in mat_khau:
        if ky_tu.islower():
            return True
    return False

def co_so(mat_khau):
    """Kiểm tra có ít nhất 1 chữ số"""
    for ky_tu in mat_khau:
        if ky_tu.isdigit():
            return True
    return False

def danh_gia_mat_khau(mat_khau):
    """Đánh giá độ mạnh của mật khẩu, trả về (điểm, nhận xét)"""
    diem = 0
    nhan_xet = []

    if kiem_tra_do_dai(mat_khau):
        diem += 1
    else:
        nhan_xet.append("❌ Cần ít nhất 8 ký tự")

    if co_chu_hoa(mat_khau):
        diem += 1
    else:
        nhan_xet.append("❌ Cần ít nhất 1 chữ hoa")

    if co_chu_thuong(mat_khau):
        diem += 1
    else:
        nhan_xet.append("❌ Cần ít nhất 1 chữ thường")

    if co_so(mat_khau):
        diem += 1
    else:
        nhan_xet.append("❌ Cần ít nhất 1 chữ số")

    return diem, nhan_xet

# Chương trình chính
mk = input("Nhập mật khẩu: ")
diem, nhan_xet = danh_gia_mat_khau(mk)

print(f"\nĐộ mạnh: {diem}/4 {'🟢' * diem}{'⚪' * (4 - diem)}")

if diem == 4:
    print("✅ Mật khẩu mạnh!")
else:
    print("Cần cải thiện:")
    for nx in nhan_xet:
        print(f"  {nx}")
```

---

## Phần 5: Bài Tập Tự Làm Tại Lớp (10 phút)

### Bài tập: Hàm xử lý danh sách điểm
Viết các hàm:
1. `nhap_diem()` - nhập n điểm, trả về list điểm
2. `tinh_trung_binh(diem)` - tính điểm trung bình
3. `tim_max_min(diem)` - trả về (điểm cao nhất, điểm thấp nhất)
4. `dem_dat_khong_dat(diem)` - trả về (số đạt >= 5, số không đạt)

> 💡 Gợi ý: Mỗi hàm làm 1 việc cụ thể, hàm chính gọi các hàm con

---

## Bài Tập Về Nhà

### Bài 1: Hàm xử lý chuỗi
Viết các hàm:
- `dem_tu(cau)` - đếm số từ trong câu
- `dao_nguoc_tu(cau)` - đảo ngược thứ tự các từ ("Tôi yêu Python" → "Python yêu Tôi")
- `viet_hoa_dau(cau)` - viết hoa chữ cái đầu mỗi từ

### Bài 2: Hàm toán học
Viết các hàm:
- `la_so_nguyen_to(n)` - kiểm tra số nguyên tố, trả về True/False
- `uoc_chung_lon_nhat(a, b)` - tìm ƯCLN
- `boi_chung_nho_nhat(a, b)` - tìm BCNN (dùng ƯCLN)

### Bài 3 (Nâng cao): Quản lý sinh viên bằng hàm
Viết chương trình quản lý sinh viên với các hàm:
- `them_sinh_vien(danh_sach)` - thêm SV mới
- `hien_thi(danh_sach)` - hiển thị danh sách
- `tim_kiem(danh_sach, ten)` - tìm SV theo tên
- `xep_loai(diem)` - xếp loại học lực
- Dùng menu while True để chạy liên tục

---

## Tóm tắt buổi học
- **Hàm**: Khối code có tên, viết 1 lần dùng nhiều lần
- **Tham số**: Dữ liệu truyền vào hàm khi gọi
- **return**: Trả kết quả về cho nơi gọi hàm
- **Scope**: Biến trong hàm chỉ sống trong hàm
- **Giá trị mặc định**: Tham số có sẵn giá trị nếu không truyền
- **Buổi sau**: Xử lý file & ngoại lệ - đọc/ghi file, xử lý lỗi
