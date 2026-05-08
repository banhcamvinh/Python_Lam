# Buổi 5: Xử Lý File & Ngoại Lệ

## Mục tiêu buổi học
- Biết cách đọc và ghi file văn bản trong Python
- Hiểu cơ chế try/except để xử lý lỗi
- Kết hợp file + xử lý lỗi để viết chương trình ổn định

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-25 phút | Đọc file |
| 25-40 phút | Ghi file |
| 40-55 phút | Xử lý ngoại lệ (try/except) |
| 55-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập tự làm + giao bài về nhà |

---

## Phần 1: Đọc File (20 phút)

### Tại sao cần đọc/ghi file?
Khi chương trình tắt, mọi dữ liệu trong biến đều mất. File giúp lưu dữ liệu lâu dài, giống như ghi vào sổ tay vậy.

### Mở và đọc file

```python
# Cách 1: Dùng with (khuyến khích - tự đóng file)
with open("du_lieu.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()  # Đọc toàn bộ file
    print(noi_dung)
```

```python
# Cách 2: Đọc từng dòng
with open("du_lieu.txt", "r", encoding="utf-8") as f:
    for dong in f:
        dong = dong.strip()  # Xóa ký tự xuống dòng \n
        print(dong)
```

```python
# Cách 3: Đọc tất cả dòng vào list
with open("du_lieu.txt", "r", encoding="utf-8") as f:
    cac_dong = f.readlines()
    print(f"File có {len(cac_dong)} dòng")
    for dong in cac_dong:
        print(dong.strip())
```

### Các chế độ mở file

```python
# "r"  - Đọc (read) - mặc định, lỗi nếu file không tồn tại
# "w"  - Ghi (write) - tạo mới hoặc GHI ĐÈ file cũ
# "a"  - Nối thêm (append) - thêm vào cuối file
# "r+" - Đọc và ghi
```

---

## Phần 2: Ghi File (15 phút)

### Ghi file mới

```python
# Ghi file - tạo mới hoặc ghi đè
with open("ket_qua.txt", "w", encoding="utf-8") as f:
    f.write("Kết quả học tập\n")
    f.write("================\n")
    f.write("Toán: 8\n")
    f.write("Lý: 7\n")
    f.write("Hóa: 9\n")

print("Đã ghi file ket_qua.txt ✅")
```

### Nối thêm vào file

```python
# Append - thêm vào cuối, không xóa nội dung cũ
with open("nhat_ky.txt", "a", encoding="utf-8") as f:
    f.write("Hôm nay học Python buổi 5\n")
    f.write("Đã hiểu cách đọc/ghi file\n")

print("Đã thêm vào nhat_ky.txt ✅")
```

### Ví dụ: Lưu danh sách sinh viên

```python
# Ghi danh sách ra file
sinh_vien = [
    {"ten": "Minh", "diem": 8.5},
    {"ten": "Lan", "diem": 7.0},
    {"ten": "Hùng", "diem": 9.0}
]

with open("sinh_vien.txt", "w", encoding="utf-8") as f:
    for sv in sinh_vien:
        f.write(f"{sv['ten']},{sv['diem']}\n")

# Đọc lại từ file
print("Đọc lại từ file:")
with open("sinh_vien.txt", "r", encoding="utf-8") as f:
    for dong in f:
        ten, diem = dong.strip().split(",")
        print(f"  {ten}: {float(diem):.1f}")
```

---

## Phần 3: Xử Lý Ngoại Lệ - try/except (15 phút)

### Tại sao cần xử lý lỗi?
Chương trình có thể gặp lỗi bất ngờ: file không tồn tại, người dùng nhập chữ thay vì số... Nếu không xử lý, chương trình sẽ crash.

### Cú pháp try/except

```python
# Không có try/except - chương trình crash
# so = int(input("Nhập số: "))  # Nhập "abc" -> crash!

# Có try/except - xử lý lỗi nhẹ nhàng
try:
    so = int(input("Nhập số: "))
    print(f"Bạn nhập: {so}")
except ValueError:
    print("⚠️ Bạn phải nhập số!")
```

### Các loại lỗi thường gặp

```python
# 1. ValueError - giá trị không hợp lệ
try:
    tuoi = int("abc")
except ValueError:
    print("Không thể chuyển 'abc' thành số")

# 2. FileNotFoundError - file không tồn tại
try:
    with open("khong_co.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File không tồn tại!")

# 3. ZeroDivisionError - chia cho 0
try:
    ket_qua = 10 / 0
except ZeroDivisionError:
    print("Không thể chia cho 0!")

# 4. Bắt nhiều loại lỗi
try:
    so = int(input("Nhập số: "))
    ket_qua = 100 / so
    print(f"100 / {so} = {ket_qua}")
except ValueError:
    print("⚠️ Phải nhập số!")
except ZeroDivisionError:
    print("⚠️ Không chia cho 0!")
```

### try/except/else/finally

