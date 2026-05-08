# Buổi 10: Module & Package

## Mục tiêu buổi học
- Hiểu module là gì, cách import và sử dụng
- Biết cách tạo module riêng để tổ chức code
- Làm quen với pip và virtual environment
- Sử dụng một số thư viện phổ biến

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-25 phút | Module có sẵn của Python |
| 25-40 phút | Tạo module riêng |
| 40-55 phút | pip và virtual environment |
| 55-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Phần 1: Module Có Sẵn (20 phút)

### Module là gì?
Module là file Python chứa code (hàm, class, biến) mà mình có thể dùng lại. Python có sẵn rất nhiều module hữu ích.

### Cách import

```python
# Cách 1: Import cả module
import math
print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0

# Cách 2: Import cụ thể
from math import pi, sqrt
print(pi)               # 3.141592653589793
print(sqrt(16))         # 4.0

# Cách 3: Đặt tên ngắn gọn
import datetime as dt
hom_nay = dt.date.today()
print(hom_nay)
```

### Các module hay dùng

```python
# --- math: Toán học ---
import math
print(f"Pi: {math.pi}")
print(f"Căn bậc 2 của 144: {math.sqrt(144)}")
print(f"Làm tròn lên: {math.ceil(4.2)}")    # 5
print(f"Làm tròn xuống: {math.floor(4.8)}")  # 4

# --- random: Ngẫu nhiên ---
import random
print(f"Số ngẫu nhiên 1-100: {random.randint(1, 100)}")
print(f"Chọn ngẫu nhiên: {random.choice(['Toán', 'Lý', 'Hóa'])}")

ds = [1, 2, 3, 4, 5]
random.shuffle(ds)  # Xáo trộn
print(f"Sau xáo trộn: {ds}")

# --- datetime: Ngày giờ ---
from datetime import datetime, date
bay_gio = datetime.now()
print(f"Bây giờ: {bay_gio.strftime('%d/%m/%Y %H:%M')}")

ngay_sinh = date(2005, 8, 15)
tuoi = (date.today() - ngay_sinh).days // 365
print(f"Tuổi: {tuoi}")

# --- os: Hệ điều hành ---
import os
print(f"Thư mục hiện tại: {os.getcwd()}")
print(f"File tồn tại? {os.path.exists('bai-hoc.md')}")

# --- json: Đọc/ghi JSON ---
import json
du_lieu = {"ten": "Minh", "tuoi": 18, "diem": [8, 7, 9]}
json_text = json.dumps(du_lieu, ensure_ascii=False, indent=2)
print(f"JSON:\n{json_text}")
```

---

## Phần 2: Tạo Module Riêng (15 phút)

### Tạo file module

```python
# File: tien_ich.py (module riêng)

def tinh_bmi(can_nang, chieu_cao):
    """Tính chỉ số BMI"""
    return can_nang / (chieu_cao ** 2)

def xep_loai_bmi(bmi):
    """Xếp loại BMI"""
    if bmi < 18.5:
        return "Thiếu cân"
    elif bmi < 25:
        return "Bình thường"
    elif bmi < 30:
        return "Thừa cân"
    return "Béo phì"

def format_tien(so_tien):
    """Format số tiền đẹp"""
    return f"{so_tien:,.0f}đ"
```

```python
# File: main.py (sử dụng module)
from tien_ich import tinh_bmi, xep_loai_bmi, format_tien

bmi = tinh_bmi(65, 1.70)
print(f"BMI: {bmi:.1f} - {xep_loai_bmi(bmi)}")
print(f"Giá: {format_tien(1500000)}")
```

### Tổ chức project nhiều file

```
my_project/
├── main.py              # File chính
├── models/
│   ├── __init__.py      # Đánh dấu đây là package
│   ├── sinh_vien.py     # Class SinhVien
│   └── lop_hoc.py       # Class LopHoc
└── utils/
    ├── __init__.py
    └── helpers.py        # Các hàm tiện ích
```

---

## Phần 3: pip & Virtual Environment (15 phút)

### pip - Cài đặt thư viện

