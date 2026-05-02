# Buổi 13: Xử Lý Dữ Liệu Nâng Cao

## Mục tiêu buổi học
- Nắm vững List Comprehension - cách viết gọn và Pythonic
- Hiểu và sử dụng lambda, map, filter
- Biết cách sắp xếp dữ liệu phức tạp
- Xử lý dữ liệu thực tế

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-25 phút | List Comprehension |
| 25-40 phút | Lambda, map, filter |
| 40-55 phút | Sắp xếp nâng cao |
| 55-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Phần 1: List Comprehension (20 phút)

### Cú pháp cơ bản

```python
# Cách thường
binh_phuong = []
for i in range(1, 11):
    binh_phuong.append(i ** 2)

# List comprehension - 1 dòng!
binh_phuong = [i ** 2 for i in range(1, 11)]
print(binh_phuong)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Với điều kiện

```python
# Lọc số chẵn
so_chan = [i for i in range(1, 21) if i % 2 == 0]
print(so_chan)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Lọc sinh viên giỏi
sinh_vien = [
    {"ten": "Minh", "diem": 8.5},
    {"ten": "Lan", "diem": 6.0},
    {"ten": "Hùng", "diem": 9.0},
    {"ten": "Mai", "diem": 7.5},
]

sv_gioi = [sv["ten"] for sv in sinh_vien if sv["diem"] >= 8.0]
print(sv_gioi)  # ['Minh', 'Hùng']
```

### Với if/else

```python
# Phân loại chẵn/lẻ
ket_qua = ["chẵn" if i % 2 == 0 else "lẻ" for i in range(1, 6)]
print(ket_qua)  # ['lẻ', 'chẵn', 'lẻ', 'chẵn', 'lẻ']

# Xếp loại điểm
diem = [8, 5, 9, 3, 7]
xep_loai = ["Đạt" if d >= 5 else "Trượt" for d in diem]
print(xep_loai)  # ['Đạt', 'Đạt', 'Đạt', 'Trượt', 'Đạt']
```

### Dictionary Comprehension

```python
# Tạo dict bình phương
bp = {i: i**2 for i in range(1, 6)}
print(bp)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Đảo key-value
mau = {"đỏ": "red", "xanh": "blue", "vàng": "yellow"}
mau_dao = {v: k for k, v in mau.items()}
print(mau_dao)  # {'red': 'đỏ', 'blue': 'xanh', 'yellow': 'vàng'}
```

---

## Phần 2: Lambda, Map, Filter (15 phút)

### Lambda - Hàm ẩn danh

```python
# Hàm thường
def binh_phuong(x):
    return x ** 2

# Lambda - viết gọn trong 1 dòng
binh_phuong = lambda x: x ** 2
print(binh_phuong(5))  # 25

# Lambda hay dùng khi cần hàm ngắn, dùng 1 lần
sap_xep = sorted(["banana", "apple", "cherry"], key=lambda s: len(s))
print(sap_xep)  # ['apple', 'banana', 'cherry']
```

### Map - Áp dụng hàm lên từng phần tử

```python
# Chuyển list string sang int
diem_str = ["8", "7", "9", "6"]
diem_int = list(map(int, diem_str))
print(diem_int)  # [8, 7, 9, 6]

# Tính bình phương
so = [1, 2, 3, 4, 5]
bp = list(map(lambda x: x ** 2, so))
print(bp)  # [1, 4, 9, 16, 25]
```

### Filter - Lọc phần tử

```python
# Lọc số dương
so = [-3, -1, 0, 2, 5, -4, 8]
so_duong = list(filter(lambda x: x > 0, so))
print(so_duong)  # [2, 5, 8]

# Lọc từ dài hơn 3 ký tự
tu = ["hi", "hello", "ok", "python", "go"]
tu_dai = list(filter(lambda t: len(t) > 3, tu))
print(tu_dai)  # ['hello', 'python']
```

---

## Phần 3: Sắp Xếp Nâng Cao (15 phút)

```python
sinh_vien = [
    {"ten": "Minh", "diem": 8.5, "tuoi": 18},
    {"ten": "Lan", "diem": 9.0, "tuoi": 19},
    {"ten": "Hùng", "diem": 7.5, "tuoi": 18},
    {"ten": "Mai", "diem": 9.0, "tuoi": 20},
]

