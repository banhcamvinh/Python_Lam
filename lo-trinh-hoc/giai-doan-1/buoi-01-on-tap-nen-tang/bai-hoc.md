# Buổi 1: Ôn Tập Nền Tảng Python

## Mục tiêu buổi học
- Nhớ lại và nắm vững các khái niệm cơ bản nhất của Python
- Tự tin viết chương trình đơn giản với biến, input/output, điều kiện
- Hiểu rõ cách Python thực thi code từ trên xuống dưới

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-10 phút | Giới thiệu khóa học, làm quen |
| 10-30 phút | Ôn tập: Biến, kiểu dữ liệu, toán tử |
| 30-50 phút | Ôn tập: Input/Output, câu điều kiện |
| 50-75 phút | Thực hành có hướng dẫn |
| 75-90 phút | Bài tập tự làm + giao bài về nhà |

---

## Phần 1: Biến và Kiểu Dữ Liệu (20 phút)

### Biến là gì?
Biến giống như một "hộp" để chứa dữ liệu. Mình đặt tên cho hộp đó để sau này lấy ra dùng.

```python
# Tạo biến - giống như dán nhãn lên hộp
ten = "Minh"
tuoi = 18
diem_trung_binh = 8.5
da_tot_nghiep = True
```

### Các kiểu dữ liệu cơ bản

```python
# 1. Chuỗi (str) - để lưu chữ, văn bản
ho_ten = "Nguyễn Văn A"
lop = "CNTT01"

# 2. Số nguyên (int) - để lưu số không có phần thập phân
tuoi = 18
so_tin_chi = 120

# 3. Số thực (float) - để lưu số có phần thập phân
diem = 8.5
chieu_cao = 1.72

# 4. Boolean (bool) - chỉ có True hoặc False
dang_hoc = True
da_nghi = False
```

### Kiểm tra kiểu dữ liệu

```python
ten = "Minh"
tuoi = 18
diem = 8.5

# Dùng type() để xem kiểu dữ liệu
print(type(ten))    # <class 'str'>
print(type(tuoi))   # <class 'int'>
print(type(diem))   # <class 'float'>
```

### Chuyển đổi kiểu dữ liệu

```python
# Chuyển từ chuỗi sang số
tuoi_nhap = "18"          # Đây là chuỗi "18", không phải số 18
tuoi_so = int(tuoi_nhap)  # Giờ mới là số 18

# Chuyển từ số sang chuỗi
diem = 8.5
diem_text = str(diem)     # "8.5"

# Lỗi hay gặp: quên chuyển kiểu
tuoi = input("Nhập tuổi: ")  # input() luôn trả về chuỗi!
# tuoi + 1  # ❌ Lỗi! Không cộng chuỗi với số được
tuoi = int(tuoi)
print(tuoi + 1)  # ✅ Giờ mới đúng
```

### Toán tử cơ bản

```python
a = 10
b = 3

print(a + b)   # 13  - Cộng
print(a - b)   # 7   - Trừ
print(a * b)   # 30  - Nhân
print(a / b)   # 3.333... - Chia (luôn ra float)
print(a // b)  # 3   - Chia lấy phần nguyên
print(a % b)   # 1   - Chia lấy dư
print(a ** b)  # 1000 - Lũy thừa (10 mũ 3)
```

---

## Phần 2: Input/Output và Câu Điều Kiện (20 phút)

### Nhập xuất dữ liệu

```python
# Xuất dữ liệu ra màn hình
print("Xin chào!")
print("Tên tôi là", "Minh")  # Tự thêm khoảng trắng giữa các giá trị

# Dùng f-string (cách hiện đại và tiện nhất)
ten = "Minh"
tuoi = 18
print(f"Tôi tên {ten}, năm nay {tuoi} tuổi")
print("Tôi tên " + ten + ", năm nay " + tuoi + "tuổi")

# Nhập dữ liệu từ bàn phím
ten = input("Nhập tên của bạn: ")
tuoi = int(input("Nhập tuổi: "))  # Nhớ chuyển sang int!
print(f"Chào {ten}, bạn {tuoi} tuổi")
```

### Câu điều kiện if/elif/else

```python
# Ví dụ 1: Kiểm tra đủ tuổi bầu cử
tuoi = int(input("Nhập tuổi: "))

if tuoi >= 18:
    print("Bạn đủ tuổi bầu cử")
else:
    print("Bạn chưa đủ tuổi bầu cử")
```

```python
# Ví dụ 2: Xếp loại học lực
diem = float(input("Nhập điểm trung bình: "))

if diem >= 9.0:
    print("Xuất sắc")
elif diem >= 8.0:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5.0:
    print("Trung bình")
else:
    print("Yếu")
```

