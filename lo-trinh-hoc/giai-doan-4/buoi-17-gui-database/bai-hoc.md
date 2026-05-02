# Buổi 17: Kết Nối GUI + Database

## Mục tiêu buổi học
- Kết hợp Tkinter với SQLite để tạo app hoàn chỉnh
- Hiển thị dữ liệu từ database lên giao diện
- CRUD đầy đủ qua giao diện đồ họa

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-15 phút | Thiết kế giao diện + database |
| 15-50 phút | Code app quản lý sản phẩm GUI |
| 50-80 phút | Thực hành hoàn thiện |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Bài Thực Hành: Quản Lý Sản Phẩm GUI + SQLite

### Thiết kế

```
┌─────────────────────────────────────┐
│         🏪 QUẢN LÝ SẢN PHẨM        │
├─────────────────────────────────────┤
│ Tên SP: [____________]              │
│ Giá:    [____________]              │
│ SL:     [____________]              │
│ [Thêm] [Sửa] [Xóa] [Làm mới]     │
├─────────────────────────────────────┤
│ ID | Tên SP      | Giá     | SL    │
│ 1  | Laptop      | 15,000k | 5     │
│ 2  | Chuột       | 200k    | 20    │
│ ...                                 │
├─────────────────────────────────────┤
│ Tổng: 5 sản phẩm | Giá trị kho: x │
└─────────────────────────────────────┘
```

### Code hoàn chỉnh

