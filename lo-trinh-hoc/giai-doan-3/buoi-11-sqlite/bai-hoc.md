# Buổi 11: SQLite & Python

## Mục tiêu buổi học
- Hiểu database là gì và tại sao cần dùng
- Biết cách tạo database SQLite, tạo bảng
- Thực hiện CRUD (Create, Read, Update, Delete) với SQL
- Kết nối Python với SQLite

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Giới thiệu Giai đoạn 3 |
| 5-20 phút | Database là gì? SQL cơ bản |
| 20-40 phút | Kết nối Python + SQLite |
| 40-55 phút | CRUD hoàn chỉnh |
| 55-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Phần 1: Database & SQL Cơ Bản (15 phút)

### Tại sao cần database?
File text/JSON ổn cho dữ liệu nhỏ, nhưng khi có hàng nghìn bản ghi, cần tìm kiếm nhanh, lọc phức tạp → cần database.

### SQLite
- Database nhẹ, không cần cài server
- Lưu trong 1 file duy nhất (`.db`)
- Python có sẵn module `sqlite3`

### SQL cơ bản

```sql
-- Tạo bảng
CREATE TABLE sinh_vien (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten TEXT NOT NULL,
    tuoi INTEGER,
    diem REAL
);

-- Thêm dữ liệu
INSERT INTO sinh_vien (ten, tuoi, diem) VALUES ('Minh', 18, 8.5);

-- Đọc dữ liệu
SELECT * FROM sinh_vien;
SELECT ten, diem FROM sinh_vien WHERE diem >= 8.0;

-- Cập nhật
UPDATE sinh_vien SET diem = 9.0 WHERE ten = 'Minh';

-- Xóa
DELETE FROM sinh_vien WHERE id = 1;
```

---

## Phần 2: Python + SQLite (20 phút)

### Kết nối và tạo bảng

```python
import sqlite3

# Kết nối (tạo file nếu chưa có)
conn = sqlite3.connect("truong_hoc.db")
cursor = conn.cursor()

# Tạo bảng
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sinh_vien (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten TEXT NOT NULL,
        ma_sv TEXT UNIQUE,
        tuoi INTEGER,
        diem REAL
    )
""")
conn.commit()
print("✅ Đã tạo bảng sinh_vien")

conn.close()
```

### CRUD với Python

```python
import sqlite3

def ket_noi():
    return sqlite3.connect("truong_hoc.db")

# CREATE - Thêm
def them_sv(ten, ma_sv, tuoi, diem):
    conn = ket_noi()
    try:
        conn.execute(
            "INSERT INTO sinh_vien (ten, ma_sv, tuoi, diem) VALUES (?, ?, ?, ?)",
            (ten, ma_sv, tuoi, diem)
        )
        conn.commit()
        print(f"✅ Đã thêm {ten}")
    except sqlite3.IntegrityError:
        print(f"⚠️ Mã SV '{ma_sv}' đã tồn tại!")
    finally:
        conn.close()

# READ - Đọc
def xem_tat_ca():
    conn = ket_noi()
    cursor = conn.execute("SELECT * FROM sinh_vien ORDER BY ten")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("📭 Chưa có sinh viên!")
        return

    print(f"\n📋 Danh sách ({len(rows)} SV):")
    print("-" * 55)
    for row in rows:
        id, ten, ma_sv, tuoi, diem = row
        print(f"  {ma_sv} | {ten:<15} | {tuoi} tuổi | Điểm: {diem}")
    print("-" * 55)

# UPDATE - Cập nhật
def cap_nhat_diem(ma_sv, diem_moi):
    conn = ket_noi()
    cursor = conn.execute(
        "UPDATE sinh_vien SET diem = ? WHERE ma_sv = ?",
        (diem_moi, ma_sv)
    )
    conn.commit()
    if cursor.rowcount > 0:
        print(f"✅ Đã cập nhật điểm cho {ma_sv}")
    else:
        print(f"🔍 Không tìm thấy {ma_sv}")
    conn.close()

# DELETE - Xóa
def xoa_sv(ma_sv):
    conn = ket_noi()
    cursor = conn.execute("DELETE FROM sinh_vien WHERE ma_sv = ?", (ma_sv,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"🗑️ Đã xóa {ma_sv}")
    else:
        print(f"🔍 Không tìm thấy {ma_sv}")
    conn.close()

# Tìm kiếm
def tim_kiem(tu_khoa):
    conn = ket_noi()
    cursor = conn.execute(
        "SELECT * FROM sinh_vien WHERE ten LIKE ?",
        (f"%{tu_khoa}%",)
    )
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print(f"🔍 Không tìm thấy '{tu_khoa}'")
    else:
        for row in rows:
            print(f"  {row[2]} | {row[1]} | Điểm: {row[4]}")
```

---

## Phần 3: Thực Hành Có Hướng Dẫn (25 phút)

### Bài thực hành: Quản lý sản phẩm

```python
import sqlite3

def tao_bang():
    conn = sqlite3.connect("cua_hang.db")
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

def them_sp(ten, gia, so_luong):
    conn = sqlite3.connect("cua_hang.db")
    conn.execute("INSERT INTO san_pham (ten, gia, so_luong) VALUES (?, ?, ?)",
                 (ten, gia, so_luong))
    conn.commit()
    conn.close()
    print(f"✅ Đã thêm {ten}")

def xem_sp():
    conn = sqlite3.connect("cua_hang.db")
    rows = conn.execute("SELECT * FROM san_pham ORDER BY ten").fetchall()
    conn.close()

    if not rows:
        print("📭 Chưa có sản phẩm!")
        return

    print(f"\n🏪 Kho hàng ({len(rows)} SP):")
    print("-" * 50)
    for id, ten, gia, sl in rows:
        print(f"  {id}. {ten:<20} | {gia:>10,.0f}đ | SL: {sl}")
    print("-" * 50)

    tong = sum(row[2] * row[3] for row in rows)
    print(f"  Tổng giá trị kho: {tong:,.0f}đ")

# Chương trình chính
tao_bang()

while True:
    print("\n=== CỬA HÀNG ===")
    print("1. Thêm SP  2. Xem kho  3. Tìm  0. Thoát")
    chon = input("Chọn: ")

    if chon == "1":
        ten = input("Tên SP: ")
        gia = float(input("Giá: "))
        sl = int(input("Số lượng: "))
        them_sp(ten, gia, sl)
    elif chon == "2":
        xem_sp()
    elif chon == "3":
        kw = input("Tìm: ")
        conn = sqlite3.connect("cua_hang.db")
        rows = conn.execute("SELECT * FROM san_pham WHERE ten LIKE ?",
                           (f"%{kw}%",)).fetchall()
        conn.close()
        for r in rows:
            print(f"  {r[1]}: {r[2]:,.0f}đ (SL: {r[3]})")
    elif chon == "0":
        break
```

---

## Bài Tập Về Nhà

### Bài 1: Sổ liên lạc với database
Chuyển ứng dụng danh bạ (buổi 6) sang dùng SQLite thay vì file text

### Bài 2: Quản lý thư viện
Database với bảng `sach`: id, ten, tac_gia, nam_xb, dang_muon
- CRUD đầy đủ + tìm kiếm theo tên/tác giả

---

## Tóm tắt buổi học
- **SQLite**: Database nhẹ, lưu trong 1 file, Python có sẵn
- **SQL**: CREATE TABLE, INSERT, SELECT, UPDATE, DELETE
- **Dùng `?`**: Tránh SQL injection, an toàn hơn
- **Buổi sau**: API cơ bản - gọi API, xử lý JSON