```python
# Ví dụ 3: Kết hợp nhiều điều kiện với and, or, not
tuoi = 20
co_cmnd = True

if tuoi >= 18 and co_cmnd:
    print("Đủ điều kiện đăng ký")
else:
    print("Chưa đủ điều kiện")
```

---

## Phần 3: Thực Hành Có Hướng Dẫn (25 phút)

### Bài thực hành 1: Máy tính tính tiền trà sữa
Viết chương trình tính tiền trà sữa cho khách.

```python
# === MÁY TÍNH TIỀN TRÀ SỮA ===

print("=== MENU TRÀ SỮA ===")
print("Trà sữa trân châu: 35,000đ")
print("Trà sữa matcha: 40,000đ")
print("Trà đào: 30,000đ")
print("==================")

# Nhập số lượng từng loại
tra_sua = int(input("Số ly trà sữa trân châu: "))
matcha = int(input("Số ly trà sữa matcha: "))
tra_dao = int(input("Số ly trà đào: "))

# Tính tổng tiền
tong_tien = tra_sua * 35000 + matcha * 40000 + tra_dao * 30000

# Giảm giá 10% nếu mua từ 5 ly trở lên
tong_ly = tra_sua + matcha + tra_dao

if tong_ly >= 5:
    giam_gia = tong_tien * 0.1
    tong_tien = tong_tien - giam_gia
    print(f"\nBạn được giảm 10%! Tiết kiệm {giam_gia:,.0f}đ")

print(f"Tổng số ly: {tong_ly}")
print(f"Tổng tiền: {tong_tien:,.0f}đ")
```

### Bài thực hành 2: Kiểm tra năm nhuận
Viết chương trình kiểm tra một năm có phải năm nhuận không.

```python
# === KIỂM TRA NĂM NHUẬN ===
# Quy tắc: chia hết cho 4, NHƯNG không chia hết cho 100, TRỪ KHI chia hết cho 400

nam = int(input("Nhập năm cần kiểm tra: "))

if nam % 400 == 0:
    print(f"{nam} là năm nhuận")
elif nam % 100 == 0:
    print(f"{nam} KHÔNG phải năm nhuận")
elif nam % 4 == 0:
    print(f"{nam} là năm nhuận")
else:
    print(f"{nam} KHÔNG phải năm nhuận")
```

---

## Phần 4: Bài Tập Tự Làm Tại Lớp (15 phút)

### Bài tập: Tính chỉ số BMI
Yêu cầu:
1. Nhập chiều cao (mét) và cân nặng (kg) từ bàn phím
2. Tính BMI = cân nặng / (chiều cao ** 2)
3. Phân loại:
   - BMI < 18.5: Thiếu cân
   - 18.5 <= BMI < 25: Bình thường
   - 25 <= BMI < 30: Thừa cân
   - BMI >= 30: Béo phì
4. In kết quả BMI (làm tròn 1 chữ số) và phân loại

> 💡 Gợi ý: Dùng `round(bmi, 1)` để làm tròn 1 chữ số thập phân

---

## Bài Tập Về Nhà

### Bài 1: Máy tính đơn giản
Viết chương trình cho phép người dùng:
- Nhập 2 số
- Chọn phép tính (+, -, *, /)
- In ra kết quả
- Xử lý trường hợp chia cho 0

### Bài 2: Tính tiền gửi xe
Viết chương trình tính tiền gửi xe ở bãi giữ xe:
- Xe đạp: 3,000đ/lượt
- Xe máy: 5,000đ/lượt (qua đêm: 10,000đ)
- Ô tô: 20,000đ/lượt (qua đêm: 40,000đ)
- Nhập loại xe và có qua đêm không, in ra số tiền phải trả

### Bài 3 (Nâng cao): Đổi tiền
Viết chương trình nhập một số tiền (VNĐ), đổi ra các tờ tiền lớn nhất có thể.
Ví dụ: 187,000đ → 1 tờ 100k + 1 tờ 50k + 1 tờ 20k + 1 tờ 10k + 1 tờ 5k + 1 tờ 2k

> 💡 Gợi ý: Dùng phép chia lấy phần nguyên (//) và chia lấy dư (%)

---

## Tóm tắt buổi học
- **Biến**: Hộp chứa dữ liệu, đặt tên để dùng lại
- **Kiểu dữ liệu**: str, int, float, bool
- **Input/Output**: input() để nhập, print() và f-string để xuất
- **Điều kiện**: if/elif/else để chương trình "ra quyết định"
- **Buổi sau**: Vòng lặp for, while - làm cho chương trình lặp lại công việc