```python
try:
    f = open("du_lieu.txt", "r", encoding="utf-8")
    noi_dung = f.read()
except FileNotFoundError:
    print("❌ File không tồn tại")
else:
    # Chạy khi KHÔNG có lỗi
    print(f"✅ Đọc thành công! ({len(noi_dung)} ký tự)")
finally:
    # LUÔN chạy, dù có lỗi hay không
    print("Hoàn tất xử lý file")
```

### Hàm nhập số an toàn

```python
def nhap_so(thong_bao="Nhập số: "):
    """Hỏi cho đến khi người dùng nhập đúng số"""
    while True:
        try:
            return float(input(thong_bao))
        except ValueError:
            print("⚠️ Vui lòng nhập số!")

# Sử dụng
tuoi = nhap_so("Nhập tuổi: ")
print(f"Tuổi của bạn: {int(tuoi)}")
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (25 phút)

### Bài thực hành 1: Sổ ghi chú

```python
# === SỔ GHI CHÚ ===
import os

FILE_GHI_CHU = "ghi_chu.txt"

def xem_ghi_chu():
    """Đọc và hiển thị tất cả ghi chú"""
    if not os.path.exists(FILE_GHI_CHU):
        print("📝 Chưa có ghi chú nào!")
        return

    with open(FILE_GHI_CHU, "r", encoding="utf-8") as f:
        cac_dong = f.readlines()

    if len(cac_dong) == 0:
        print("📝 Chưa có ghi chú nào!")
        return

    print(f"\n📋 Có {len(cac_dong)} ghi chú:")
    for i, dong in enumerate(cac_dong):
        print(f"  {i + 1}. {dong.strip()}")

def them_ghi_chu():
    """Thêm ghi chú mới"""
    noi_dung = input("Nhập ghi chú: ")
    with open(FILE_GHI_CHU, "a", encoding="utf-8") as f:
        f.write(noi_dung + "\n")
    print("✅ Đã thêm ghi chú!")

def xoa_ghi_chu():
    """Xóa một ghi chú theo số thứ tự"""
    xem_ghi_chu()

    try:
        with open(FILE_GHI_CHU, "r", encoding="utf-8") as f:
            cac_dong = f.readlines()
    except FileNotFoundError:
        return

    if len(cac_dong) == 0:
        return

    try:
        stt = int(input("Nhập số thứ tự cần xóa: "))
        if 1 <= stt <= len(cac_dong):
            da_xoa = cac_dong.pop(stt - 1)
            with open(FILE_GHI_CHU, "w", encoding="utf-8") as f:
                f.writelines(cac_dong)
            print(f"🗑️ Đã xóa: {da_xoa.strip()}")
        else:
            print("⚠️ Số thứ tự không hợp lệ!")
    except ValueError:
        print("⚠️ Vui lòng nhập số!")

# Chương trình chính
while True:
    print("\n=== SỔ GHI CHÚ ===")
    print("1. Xem ghi chú")
    print("2. Thêm ghi chú")
    print("3. Xóa ghi chú")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        xem_ghi_chu()
    elif chon == "2":
        them_ghi_chu()
    elif chon == "3":
        xoa_ghi_chu()
    elif chon == "0":
        print("Tạm biệt! 👋")
        break
    else:
        print("⚠️ Lựa chọn không hợp lệ!")
```

---

## Phần 5: Bài Tập Tự Làm Tại Lớp (10 phút)

### Bài tập: Đếm từ trong file
Yêu cầu:
1. Tạo file `bai_van.txt` với vài đoạn văn
2. Đọc file, đếm: số dòng, số từ, số ký tự
3. Xử lý lỗi nếu file không tồn tại

> 💡 Gợi ý: Dùng `split()` để đếm từ, `len()` để đếm ký tự

---

## Bài Tập Về Nhà

### Bài 1: Nhật ký cá nhân
Viết chương trình nhật ký:
- Thêm entry mới (tự động ghi ngày giờ)
- Xem tất cả entries
- Tìm kiếm theo từ khóa
- Gợi ý: Dùng `from datetime import datetime` để lấy ngày giờ

### Bài 2: Quản lý điểm từ file
Tạo file `diem.csv` với nội dung: `Tên,Toán,Lý,Hóa` (mỗi dòng 1 sinh viên)
- Đọc file, tính điểm TB mỗi sinh viên
- Xếp loại và ghi kết quả ra file `ket_qua.csv`

### Bài 3 (Nâng cao): Chương trình quiz
- Lưu câu hỏi trong file `cau_hoi.txt` (mỗi dòng: câu hỏi|đáp án)
- Đọc file, hỏi ngẫu nhiên, chấm điểm
- Lưu kết quả cao nhất vào file `ky_luc.txt`

---

## Tóm tắt buổi học
- **Đọc file**: `open("file.txt", "r")`, dùng `with` để tự đóng
- **Ghi file**: `"w"` ghi đè, `"a"` nối thêm
- **try/except**: Bắt lỗi để chương trình không crash
- **Lỗi hay gặp**: ValueError, FileNotFoundError, ZeroDivisionError
- **Buổi sau**: Git cơ bản - Quản lý mã nguồn với Git và GitHub!
