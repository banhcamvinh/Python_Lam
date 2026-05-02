# === BÀI THỰC HÀNH: QUẢN LÝ SẢN PHẨM VỚI SQLITE ===
import sqlite3

DB = "cua_hang.db"


def tao_bang():
    conn = sqlite3.connect(DB)
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
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO san_pham (ten, gia, so_luong) VALUES (?, ?, ?)",
                 (ten, gia, so_luong))
    conn.commit()
    conn.close()
    print(f"✅ Đã thêm {ten}")


def xem_sp():
    conn = sqlite3.connect(DB)
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
    tong = sum(r[2] * r[3] for r in rows)
    print(f"  Tổng giá trị kho: {tong:,.0f}đ")


def tim_sp(tu_khoa):
    conn = sqlite3.connect(DB)
    rows = conn.execute("SELECT * FROM san_pham WHERE ten LIKE ?",
                        (f"%{tu_khoa}%",)).fetchall()
    conn.close()
    if not rows:
        print(f"🔍 Không tìm thấy '{tu_khoa}'")
    else:
        for r in rows:
            print(f"  {r[1]}: {r[2]:,.0f}đ (SL: {r[3]})")


# Chương trình chính
tao_bang()

while True:
    print("\n=== 🏪 CỬA HÀNG ===")
    print("1. Thêm SP  2. Xem kho  3. Tìm  0. Thoát")
    chon = input("Chọn: ")

    if chon == "1":
        ten = input("Tên SP: ")
        try:
            gia = float(input("Giá: "))
            sl = int(input("Số lượng: "))
            them_sp(ten, gia, sl)
        except ValueError:
            print("⚠️ Nhập số!")
    elif chon == "2":
        xem_sp()
    elif chon == "3":
        tim_sp(input("Tìm: "))
    elif chon == "0":
        print("Tạm biệt! 👋")
        break