```bash
# Xem các thư viện đã cài
pip list

# Cài thư viện mới
pip install requests
pip install colorama

# Gỡ thư viện
pip uninstall requests

# Lưu danh sách thư viện
pip freeze > requirements.txt

# Cài từ file requirements.txt
pip install -r requirements.txt
```

### Virtual Environment - Môi trường ảo

```bash
# Tạo môi trường ảo
python -m venv myenv

# Kích hoạt (macOS/Linux)
source myenv/bin/activate

# Kích hoạt (Windows)
myenv\Scripts\activate

# Tắt môi trường ảo
deactivate
```

### Ví dụ: Dùng thư viện colorama

```python
# pip install colorama
from colorama import Fore, Style

print(Fore.RED + "Lỗi: File không tồn tại!" + Style.RESET_ALL)
print(Fore.GREEN + "Thành công!" + Style.RESET_ALL)
print(Fore.YELLOW + "Cảnh báo: Dung lượng thấp" + Style.RESET_ALL)
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (25 phút)

### Bài thực hành: Ứng dụng xổ số mini

```python
import random
from datetime import datetime

def tao_ve_so():
    """Tạo vé số ngẫu nhiên 6 số (1-45)"""
    return sorted(random.sample(range(1, 46), 6))

def kiem_tra_trung(ve_cua_ban, ve_trung):
    """Đếm số trùng khớp"""
    trung = []
    for so in ve_cua_ban:
        if so in ve_trung:
            trung.append(so)
    return trung

def tinh_giai_thuong(so_trung):
    """Tính giải thưởng dựa trên số trùng"""
    giai = {
        6: "JACKPOT - 10,000,000,000đ 🎉🎉🎉",
        5: "Giải nhất - 100,000,000đ 🎉",
        4: "Giải nhì - 10,000,000đ",
        3: "Giải ba - 500,000đ",
        2: "Giải khuyến khích - 50,000đ",
    }
    return giai.get(so_trung, "Không trúng 😢")

# Chương trình chính
print("=" * 40)
print("   🎰 XỔ SỐ PYTHON")
print(f"   {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print("=" * 40)

# Tạo kết quả xổ số
ket_qua = tao_ve_so()

# Người chơi chọn số
print("\nChọn 6 số từ 1 đến 45:")
ve_cua_ban = []
for i in range(6):
    while True:
        try:
            so = int(input(f"  Số thứ {i + 1}: "))
            if 1 <= so <= 45 and so not in ve_cua_ban:
                ve_cua_ban.append(so)
                break
            else:
                print("  ⚠️ Số không hợp lệ hoặc đã chọn!")
        except ValueError:
            print("  ⚠️ Nhập số!")

ve_cua_ban.sort()

# Kết quả
print(f"\n🎱 Kết quả xổ số: {ket_qua}")
print(f"🎫 Vé của bạn:    {ve_cua_ban}")

trung = kiem_tra_trung(ve_cua_ban, ket_qua)
print(f"\n✨ Số trùng: {trung} ({len(trung)} số)")
print(f"🏆 {tinh_giai_thuong(len(trung))}")
```

---

## Bài Tập Về Nhà

### Bài 1: Tạo module tiện ích
Tạo file `my_utils.py` chứa các hàm:
- `la_email_hop_le(email)` - kiểm tra email
- `la_so_dien_thoai(sdt)` - kiểm tra SĐT VN
- `tao_mat_khau(do_dai)` - tạo mật khẩu ngẫu nhiên
Viết file `main.py` import và sử dụng

### Bài 2: Ứng dụng ghi chú với JSON
Dùng module `json` để lưu/đọc ghi chú dạng JSON thay vì text thuần

### Bài 3 (Nâng cao): Tổ chức project
Tách project quản lý sinh viên (buổi 7) thành nhiều file:
- `models/sinh_vien.py`, `models/lop_hoc.py`
- `utils/helpers.py`
- `main.py`

---

## Tóm tắt buổi học
- **Module**: File Python chứa code tái sử dụng
- **import**: Nhiều cách import (import, from...import, as)
- **Module hay dùng**: math, random, datetime, os, json
- **pip**: Cài thư viện bên ngoài
- **venv**: Môi trường ảo, tách biệt thư viện giữa các project
- **Buổi sau**: Mini Project 2 - Quản lý sinh viên (OOP + file)
