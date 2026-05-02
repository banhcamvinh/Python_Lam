# 🐍 Tổng Quan Lộ Trình Học Python - Từ Cơ Bản Đến Tự Làm App

## Thông tin chung
- **Đối tượng**: Sinh viên đại học năm nhất, đã biết Python cơ bản nhưng chưa vững
- **Mục tiêu**: Tự xây dựng được ứng dụng hoàn chỉnh (GUI hoặc Web)
- **Tổng số buổi**: 20 buổi (mỗi buổi 90 phút)
- **Cấu trúc mỗi buổi**: Lý thuyết → Ví dụ minh họa → Thực hành → Bài tập về nhà

---

## Sơ Đồ Lộ Trình

```
┌─────────────────────────────────────────────────────────────┐
│                    GIAI ĐOẠN 1 (Buổi 1-6)                  │
│                  Củng Cố Nền Tảng Python                    │
│                                                             │
│  Buổi 1: Biến, kiểu dữ liệu, if/else                     │
│  Buổi 2: Vòng lặp for/while, xử lý chuỗi                 │
│  Buổi 3: List, Tuple, Dictionary                           │
│  Buổi 4: Hàm (Function)                                    │
│  Buổi 5: Đọc/ghi file, try/except                         │
│  Buổi 6: 🏆 Mini Project 1 - Quản lý danh bạ (console)   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    GIAI ĐOẠN 2 (Buổi 7-10)                 │
│              Lập Trình Hướng Đối Tượng (OOP)               │
│                                                             │
│  Buổi 7:  Class, Object, __init__, phương thức             │
│  Buổi 8:  Kế thừa, đa hình, đóng gói                     │
│  Buổi 9:  Module, Package, pip, venv                       │
│  Buổi 10: 🏆 Mini Project 2 - Quản lý SV (OOP + JSON)    │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    GIAI ĐOẠN 3 (Buổi 11-14)                │
│                  Làm Việc Với Dữ Liệu                      │
│                                                             │
│  Buổi 11: SQLite Database + Python                         │
│  Buổi 12: Gọi API, xử lý JSON, requests                   │
│  Buổi 13: List comprehension, lambda, map/filter           │
│  Buổi 14: 🏆 Mini Project 3 - App thời tiết (API + DB)   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    GIAI ĐOẠN 4 (Buổi 15-20)                │
│            Xây Dựng Ứng Dụng Có Giao Diện                  │
│                                                             │
│  Buổi 15: Tkinter cơ bản - Label, Button, Entry           │
│  Buổi 16: Tkinter nâng cao - Listbox, Menu, Frame         │
│  Buổi 17: Kết nối GUI + Database                          │
│  Buổi 18: Web app Flask (1) - Route, Template, Form       │
│  Buổi 19: Web app Flask (2) - Database, Login, Deploy     │
│  Buổi 20: 🎓 Đồ án cuối khóa - Trình bày sản phẩm       │
└─────────────────────────────────────────────────────────────┘
```

---

## Chi Tiết Từng Buổi

### 📘 Giai đoạn 1: Củng Cố Nền Tảng (Buổi 1-6)

| Buổi | Chủ đề | Kiến thức chính | Thực hành |
|------|--------|-----------------|-----------|
| 1 | Ôn tập nền tảng | Biến, kiểu dữ liệu, toán tử, if/elif/else | Tính tiền trà sữa, kiểm tra năm nhuận |
| 2 | Vòng lặp & chuỗi | for, while, break/continue, xử lý chuỗi | Trò chơi đoán số, đếm nguyên âm |
| 3 | List, Tuple, Dict | Cấu trúc dữ liệu, CRUD, duyệt | Quản lý điểm, đếm tần suất từ |
| 4 | Hàm (Function) | Định nghĩa hàm, tham số, return, scope | Máy tính bỏ túi, kiểm tra mật khẩu |
| 5 | File & Ngoại lệ | Đọc/ghi file, try/except | Sổ ghi chú |
| 6 | **Mini Project 1** | Tổng hợp GĐ1 | **Quản lý danh bạ (console)** |

### 📗 Giai đoạn 2: Lập Trình Hướng Đối Tượng (Buổi 7-10)