# Sắp xếp theo điểm giảm dần
theo_diem = sorted(sinh_vien, key=lambda sv: sv["diem"], reverse=True)
for sv in theo_diem:
    print(f"  {sv['ten']}: {sv['diem']}")

# Sắp xếp theo nhiều tiêu chí: điểm giảm, rồi tên tăng
theo_nhieu = sorted(sinh_vien, key=lambda sv: (-sv["diem"], sv["ten"]))
print("\nTheo điểm giảm + tên tăng:")
for sv in theo_nhieu:
    print(f"  {sv['ten']}: {sv['diem']}")
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (25 phút)

### Bài thực hành: Phân tích dữ liệu bán hàng

```python
# Dữ liệu bán hàng
don_hang = [
    {"sp": "Laptop", "gia": 15000000, "sl": 2, "thang": 1},
    {"sp": "Chuột", "gia": 200000, "sl": 10, "thang": 1},
    {"sp": "Laptop", "gia": 15000000, "sl": 1, "thang": 2},
    {"sp": "Bàn phím", "gia": 500000, "sl": 5, "thang": 2},
    {"sp": "Chuột", "gia": 200000, "sl": 8, "thang": 2},
    {"sp": "Màn hình", "gia": 5000000, "sl": 3, "thang": 3},
    {"sp": "Laptop", "gia": 15000000, "sl": 3, "thang": 3},
]

# 1. Tổng doanh thu
doanh_thu = [d["gia"] * d["sl"] for d in don_hang]
print(f"💰 Tổng doanh thu: {sum(doanh_thu):,.0f}đ")

# 2. Doanh thu theo tháng
for thang in [1, 2, 3]:
    dt_thang = sum(d["gia"] * d["sl"] for d in don_hang if d["thang"] == thang)
    print(f"  Tháng {thang}: {dt_thang:,.0f}đ")

# 3. Sản phẩm bán chạy nhất
sp_sl = {}
for d in don_hang:
    sp_sl[d["sp"]] = sp_sl.get(d["sp"], 0) + d["sl"]

sp_ban_chay = max(sp_sl.items(), key=lambda x: x[1])
print(f"\n🏆 Bán chạy nhất: {sp_ban_chay[0]} ({sp_ban_chay[1]} cái)")

# 4. Đơn hàng lớn nhất
don_lon_nhat = max(don_hang, key=lambda d: d["gia"] * d["sl"])
print(f"📦 Đơn lớn nhất: {don_lon_nhat['sp']} - "
      f"{don_lon_nhat['gia'] * don_lon_nhat['sl']:,.0f}đ")
```

---

## Bài Tập Về Nhà

### Bài 1: Xử lý danh sách điểm
Cho list điểm, dùng comprehension và lambda để:
- Lọc điểm >= 5, tính TB điểm đạt
- Chuyển điểm số sang điểm chữ (A/B/C/D/F)
- Tìm 3 điểm cao nhất

### Bài 2: Phân tích văn bản
Nhập đoạn văn, dùng các kỹ thuật đã học để:
- Đếm tần suất từ, sắp xếp theo tần suất giảm dần
- Tìm 5 từ xuất hiện nhiều nhất
- Tính độ dài trung bình của từ

---

## Tóm tắt buổi học
- **List Comprehension**: `[biểu_thức for x in list if điều_kiện]`
- **Lambda**: Hàm ẩn danh, viết gọn 1 dòng
- **map()**: Áp dụng hàm lên mọi phần tử
- **filter()**: Lọc phần tử theo điều kiện
- **sorted()**: Sắp xếp linh hoạt với key
- **Buổi sau**: Mini Project 3 - App tra cứu thời tiết