```python
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class QuanLySanPham:
    DB = "san_pham_gui.db"

    def __init__(self):
        self.cua_so = tk.Tk()
        self.cua_so.title("🏪 Quản Lý Sản Phẩm")
        self.cua_so.geometry("600x500")
        self.tao_database()
        self.tao_giao_dien()
        self.tai_du_lieu()

    def tao_database(self):
        conn = sqlite3.connect(self.DB)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS san_pham (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ten TEXT NOT NULL,
                gia REAL,
                so_luong INTEGER DEFAULT 0
            )
        """)
        conn.commit()
        conn.close()

    def tao_giao_dien(self):
        # Frame nhập liệu
        frame_nhap = tk.LabelFrame(self.cua_so, text="Thông tin sản phẩm",
                                     padx=10, pady=10)
        frame_nhap.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_nhap, text="Tên SP:").grid(row=0, column=0, sticky="w")
        self.entry_ten = tk.Entry(frame_nhap, width=30)
        self.entry_ten.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(frame_nhap, text="Giá:").grid(row=1, column=0, sticky="w")
        self.entry_gia = tk.Entry(frame_nhap, width=30)
        self.entry_gia.grid(row=1, column=1, padx=5, pady=3)

        tk.Label(frame_nhap, text="Số lượng:").grid(row=2, column=0, sticky="w")
        self.entry_sl = tk.Entry(frame_nhap, width=30)
        self.entry_sl.grid(row=2, column=1, padx=5, pady=3)

        # Frame nút bấm
        frame_btn = tk.Frame(self.cua_so)
        frame_btn.pack(fill="x", padx=10, pady=5)

        tk.Button(frame_btn, text="➕ Thêm", command=self.them,
                  bg="#4CAF50", fg="white", width=10).pack(side="left", padx=3)
        tk.Button(frame_btn, text="✏️ Sửa", command=self.sua,
                  bg="#FF9800", fg="white", width=10).pack(side="left", padx=3)
        tk.Button(frame_btn, text="🗑️ Xóa", command=self.xoa,
                  bg="#f44336", fg="white", width=10).pack(side="left", padx=3)
        tk.Button(frame_btn, text="🔄 Làm mới", command=self.lam_moi,
                  width=10).pack(side="left", padx=3)

        # Treeview (bảng dữ liệu)
        frame_bang = tk.Frame(self.cua_so)
        frame_bang.pack(fill="both", expand=True, padx=10, pady=5)

        cols = ("id", "ten", "gia", "so_luong")
        self.tree = ttk.Treeview(frame_bang, columns=cols, show="headings",
                                  height=10)
        self.tree.heading("id", text="ID")
        self.tree.heading("ten", text="Tên SP")
        self.tree.heading("gia", text="Giá")
        self.tree.heading("so_luong", text="SL")

        self.tree.column("id", width=40)
        self.tree.column("ten", width=200)
        self.tree.column("gia", width=120)
        self.tree.column("so_luong", width=60)

        self.tree.pack(side="left", fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.chon_dong)

        scrollbar = ttk.Scrollbar(frame_bang, command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.config(yscrollcommand=scrollbar.set)

        # Label thống kê
        self.label_thongke = tk.Label(self.cua_so, text="",
                                       font=("Arial", 10))
        self.label_thongke.pack(pady=5)

    def tai_du_lieu(self):
        # Xóa dữ liệu cũ trên bảng
        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = sqlite3.connect(self.DB)
        rows = conn.execute("SELECT * FROM san_pham ORDER BY ten").fetchall()
        conn.close()

        tong_gia_tri = 0
        for row in rows:
            self.tree.insert("", tk.END, values=(
                row[0], row[1], f"{row[2]:,.0f}đ", row[3]
            ))
            tong_gia_tri += row[2] * row[3]

        self.label_thongke.config(
            text=f"Tổng: {len(rows)} SP | Giá trị kho: {tong_gia_tri:,.0f}đ"
        )

    def them(self):
        ten = self.entry_ten.get().strip()
        try:
            gia = float(self.entry_gia.get())
            sl = int(self.entry_sl.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Giá và SL phải là số!")
            return

        if not ten:
            messagebox.showerror("Lỗi", "Nhập tên sản phẩm!")
            return

        conn = sqlite3.connect(self.DB)
        conn.execute("INSERT INTO san_pham (ten, gia, so_luong) VALUES (?,?,?)",
                     (ten, gia, sl))
        conn.commit()
        conn.close()

        self.lam_moi()
        messagebox.showinfo("OK", f"Đã thêm {ten}")

    def sua(self):
        chon = self.tree.selection()
        if not chon:
            messagebox.showwarning("Cảnh báo", "Chọn sản phẩm cần sửa!")
            return

        id_sp = self.tree.item(chon[0])["values"][0]
        ten = self.entry_ten.get().strip()
        try:
            gia = float(self.entry_gia.get())
            sl = int(self.entry_sl.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Giá và SL phải là số!")
            return

        conn = sqlite3.connect(self.DB)
        conn.execute("UPDATE san_pham SET ten=?, gia=?, so_luong=? WHERE id=?",
                     (ten, gia, sl, id_sp))
        conn.commit()
        conn.close()

        self.lam_moi()
        messagebox.showinfo("OK", "Đã cập nhật!")

    def xoa(self):
        chon = self.tree.selection()
        if not chon:
            messagebox.showwarning("Cảnh báo", "Chọn sản phẩm cần xóa!")
            return

        if not messagebox.askyesno("Xác nhận", "Xóa sản phẩm này?"):
            return

        id_sp = self.tree.item(chon[0])["values"][0]
        conn = sqlite3.connect(self.DB)
        conn.execute("DELETE FROM san_pham WHERE id=?", (id_sp,))
        conn.commit()
        conn.close()

        self.lam_moi()

    def chon_dong(self, event):
        chon = self.tree.selection()
        if chon:
            values = self.tree.item(chon[0])["values"]
            self.entry_ten.delete(0, tk.END)
            self.entry_ten.insert(0, values[1])
            self.entry_gia.delete(0, tk.END)
            self.entry_gia.insert(0, str(values[2]).replace(",", "").replace("đ", ""))
            self.entry_sl.delete(0, tk.END)
            self.entry_sl.insert(0, values[3])

    def lam_moi(self):
        self.entry_ten.delete(0, tk.END)
        self.entry_gia.delete(0, tk.END)
        self.entry_sl.delete(0, tk.END)
        self.tai_du_lieu()

    def chay(self):
        self.cua_so.mainloop()

QuanLySanPham().chay()
```

---

## Bài Tập Về Nhà

### Bài 1: Quản lý sinh viên GUI
Chuyển Mini Project 2 sang giao diện Tkinter + SQLite

### Bài 2: Thêm tìm kiếm
Thêm ô tìm kiếm vào app sản phẩm, lọc theo tên

---

## Tóm tắt buổi học
- **Treeview**: Widget bảng dữ liệu chuyên nghiệp
- **LabelFrame**: Nhóm widget có tiêu đề
- **Kết hợp GUI + DB**: Hiển thị, thêm, sửa, xóa qua giao diện
- **Buổi sau**: Web app với Flask (phần 1)
