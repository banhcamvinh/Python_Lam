# Buổi 2: Vòng Lặp & Xử Lý Chuỗi

## Mục tiêu buổi học
- Hiểu và sử dụng thành thạo vòng lặp for và while
- Biết khi nào dùng for, khi nào dùng while
- Nắm được break, continue để điều khiển vòng lặp
- Thao tác cơ bản với chuỗi: cắt, nối, tìm kiếm, thay thế

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước, giải đáp bài tập về nhà |
| 5-25 phút | Vòng lặp for |
| 25-40 phút | Vòng lặp while, break/continue |
| 40-55 phút | Xử lý chuỗi |
| 55-75 phút | Thực hành có hướng dẫn |
| 75-90 phút | Bài tập tự làm + giao bài về nhà |

---

## Phần 1: Vòng Lặp for (20 phút)

### Tại sao cần vòng lặp?
Tưởng tượng bạn muốn in "Xin chào" 100 lần. Không lẽ viết 100 dòng print()? Vòng lặp giúp mình lặp lại một công việc nhiều lần mà chỉ viết code một lần.

### range() - Tạo dãy số

```python
# range(n) -> từ 0 đến n-1
for i in range(5):
    print(i)  # In ra: 0, 1, 2, 3, 4

# range(start, stop) -> từ start đến stop-1
for i in range(1, 6):
    print(i)  # In ra: 1, 2, 3, 4, 5

# range(start, stop, step) -> nhảy theo bước step
for i in range(0, 10, 2):
    print(i)  # In ra: 0, 2, 4, 6, 8

# Đếm ngược
for i in range(5, 0, -1):
    print(i)  # In ra: 5, 4, 3, 2, 1
```

### Duyệt qua chuỗi và danh sách

```python
# Duyệt từng ký tự trong chuỗi
ten = "Python"
for ky_tu in ten:
    print(ky_tu)  # P, y, t, h, o, n

# Duyệt danh sách
mon_hoc = ["Toán", "Lý", "Hóa", "Tin"]
for mon in mon_hoc:
    print(f"Môn: {mon}")
```

### Ví dụ thực tế: Bảng cửu chương

```python
# In bảng cửu chương của một số
so = int(input("Nhập số cần in bảng cửu chương: "))

print(f"\n--- Bảng cửu chương {so} ---")
for i in range(1, 11):
    print(f"{so} x {i} = {so * i}")
```

### Ví dụ thực tế: Tính tổng

```python
# Tính tổng từ 1 đến n
n = int(input("Nhập n: "))
tong = 0

for i in range(1, n + 1):
    tong = tong + i  # hoặc viết tắt: tong += i

print(f"Tổng từ 1 đến {n} = {tong}")
```

---

## Phần 2: Vòng Lặp while & break/continue (15 phút)

### while - Lặp khi điều kiện còn đúng

```python
# Đếm từ 1 đến 5
dem = 1
while dem <= 5:
    print(dem)
    dem += 1  # QUAN TRỌNG: phải thay đổi biến, không thì lặp vô hạn!
```

### Khi nào dùng for, khi nào dùng while?
- **for**: Khi biết trước số lần lặp (lặp 10 lần, duyệt danh sách...)
- **while**: Khi không biết trước, lặp cho đến khi thỏa điều kiện

```python
# Ví dụ: Hỏi mật khẩu cho đến khi đúng (không biết user nhập sai bao nhiêu lần)
mat_khau_dung = "python123"

mat_khau = input("Nhập mật khẩu: ")
while mat_khau != mat_khau_dung:
    print("❌ Sai mật khẩu, thử lại!")
    mat_khau = input("Nhập mật khẩu: ")

print("✅ Đăng nhập thành công!")
```

### break - Thoát vòng lặp ngay lập tức

```python
# Tìm số chia hết cho 7 đầu tiên trong khoảng 50-100
for so in range(50, 101):
    if so % 7 == 0:
        print(f"Số chia hết cho 7 đầu tiên: {so}")
        break  # Tìm thấy rồi, thoát luôn
```

