# Buổi 3: List, Tuple, Dictionary

## Mục tiêu buổi học
- Hiểu và sử dụng được 3 cấu trúc dữ liệu quan trọng nhất: List, Tuple, Dictionary
- Biết khi nào dùng loại nào cho phù hợp
- Thành thạo các thao tác thêm, xóa, sửa, tìm kiếm trên List và Dictionary

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước, giải đáp bài tập về nhà |
| 5-30 phút | List (danh sách) |
| 30-45 phút | Tuple (bộ giá trị) |
| 45-65 phút | Dictionary (từ điển) |
| 65-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập tự làm + giao bài về nhà |

---

## Phần 1: List - Danh Sách (25 phút)

### List là gì?
List giống như một danh sách có thứ tự. Mình có thể thêm, xóa, sửa các phần tử bên trong.

```python
# Tạo list
diem_so = [8, 7, 9, 6, 10]
mon_hoc = ["Toán", "Lý", "Hóa", "Tin"]
hon_hop = ["Minh", 18, 8.5, True]  # List có thể chứa nhiều kiểu

# List rỗng
danh_sach = []
```

### Truy cập phần tử

```python
mon_hoc = ["Toán", "Lý", "Hóa", "Tin", "Anh"]

# Truy cập bằng chỉ số (index), đếm từ 0
print(mon_hoc[0])    # Toán
print(mon_hoc[2])    # Hóa
print(mon_hoc[-1])   # Anh (phần tử cuối)

# Cắt list (slicing) - giống chuỗi
print(mon_hoc[1:3])  # ['Lý', 'Hóa']
print(mon_hoc[:3])   # ['Toán', 'Lý', 'Hóa']

# Độ dài list
print(len(mon_hoc))  # 5
```

### Thêm, xóa, sửa phần tử

```python
# Tạo danh sách sinh viên
sv = ["An", "Bình", "Chi"]

# Thêm vào cuối
sv.append("Dũng")
print(sv)  # ['An', 'Bình', 'Chi', 'Dũng']

# Chèn vào vị trí cụ thể
sv.insert(1, "Anh")
print(sv)  # ['An', 'Anh', 'Bình', 'Chi', 'Dũng']

# Sửa phần tử
sv[0] = "An Khang"
print(sv)  # ['An Khang', 'Anh', 'Bình', 'Chi', 'Dũng']

# Xóa theo giá trị
sv.remove("Bình")
print(sv)  # ['An Khang', 'Anh', 'Chi', 'Dũng']

# Xóa theo vị trí
sv.pop(0)       # Xóa phần tử đầu
print(sv)       # ['Anh', 'Chi', 'Dũng']

sv.pop()        # Không truyền index -> xóa phần tử cuối
print(sv)       # ['Anh', 'Chi']
```

### Các thao tác hữu ích

```python
diem = [8, 6, 9, 7, 10, 6, 8]

# Sắp xếp
diem.sort()
print(diem)  # [6, 6, 7, 8, 8, 9, 10]

diem.sort(reverse=True)
print(diem)  # [10, 9, 8, 8, 7, 6, 6]

# Tìm min, max, tổng
print(f"Điểm cao nhất: {max(diem)}")
print(f"Điểm thấp nhất: {min(diem)}")
print(f"Tổng điểm: {sum(diem)}")
print(f"Điểm TB: {sum(diem) / len(diem):.1f}")

# Kiểm tra phần tử có trong list không
print(10 in diem)   # True
print(5 in diem)    # False

# Đếm số lần xuất hiện
print(diem.count(8))  # 2
```

### Duyệt list

```python
mon_hoc = ["Toán", "Lý", "Hóa", "Tin"]

# Cách 1: Duyệt trực tiếp
for mon in mon_hoc:
    print(f"Môn: {mon}")

# Cách 2: Duyệt với index (dùng enumerate)
for i, mon in enumerate(mon_hoc):
    print(f"{i + 1}. {mon}")
# 1. Toán
# 2. Lý
# 3. Hóa
# 4. Tin
```

---

## Phần 2: Tuple - Bộ Giá Trị (15 phút)

### Tuple là gì?
Tuple giống List nhưng KHÔNG THỂ thay đổi sau khi tạo. Dùng khi dữ liệu cố định, không muốn ai sửa.

