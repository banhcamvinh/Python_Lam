# Buổi 16: Tkinter Nâng Cao

## Mục tiêu buổi học
- Sử dụng thêm widget: Listbox, Combobox, Messagebox, Menu
- Biết cách tổ chức layout phức tạp với Frame
- Tạo ứng dụng GUI hoàn chỉnh hơn

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-20 phút | Listbox, Scrollbar |
| 20-35 phút | Messagebox, Menu |
| 35-50 phút | Frame, tổ chức layout |
| 50-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Phần 1: Listbox & Scrollbar (15 phút)

```python
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Danh sách")

# Frame chứa listbox + scrollbar
frame = tk.Frame(cua_so)
frame.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame, font=("Arial", 12), width=30, height=10,
                      yscrollcommand=scrollbar.set)
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)

# Thêm dữ liệu
for i in range(1, 21):
    listbox.insert(tk.END, f"Mục {i}")

# Lấy mục được chọn
def xem_chon():
    chon = listbox.curselection()
    if chon:
        print(f"Đã chọn: {listbox.get(chon[0])}")

tk.Button(cua_so, text="Xem đã chọn", command=xem_chon).pack(pady=5)

cua_so.mainloop()
```

---

## Phần 2: Messagebox & Menu (15 phút)

### Messagebox

```python
from tkinter import messagebox

# Thông báo
messagebox.showinfo("Thông báo", "Lưu thành công!")

# Cảnh báo
messagebox.showwarning("Cảnh báo", "Dung lượng sắp đầy!")

# Lỗi
messagebox.showerror("Lỗi", "Không thể kết nối!")

# Hỏi xác nhận
ket_qua = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa?")
if ket_qua:
    print("Đã xóa")
```

### Menu

```python
import tkinter as tk
from tkinter import messagebox

cua_so = tk.Tk()

# Tạo thanh menu
menu_bar = tk.Menu(cua_so)

# Menu File
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Mới", command=lambda: print("Tạo mới"))
menu_file.add_command(label="Mở", command=lambda: print("Mở file"))
menu_file.add_separator()
menu_file.add_command(label="Thoát", command=cua_so.quit)
menu_bar.add_cascade(label="File", menu=menu_file)

# Menu Help
menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="Giới thiệu",
    command=lambda: messagebox.showinfo("Giới thiệu", "App v1.0"))
menu_bar.add_cascade(label="Help", menu=menu_help)

cua_so.config(menu=menu_bar)
cua_so.mainloop()
```

---

## Phần 3: Frame - Tổ Chức Layout (15 phút)

```python
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Layout với Frame")

# Frame trên - tiêu đề
frame_top = tk.Frame(cua_so, bg="#2196F3", height=50)
frame_top.pack(fill="x")
tk.Label(frame_top, text="📋 TODO LIST", font=("Arial", 16, "bold"),
         bg="#2196F3", fg="white").pack(pady=10)

# Frame giữa - nội dung
frame_mid = tk.Frame(cua_so)
frame_mid.pack(fill="both", expand=True, padx=10, pady=5)

# Frame dưới - nút bấm
frame_bot = tk.Frame(cua_so)
frame_bot.pack(fill="x", padx=10, pady=5)

# Widget trong frame_mid
entry = tk.Entry(frame_mid, font=("Arial", 12))
entry.pack(fill="x", pady=5)

listbox = tk.Listbox(frame_mid, font=("Arial", 12), height=8)
listbox.pack(fill="both", expand=True)

# Widget trong frame_bot
tk.Button(frame_bot, text="Thêm", bg="#4CAF50", fg="white").pack(
    side="left", padx=5)
tk.Button(frame_bot, text="Xóa", bg="#f44336", fg="white").pack(
    side="left", padx=5)

cua_so.mainloop()
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (30 phút)

### Bài thực hành: App Todo List GUI

```python
import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self):
        self.cua_so = tk.Tk()
        self.cua_so.title("📋 Todo List")
        self.cua_so.geometry("400x500")
        self.tao_giao_dien()

    def tao_giao_dien(self):
        # Tiêu đề
        tk.Label(self.cua_so, text="📋 TODO LIST",
                 font=("Arial", 18, "bold")).pack(pady=10)

        # Frame nhập
        frame_nhap = tk.Frame(self.cua_so)
        frame_nhap.pack(fill="x", padx=20)

        self.entry = tk.Entry(frame_nhap, font=("Arial", 13))
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", lambda e: self.them())

        tk.Button(frame_nhap, text="Thêm", command=self.them,
                  bg="#4CAF50", fg="white", font=("Arial", 11)).pack(
            side="right", padx=(5, 0))

        # Listbox
        frame_list = tk.Frame(self.cua_so)
        frame_list.pack(fill="both", expand=True, padx=20, pady=10)

        self.listbox = tk.Listbox(frame_list, font=("Arial", 13),
                                   selectbackground="#2196F3")
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame_list)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Nút xóa
        frame_btn = tk.Frame(self.cua_so)
        frame_btn.pack(fill="x", padx=20, pady=(0, 10))

        tk.Button(frame_btn, text="✅ Hoàn thành", command=self.hoan_thanh,
                  bg="#FF9800", fg="white", font=("Arial", 11)).pack(
            side="left", padx=5)
        tk.Button(frame_btn, text="🗑️ Xóa", command=self.xoa,
                  bg="#f44336", fg="white", font=("Arial", 11)).pack(
            side="left", padx=5)

        # Đếm
        self.label_dem = tk.Label(self.cua_so, text="0 công việc",
                                   font=("Arial", 11))
        self.label_dem.pack(pady=5)

    def them(self):
        viec = self.entry.get().strip()
        if viec:
            self.listbox.insert(tk.END, f"⬜ {viec}")
            self.entry.delete(0, tk.END)
            self.cap_nhat_dem()
        else:
            messagebox.showwarning("Cảnh báo", "Nhập công việc!")

    def hoan_thanh(self):
        chon = self.listbox.curselection()
        if chon:
            viec = self.listbox.get(chon[0])
            self.listbox.delete(chon[0])
            self.listbox.insert(chon[0], viec.replace("⬜", "✅"))
            self.cap_nhat_dem()

    def xoa(self):
        chon = self.listbox.curselection()
        if chon:
            if messagebox.askyesno("Xác nhận", "Xóa công việc này?"):
                self.listbox.delete(chon[0])
                self.cap_nhat_dem()

    def cap_nhat_dem(self):
        tong = self.listbox.size()
        self.label_dem.config(text=f"{tong} công việc")

    def chay(self):
        self.cua_so.mainloop()

TodoApp().chay()
```

---

## Bài Tập Về Nhà

### Bài 1: App ghi chú GUI
Chuyển sổ ghi chú (buổi 5) sang giao diện Tkinter

### Bài 2: App quản lý danh bạ GUI
Chuyển danh bạ (buổi 6) sang giao diện với Listbox, Entry, Button

---

## Tóm tắt buổi học
- **Listbox**: Hiển thị danh sách, chọn mục
- **Messagebox**: Thông báo, cảnh báo, xác nhận
- **Menu**: Thanh menu cho ứng dụng
- **Frame**: Nhóm widget, tổ chức layout
- **Buổi sau**: Kết nối GUI + Database