### continue - Bỏ qua lần lặp hiện tại, nhảy sang lần tiếp

```python
# In các số từ 1-10, bỏ qua số chẵn
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Bỏ qua, không chạy print bên dưới
    print(i)  # Chỉ in: 1, 3, 5, 7, 9
```

### Ví dụ kết hợp: Menu chương trình

```python
# Chương trình chạy liên tục cho đến khi người dùng chọn thoát
while True:
    print("\n=== MENU ===")
    print("1. Chào hỏi")
    print("2. Tính tuổi")
    print("0. Thoát")

    lua_chon = input("Chọn: ")

    if lua_chon == "1":
        ten = input("Tên bạn: ")
        print(f"Xin chào {ten}!")
    elif lua_chon == "2":
        nam_sinh = int(input("Năm sinh: "))
        print(f"Bạn khoảng {2026 - nam_sinh} tuổi")
    elif lua_chon == "0":
        print("Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ!")
```

---

## Phần 3: Xử Lý Chuỗi (15 phút)

### Truy cập ký tự và cắt chuỗi (slicing)

```python
text = "Hello Python"

# Truy cập từng ký tự (đếm từ 0)
print(text[0])    # H
print(text[6])    # P
print(text[-1])   # n (ký tự cuối)

# Cắt chuỗi: text[start:stop]
print(text[0:5])   # Hello (từ vị trí 0 đến 4)
print(text[6:])    # Python (từ vị trí 6 đến hết)
print(text[:5])    # Hello (từ đầu đến vị trí 4)
```

### Các phương thức chuỗi hay dùng

```python
ten = "  nguyễn văn minh  "

# Xóa khoảng trắng thừa
print(ten.strip())        # "nguyễn văn minh"

# Chuyển hoa/thường
print(ten.strip().upper())    # "NGUYỄN VĂN MINH"
print(ten.strip().lower())    # "nguyễn văn minh"
print(ten.strip().title())    # "Nguyễn Văn Minh"

# Thay thế
email = "minh@gmail.com"
print(email.replace("gmail", "yahoo"))  # minh@yahoo.com

# Tìm kiếm
cau = "Tôi đang học Python"
print("Python" in cau)          # True
print(cau.find("Python"))       # 14 (vị trí tìm thấy)
print(cau.find("Java"))         # -1 (không tìm thấy)

# Đếm số lần xuất hiện
text = "banana"
print(text.count("a"))  # 3
```

### Tách và nối chuỗi

```python
# split() - Tách chuỗi thành danh sách
ho_ten = "Nguyễn Văn Minh"
cac_tu = ho_ten.split(" ")
print(cac_tu)       # ['Nguyễn', 'Văn', 'Minh']
print(cac_tu[-1])   # Minh (lấy tên)

# Tách CSV
diem_str = "8,7,9,6,10"
diem_list = diem_str.split(",")
print(diem_list)    # ['8', '7', '9', '6', '10']

# join() - Nối danh sách thành chuỗi
tu = ["Xin", "chào", "các", "bạn"]
cau = " ".join(tu)
print(cau)  # "Xin chào các bạn"

# Nối bằng dấu khác
print(" - ".join(tu))  # "Xin - chào - các - bạn"
```

### Ví dụ thực tế: Kiểm tra email đơn giản

```python
email = input("Nhập email: ")

if "@" in email and "." in email:
    # Tách lấy phần tên và domain
    ten_email = email.split("@")[0]
    domain = email.split("@")[1]
    print(f"Tên: {ten_email}")
    print(f"Domain: {domain}")
    print("✅ Email hợp lệ")
else:
    print("❌ Email không hợp lệ")
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (20 phút)

### Bài thực hành 1: Trò chơi đoán số
Máy tính random một số từ 1-100, người chơi đoán cho đến khi đúng.

```python
import random

# Máy chọn số ngẫu nhiên từ 1 đến 100
so_bi_mat = random.randint(1, 100)
so_lan_doan = 0

print("=== TRÒ CHƠI ĐOÁN SỐ ===")
print("Tôi đang nghĩ một số từ 1 đến 100. Bạn đoán đi!")