```python
# Tạo tuple - dùng ngoặc tròn ()
toa_do = (10, 20)
mau_sac = ("đỏ", "xanh", "vàng")
thong_tin = ("Minh", 18, "CNTT")

# Truy cập giống list
print(toa_do[0])     # 10
print(mau_sac[-1])   # vàng

# KHÔNG THỂ sửa tuple
# toa_do[0] = 99  # ❌ Lỗi! TypeError
```

### Khi nào dùng Tuple?

```python
# 1. Tọa độ (x, y) - không cần thay đổi
vi_tri = (100, 200)

# 2. Ngày tháng năm
ngay_sinh = (15, 8, 2005)

# 3. Trả về nhiều giá trị từ hàm (sẽ học ở buổi 4)
# 4. Dùng làm key cho dictionary (list không làm được)

# Unpacking - tách tuple ra nhiều biến
x, y = toa_do
print(f"x = {x}, y = {y}")

ngay, thang, nam = ngay_sinh
print(f"Ngày sinh: {ngay}/{thang}/{nam}")
```

### So sánh List vs Tuple

```python
# List: thay đổi được, dùng [] 
danh_sach = [1, 2, 3]
danh_sach[0] = 99  # ✅ OK

# Tuple: không thay đổi được, dùng ()
bo = (1, 2, 3)
# bo[0] = 99  # ❌ Lỗi!

# Quy tắc đơn giản:
# - Dữ liệu cần thêm/xóa/sửa -> dùng List
# - Dữ liệu cố định, chỉ đọc -> dùng Tuple
```

---

## Phần 3: Dictionary - Từ Điển (20 phút)

### Dictionary là gì?
Dictionary lưu dữ liệu theo cặp key: value (khóa: giá trị). Giống cuốn từ điển: tra từ (key) để tìm nghĩa (value).

```python
# Tạo dictionary
sinh_vien = {
    "ten": "Nguyễn Văn Minh",
    "tuoi": 18,
    "lop": "CNTT01",
    "diem_tb": 8.5
}

# Dictionary rỗng
du_lieu = {}
```

### Truy cập và thay đổi

```python
sinh_vien = {
    "ten": "Minh",
    "tuoi": 18,
    "lop": "CNTT01"
}

# Truy cập giá trị qua key
print(sinh_vien["ten"])     # Minh
print(sinh_vien["tuoi"])    # 18

# Cách an toàn hơn: dùng get() (không lỗi nếu key không tồn tại)
print(sinh_vien.get("email", "Chưa có"))  # Chưa có

# Thêm / sửa
sinh_vien["email"] = "minh@gmail.com"  # Thêm mới
sinh_vien["tuoi"] = 19                  # Sửa giá trị
print(sinh_vien)

# Xóa
del sinh_vien["lop"]
print(sinh_vien)
```

### Duyệt Dictionary

```python
sinh_vien = {"ten": "Minh", "tuoi": 18, "diem": 8.5}

# Duyệt qua keys
for key in sinh_vien:
    print(f"{key}: {sinh_vien[key]}")

# Duyệt qua cả key và value (cách hay hơn)
for key, value in sinh_vien.items():
    print(f"{key}: {value}")

# Chỉ lấy keys hoặc values
print(list(sinh_vien.keys()))    # ['ten', 'tuoi', 'diem']
print(list(sinh_vien.values()))  # ['Minh', 18, 8.5]
```

### Ví dụ thực tế: Danh bạ điện thoại

```python
# Dictionary lồng trong list - rất phổ biến!
danh_ba = [
    {"ten": "Minh", "sdt": "0901234567"},
    {"ten": "Lan", "sdt": "0912345678"},
    {"ten": "Hùng", "sdt": "0923456789"}
]

# In danh bạ
print("=== DANH BẠ ===")
for i, nguoi in enumerate(danh_ba):
    print(f"{i + 1}. {nguoi['ten']}: {nguoi['sdt']}")

# Tìm kiếm
ten_tim = input("\nNhập tên cần tìm: ")
for nguoi in danh_ba:
    if nguoi["ten"].lower() == ten_tim.lower():
        print(f"📞 {nguoi['ten']}: {nguoi['sdt']}")
        break
else:
    print("Không tìm thấy!")
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (15 phút)

### Bài thực hành 1: Quản lý điểm sinh viên

```python
# === QUẢN LÝ ĐIỂM SINH VIÊN ===

