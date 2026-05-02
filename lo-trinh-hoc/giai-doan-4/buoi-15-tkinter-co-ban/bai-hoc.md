# Buổi 15: Tkinter Cơ Bản - Tạo Giao Diện

## Mục tiêu buổi học
- Hiểu cách tạo ứng dụng có giao diện (GUI) bằng Tkinter
- Biết cách tạo cửa sổ, label, button, entry
- Xử lý sự kiện khi người dùng click button

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Giới thiệu Giai đoạn 4 |
| 5-20 phút | Cửa sổ đầu tiên, Label, Button |
| 20-40 phút | Entry, xử lý sự kiện |
| 40-55 phút | Layout cơ bản (pack, grid) |
| 55-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Phần 1: Cửa Sổ Đầu Tiên (15 phút)

### Tkinter là gì?
Tkinter là thư viện GUI có sẵn trong Python. Không cần cài thêm gì, chỉ import là dùng.

```python
import tkinter as tk

# Tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("App đầu tiên")
cua_so.geometry("400x300")  # Rộng x Cao

# Label - hiển thị text
label = tk.Label(cua_so, text="Xin chào! 👋", font=("Arial", 20))
label.pack(pady=20)

# Button - nút bấm
def khi_click():
    label.config(text="Bạn đã click! 🎉")

btn = tk.Button(cua_so, text="Click tôi", command=khi_click,
                font=("Arial", 14), bg="#4CAF50", fg="white")
btn.pack(pady=10)

# Chạy ứng dụng
cua_so.mainloop()
```

---

## Phần 2: Entry & Xử Lý Sự Kiện (20 phút)

### Entry - Ô nhập liệu

```python
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Chào hỏi")
cua_so.geometry("400x200")

# Label hướng dẫn
tk.Label(cua_so, text="Nhập tên:", font=("Arial", 14)).pack(pady=5)

# Entry - ô nhập
entry_ten = tk.Entry(cua_so, font=("Arial", 14), width=25)
entry_ten.pack(pady=5)

# Label kết quả
label_kq = tk.Label(cua_so, text="", font=("Arial", 16))
label_kq.pack(pady=10)

# Xử lý khi click
def chao():
    ten = entry_ten.get()  # Lấy text từ entry
    if ten:
        label_kq.config(text=f"Xin chào {ten}! 👋")
    else:
        label_kq.config(text="Bạn chưa nhập tên!")

tk.Button(cua_so, text="Chào", command=chao,
          font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=5)

cua_so.mainloop()
```

---

## Phần 3: Layout (15 phút)

### Pack - Xếp theo chiều dọc/ngang

```python
# pack() mặc định xếp từ trên xuống
label1.pack()       # Trên
label2.pack()       # Giữa
label3.pack()       # Dưới

# Tùy chỉnh
label.pack(side="left")    # Xếp trái
label.pack(side="right")   # Xếp phải
label.pack(pady=10)        # Padding dọc
label.pack(padx=10)        # Padding ngang
```

### Grid - Xếp theo lưới (hàng, cột)

```python
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Form đăng ký")

# Hàng 0
tk.Label(cua_so, text="Họ tên:").grid(row=0, column=0, padx=10, pady=5)
entry_ten = tk.Entry(cua_so)
entry_ten.grid(row=0, column=1, padx=10, pady=5)

# Hàng 1
tk.Label(cua_so, text="Email:").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(cua_so)
entry_email.grid(row=1, column=1, padx=10, pady=5)

# Hàng 2
tk.Label(cua_so, text="Tuổi:").grid(row=2, column=0, padx=10, pady=5)
entry_tuoi = tk.Entry(cua_so)
entry_tuoi.grid(row=2, column=1, padx=10, pady=5)

# Hàng 3 - Button
tk.Button(cua_so, text="Đăng ký", bg="#4CAF50", fg="white").grid(
    row=3, column=0, columnspan=2, pady=10)

cua_so.mainloop()
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (25 phút)

### Bài thực hành: Máy tính GUI

```python
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("🧮 Máy Tính")
cua_so.geometry("300x400")
cua_so.resizable(False, False)

# Ô hiển thị
man_hinh = tk.Entry(cua_so, font=("Arial", 24), justify="right",
                     bd=5, relief="sunken")
man_hinh.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Biến lưu phép tính
phep_tinh = ""

def click_so(so):
    global phep_tinh
    phep_tinh += str(so)
    man_hinh.delete(0, tk.END)
    man_hinh.insert(tk.END, phep_tinh)

def click_phep(p):
    global phep_tinh
    phep_tinh += p
    man_hinh.delete(0, tk.END)
    man_hinh.insert(tk.END, phep_tinh)

def tinh_ket_qua():
    global phep_tinh
    try:
        kq = eval(phep_tinh)
        man_hinh.delete(0, tk.END)
        man_hinh.insert(tk.END, str(kq))
        phep_tinh = str(kq)
    except:
        man_hinh.delete(0, tk.END)
        man_hinh.insert(tk.END, "Lỗi")
        phep_tinh = ""

def xoa():
    global phep_tinh
    phep_tinh = ""
    man_hinh.delete(0, tk.END)

# Tạo các nút
cac_nut = [
    ("C", 1, 0), ("/", 1, 1), ("*", 1, 2), ("-", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("=", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("0", 4, 3),
]

for (text, row, col) in cac_nut:
    if text == "C":
        cmd = xoa
    elif text == "=":
        cmd = tinh_ket_qua
    elif text in "+-*/":
        cmd = lambda p=text: click_phep(p)
    else:
        cmd = lambda s=text: click_so(s)

    tk.Button(cua_so, text=text, font=("Arial", 18), width=4, height=2,
              command=cmd).grid(row=row, column=col, padx=2, pady=2)

cua_so.mainloop()
```

---

## Bài Tập Về Nhà

### Bài 1: App đổi đơn vị
Tạo GUI đổi nhiệt độ (°C ↔ °F) hoặc đổi tiền tệ

### Bài 2: App đếm từ
Tạo GUI nhập văn bản, hiển thị: số từ, số ký tự, số dòng

---

## Tóm tắt buổi học
- **Tkinter**: Thư viện GUI có sẵn trong Python
- **Widget cơ bản**: Label, Button, Entry
- **Layout**: pack() đơn giản, grid() linh hoạt
- **command**: Gắn hàm xử lý cho button
- **Buổi sau**: Tkinter nâng cao - Listbox, Menu, MessageBox