| Buổi | Chủ đề | Kiến thức chính | Thực hành |
|------|--------|-----------------|-----------|
| 7 | OOP cơ bản | Class, object, __init__, self, __str__ | Quản lý lớp học, tài khoản ngân hàng |
| 8 | OOP nâng cao | Kế thừa, đa hình, đóng gói, super() | Hệ thống nhân viên, hình học |
| 9 | Module & Package | import, module riêng, pip, venv, json | Xổ số Python |
| 10 | **Mini Project 2** | Tổng hợp GĐ2 | **Quản lý sinh viên (OOP + JSON)** |

### 📙 Giai đoạn 3: Làm Việc Với Dữ Liệu (Buổi 11-14)

| Buổi | Chủ đề | Kiến thức chính | Thực hành |
|------|--------|-----------------|-----------|
| 11 | SQLite & Python | SQL cơ bản, CRUD, sqlite3 | Quản lý sản phẩm |
| 12 | API cơ bản | HTTP, requests, JSON, xử lý lỗi | Từ điển Anh-Anh |
| 13 | Xử lý dữ liệu | Comprehension, lambda, map/filter, sorted | Phân tích bán hàng |
| 14 | **Mini Project 3** | Tổng hợp GĐ3 | **App tra cứu thời tiết (API + DB)** |

### 📕 Giai đoạn 4: Xây Dựng Ứng Dụng (Buổi 15-20)

| Buổi | Chủ đề | Kiến thức chính | Thực hành |
|------|--------|-----------------|-----------|
| 15 | Tkinter cơ bản | Label, Button, Entry, pack/grid | Máy tính GUI |
| 16 | Tkinter nâng cao | Listbox, Messagebox, Menu, Frame | Todo List GUI |
| 17 | GUI + Database | Treeview, SQLite + Tkinter | Quản lý sản phẩm GUI |
| 18 | Flask (1) | Route, Template, Jinja2, Form | Web app cơ bản |
| 19 | Flask (2) | Flask + SQLite, Session/Login, Deploy | Web app hoàn chỉnh |
| 20 | **Đồ án cuối khóa** | Tổng hợp toàn bộ | **Trình bày sản phẩm cá nhân** |

---

## Cấu Trúc Thư Mục

```
lo-trinh-hoc/
├── OVERVIEW.md              ← File này
├── README.md                ← Mô tả lộ trình
│
├── giai-doan-1/             ← Củng cố nền tảng
│   ├── buoi-01-on-tap-nen-tang/
│   │   ├── bai-hoc.md      ← Nội dung bài giảng
│   │   ├── vi-du/           ← Code ví dụ minh họa
│   │   └── thuc-hanh/       ← Code bài thực hành
│   ├── buoi-02-vong-lap-va-chuoi/
│   ├── buoi-03-list-tuple-dict/
│   ├── buoi-04-ham/
│   ├── buoi-05-file-va-ngoai-le/
│   └── buoi-06-mini-project-1/
│
├── giai-doan-2/             ← OOP
│   ├── buoi-07-oop-co-ban/
│   ├── buoi-08-oop-nang-cao/
│   ├── buoi-09-module-package/
│   └── buoi-10-mini-project-2/
│
├── giai-doan-3/             ← Dữ liệu
│   ├── buoi-11-sqlite/
│   ├── buoi-12-api/
│   ├── buoi-13-xu-ly-du-lieu/
│   └── buoi-14-mini-project-3/
│
└── giai-doan-4/             ← Ứng dụng
    ├── buoi-15-tkinter-co-ban/
    ├── buoi-16-tkinter-nang-cao/
    ├── buoi-17-gui-database/
    ├── buoi-18-flask-1/
    ├── buoi-19-flask-2/
    └── buoi-20-do-an-cuoi-khoa/
```

---

## Ghi Chú Cho Giảng Viên

### Nguyên tắc giảng dạy
- Mỗi buổi bắt đầu bằng ôn nhanh buổi trước (5 phút)
- Ví dụ gần gũi với sinh viên (trà sữa, điểm, danh bạ...)
- Code comment bằng tiếng Việt
- Khuyến khích học sinh hỏi và thử nghiệm

### Điều chỉnh tốc độ
- Nếu lớp tiếp thu nhanh: thêm bài tập nâng cao, rút ngắn phần ôn
- Nếu lớp cần thêm thời gian: có thể chia buổi 17-19 thành nhiều buổi hơn
- Mini project có thể kéo dài 2 buổi nếu cần

### Đánh giá
- Bài tập về nhà: theo dõi tiến độ
- Mini project: đánh giá tổng hợp mỗi giai đoạn
- Đồ án cuối khóa: đánh giá toàn diện