diem_lop = []

# Nhập điểm
so_sv = int(input("Nhập số sinh viên: "))

for i in range(so_sv):
    print(f"\n--- Sinh viên {i + 1} ---")
    ten = input("Họ tên: ")
    diem = float(input("Điểm TB: "))
    diem_lop.append({"ten": ten, "diem": diem})

# Hiển thị kết quả
print("\n" + "=" * 40)
print("   BẢNG ĐIỂM LỚP")
print("=" * 40)

for i, sv in enumerate(diem_lop):
    # Xếp loại
    if sv["diem"] >= 8.0:
        loai = "Giỏi"
    elif sv["diem"] >= 6.5:
        loai = "Khá"
    elif sv["diem"] >= 5.0:
        loai = "TB"
    else:
        loai = "Yếu"
    print(f"{i + 1}. {sv['ten']:<15} | Điểm: {sv['diem']:.1f} | {loai}")

# Thống kê
tat_ca_diem = [sv["diem"] for sv in diem_lop]
print(f"\nĐiểm cao nhất: {max(tat_ca_diem):.1f}")
print(f"Điểm thấp nhất: {min(tat_ca_diem):.1f}")
print(f"Điểm trung bình lớp: {sum(tat_ca_diem) / len(tat_ca_diem):.1f}")
```

### Bài thực hành 2: Đếm tần suất từ

```python
# === ĐẾM TẦN SUẤT TỪ ===

cau = input("Nhập một câu: ")
cac_tu = cau.lower().split()

# Đếm bằng dictionary
tan_suat = {}
for tu in cac_tu:
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

# Hiển thị kết quả
print(f"\nCâu: \"{cau}\"")
print(f"Tổng số từ: {len(cac_tu)}")
print(f"Số từ khác nhau: {len(tan_suat)}")
print("\nTần suất:")
for tu, dem in tan_suat.items():
    thanh = "█" * dem
    print(f"  '{tu}': {dem} lần {thanh}")
```

---

## Phần 5: Bài Tập Tự Làm Tại Lớp (10 phút)

### Bài tập: Giỏ hàng mua sắm
Yêu cầu:
1. Tạo list `gio_hang` rỗng
2. Cho người dùng nhập tên sản phẩm và giá, thêm vào giỏ hàng (dùng dictionary)
3. Nhập "xong" để dừng
4. In ra danh sách sản phẩm, tổng tiền

> 💡 Gợi ý: Mỗi sản phẩm là 1 dictionary `{"ten": ..., "gia": ...}`, thêm vào list bằng `append()`

---

## Bài Tập Về Nhà

### Bài 1: Quản lý todo list
Viết chương trình todo list đơn giản:
- Thêm công việc mới
- Xem danh sách công việc
- Đánh dấu hoàn thành (xóa khỏi list)
- Thoát chương trình
- Dùng while True + menu để chạy liên tục

### Bài 2: Thống kê điểm
Nhập điểm của n sinh viên vào list, sau đó:
- In ra điểm cao nhất, thấp nhất, trung bình
- Đếm số sinh viên giỏi (>=8), khá (>=6.5), TB (>=5), yếu (<5)
- Sắp xếp và in danh sách theo điểm giảm dần

### Bài 3 (Nâng cao): Từ điển Anh-Việt
Tạo dictionary chứa 10 từ Anh-Việt. Viết chương trình:
- Tra từ: nhập từ tiếng Anh, hiện nghĩa tiếng Việt
- Thêm từ mới vào từ điển
- Hiển thị tất cả từ trong từ điển
- Chạy liên tục cho đến khi chọn thoát

---

## Tóm tắt buổi học
- **List**: Danh sách có thứ tự, thay đổi được. Dùng `[]`
- **Tuple**: Giống list nhưng không thay đổi được. Dùng `()`
- **Dictionary**: Lưu theo cặp key:value. Dùng `{}`
- **Khi nào dùng gì**: List cho danh sách, Tuple cho dữ liệu cố định, Dict cho dữ liệu có nhãn
- **Buổi sau**: Hàm (Function) - chia code thành các khối nhỏ, tái sử dụng