while True:
    doan = int(input("Nhập số bạn đoán: "))
    so_lan_doan += 1

    if doan < so_bi_mat:
        print("📈 Lớn hơn đi!")
    elif doan > so_bi_mat:
        print("📉 Nhỏ hơn đi!")
    else:
        print(f"🎉 Chính xác! Bạn đoán đúng sau {so_lan_doan} lần!")
        break

# Đánh giá
if so_lan_doan <= 5:
    print("Xuất sắc! 🌟")
elif so_lan_doan <= 10:
    print("Khá lắm! 👍")
else:
    print("Cần luyện thêm nhé! 💪")
```

### Bài thực hành 2: Đếm nguyên âm trong câu

```python
# Đếm số nguyên âm trong một câu
cau = input("Nhập một câu: ")
nguyen_am = "aeiouAEIOU"
dem = 0

for ky_tu in cau:
    if ky_tu in nguyen_am:
        dem += 1

print(f"Câu: \"{cau}\"")
print(f"Số nguyên âm: {dem}")

# Bonus: Hiển thị chi tiết
print("\nChi tiết:")
for na in "aeiou":
    so_lan = cau.lower().count(na)
    if so_lan > 0:
        print(f"  '{na}': {so_lan} lần")
```

---

## Phần 5: Bài Tập Tự Làm Tại Lớp (15 phút)

### Bài tập: In hình tam giác sao
Yêu cầu:
1. Nhập số dòng n
2. In tam giác sao như mẫu (n=5):

```
*
**
***
****
*****
```

> 💡 Gợi ý: Dùng `"*" * i` để lặp ký tự, kết hợp vòng for

Nâng cao: In tam giác cân
```
    *
   ***
  *****
 *******
*********
```

> 💡 Gợi ý: Mỗi dòng i cần `(n-i)` khoảng trắng và `(2*i - 1)` dấu sao

---

## Bài Tập Về Nhà

### Bài 1: Tìm số nguyên tố
Viết chương trình nhập số n, kiểm tra n có phải số nguyên tố không.
- Số nguyên tố là số > 1 và chỉ chia hết cho 1 và chính nó
- Gợi ý: Dùng vòng lặp kiểm tra từ 2 đến n-1 (hoặc tối ưu hơn: đến căn bậc 2 của n)

### Bài 2: Đảo ngược chuỗi
Viết chương trình nhập một chuỗi và in ra chuỗi đảo ngược.
- Ví dụ: "Python" → "nohtyP"
- Thử 2 cách: dùng vòng lặp và dùng slicing

### Bài 3: Mật khẩu mạnh
Viết chương trình kiểm tra mật khẩu có đủ mạnh không:
- Ít nhất 8 ký tự
- Có ít nhất 1 chữ hoa
- Có ít nhất 1 chữ thường
- Có ít nhất 1 số
- Gợi ý: Dùng các phương thức `.isupper()`, `.islower()`, `.isdigit()` kết hợp vòng lặp

### Bài 4 (Nâng cao): Mã hóa Caesar
Viết chương trình mã hóa một câu bằng mật mã Caesar (dịch mỗi chữ cái đi k vị trí).
- Ví dụ với k=3: "abc" → "def", "xyz" → "abc"
- Chỉ mã hóa chữ cái, giữ nguyên số và ký tự đặc biệt
- Gợi ý: Dùng `ord()` và `chr()` để chuyển ký tự ↔ mã ASCII

---

## Tóm tắt buổi học
- **for**: Lặp khi biết trước số lần, duyệt danh sách/chuỗi
- **while**: Lặp khi chưa biết trước, dừng khi điều kiện sai
- **break**: Thoát vòng lặp ngay, **continue**: Bỏ qua lần lặp hiện tại
- **Chuỗi**: Cắt (slicing), tìm (find/in), tách (split), nối (join), thay thế (replace)
- **Buổi sau**: List, Tuple, Dictionary - cấu trúc dữ liệu để quản lý nhiều dữ liệu
