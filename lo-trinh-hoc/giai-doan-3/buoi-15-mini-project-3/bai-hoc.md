# Buổi 15: Mini Project 3 - App Tra Cứu Thời Tiết

## Mục tiêu buổi học
- Tổng hợp kiến thức Giai đoạn 3: SQLite, API, xử lý dữ liệu
- Xây dựng app tra cứu thời tiết dùng API + lưu lịch sử vào database
- Rèn kỹ năng kết hợp nhiều thành phần

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-10 phút | Phân tích yêu cầu, đăng ký API key |
| 10-30 phút | Code gọi API thời tiết |
| 30-50 phút | Code lưu lịch sử vào SQLite |
| 50-75 phút | Hoàn thiện menu và test |
| 75-90 phút | Review, gợi ý cải tiến |

---

## Yêu Cầu Ứng Dụng

### Chức năng
1. Tra cứu thời tiết theo tên thành phố
2. Hiển thị: nhiệt độ, độ ẩm, mô tả, tốc độ gió
3. Lưu lịch sử tra cứu vào SQLite
4. Xem lịch sử tra cứu

### API sử dụng
- OpenWeatherMap (miễn phí): https://openweathermap.org/api
- Đăng ký lấy API key miễn phí

---

## Code Hoàn Chỉnh

```python
import requests
import sqlite3
from datetime import datetime

API_KEY = "YOUR_API_KEY"  # Thay bằng API key của bạn
DB_FILE = "thoi_tiet.db"

# === DATABASE ===
def tao_database():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS lich_su (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thanh_pho TEXT,
            nhiet_do REAL,
            do_am INTEGER,
            mo_ta TEXT,
            thoi_gian TEXT
        )
    """)
    conn.commit()
    conn.close()

def luu_lich_su(thanh_pho, nhiet_do, do_am, mo_ta):
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT INTO lich_su (thanh_pho, nhiet_do, do_am, mo_ta, thoi_gian) "
        "VALUES (?, ?, ?, ?, ?)",
        (thanh_pho, nhiet_do, do_am, mo_ta,
         datetime.now().strftime("%d/%m/%Y %H:%M"))
    )
    conn.commit()
    conn.close()

def xem_lich_su():
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute(
        "SELECT * FROM lich_su ORDER BY id DESC LIMIT 10"
    ).fetchall()
    conn.close()

    if not rows:
        print("📭 Chưa có lịch sử tra cứu!")
        return

    print(f"\n📋 Lịch sử tra cứu (10 gần nhất):")
    print("-" * 60)
    for row in rows:
        print(f"  {row[5]} | {row[1]:<15} | {row[2]}°C | {row[4]}")
    print("-" * 60)

# === API ===
def tra_cuu_thoi_tiet(thanh_pho):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": thanh_pho,
        "appid": API_KEY,
        "units": "metric",      # Độ C
        "lang": "vi"             # Tiếng Việt
    }

    try:
        response = requests.get(url, params=params, timeout=5)
    except requests.exceptions.ConnectionError:
        print("❌ Không có kết nối mạng!")
        return

    if response.status_code == 404:
        print(f"❌ Không tìm thấy thành phố '{thanh_pho}'")
        return

    if response.status_code == 401:
        print("❌ API key không hợp lệ!")
        return

    if response.status_code != 200:
        print(f"❌ Lỗi: {response.status_code}")
        return

    data = response.json()
    nhiet_do = data["main"]["temp"]
    cam_giac = data["main"]["feels_like"]
    do_am = data["main"]["humidity"]
    mo_ta = data["weather"][0]["description"]
    gio = data["wind"]["speed"]
    ten_tp = data["name"]

    print(f"\n🌤️  Thời tiết tại {ten_tp}")
    print(f"{'=' * 35}")
    print(f"  🌡️  Nhiệt độ: {nhiet_do}°C (cảm giác {cam_giac}°C)")
    print(f"  💧 Độ ẩm: {do_am}%")
    print(f"  ☁️  Mô tả: {mo_ta}")
    print(f"  💨 Gió: {gio} m/s")

    # Lưu lịch sử
    luu_lich_su(ten_tp, nhiet_do, do_am, mo_ta)

# === CHƯƠNG TRÌNH CHÍNH ===
def main():
    tao_database()

    print("=" * 35)
    print("   🌤️  APP THỜI TIẾT")
    print("=" * 35)

    while True:
        print("\n1. 🔍 Tra cứu thời tiết")
        print("2. 📋 Xem lịch sử")
        print("0. 🚪 Thoát")

        chon = input("\nChọn: ")

        if chon == "1":
            tp = input("Nhập tên thành phố: ").strip()
            if tp:
                tra_cuu_thoi_tiet(tp)
        elif chon == "2":
            xem_lich_su()
        elif chon == "0":
            print("Tạm biệt! 👋")
            break

main()
```

---

## Gợi Ý Cải Tiến (Bài Tập Về Nhà)

### Mức 1
- Thêm tra cứu dự báo 5 ngày tới
- Hiển thị icon thời tiết bằng emoji phù hợp

### Mức 2
- So sánh thời tiết 2 thành phố
- Thống kê từ lịch sử: thành phố tra nhiều nhất, nhiệt độ TB

### Mức 3
- Thêm chức năng yêu thích (lưu danh sách TP hay tra)
- Tự động tra cứu các TP yêu thích

---

## Tóm tắt Giai đoạn 3
- **SQLite**: Lưu trữ dữ liệu có cấu trúc, truy vấn nhanh
- **API**: Lấy dữ liệu từ internet (thời tiết, tin tức, dịch thuật...)
- **Xử lý dữ liệu**: Comprehension, lambda, map/filter
- **Giai đoạn 4**: Xây dựng ứng dụng có giao diện (Tkinter + Flask)
