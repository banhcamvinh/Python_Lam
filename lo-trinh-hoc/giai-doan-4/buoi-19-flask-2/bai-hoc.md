# Buổi 19: Web App Với Flask (Phần 2)

## Mục tiêu buổi học
- Kết nối Flask với SQLite database
- Tạo hệ thống đăng nhập đơn giản
- Biết cách deploy (triển khai) web app

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-25 phút | Flask + SQLite |
| 25-45 phút | Hệ thống đăng nhập (session) |
| 45-60 phút | Deploy cơ bản |
| 60-80 phút | Thực hành hoàn thiện |
| 80-90 phút | Bài tập + chuẩn bị đồ án |

---

## Phần 1: Flask + SQLite (20 phút)

### Kết nối database

```python
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB = "web_app.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row  # Truy cập cột bằng tên
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sinh_vien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten TEXT NOT NULL,
            email TEXT,
            diem REAL
        )
    """)
    conn.commit()
    conn.close()

init_db()
```

### CRUD qua web

```python
@app.route("/")
def index():
    conn = get_db()
    ds = conn.execute("SELECT * FROM sinh_vien ORDER BY ten").fetchall()
    conn.close()
    return render_template("index.html", sinh_vien=ds)

@app.route("/them", methods=["GET", "POST"])
def them():
    if request.method == "POST":
        ten = request.form["ten"]
        email = request.form["email"]
        diem = float(request.form["diem"])

        conn = get_db()
        conn.execute("INSERT INTO sinh_vien (ten, email, diem) VALUES (?,?,?)",
                     (ten, email, diem))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("them.html")

@app.route("/xoa/<int:id>")
def xoa(id):
    conn = get_db()
    conn.execute("DELETE FROM sinh_vien WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))
```

---

## Phần 2: Hệ Thống Đăng Nhập (20 phút)

### Session trong Flask

```python
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "khoa_bi_mat_cua_ban"  # Cần cho session

# Tài khoản đơn giản (thực tế nên lưu trong DB + mã hóa)
USERS = {
    "admin": "123456",
    "giaovien": "python2026"
}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USERS and USERS[username] == password:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", loi="Sai tài khoản hoặc mật khẩu!")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# Kiểm tra đăng nhập
def can_dang_nhap(f):
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

@app.route("/")
@can_dang_nhap
def index():
    return render_template("index.html", user=session["user"])
```

```html
<!-- templates/login.html -->
{% extends "base.html" %}
{% block content %}
<h1>🔐 Đăng nhập</h1>
{% if loi %}
    <p style="color: red;">{{ loi }}</p>
{% endif %}
<form method="POST">
    <p>Username: <input type="text" name="username" required></p>
    <p>Password: <input type="password" name="password" required></p>
    <button type="submit">Đăng nhập</button>
</form>
{% endblock %}
```

---

## Phần 3: Deploy Cơ Bản (15 phút)

### Chuẩn bị deploy

```bash
# Tạo file requirements.txt
pip freeze > requirements.txt

# File chạy chính
# Procfile (cho Render/Heroku)
web: python app.py
```

### Các nền tảng deploy miễn phí
1. **PythonAnywhere** - Dễ nhất cho người mới
2. **Render** - Miễn phí, tự động deploy từ GitHub
3. **Railway** - Đơn giản, hỗ trợ database

### Deploy lên PythonAnywhere (hướng dẫn nhanh)
1. Đăng ký tài khoản tại pythonanywhere.com
2. Upload code lên
3. Cấu hình web app → chọn Flask
4. Chỉ đường dẫn đến file app.py
5. Reload → Web app online!

---

## Phần 4: Thực Hành (20 phút)

### Hoàn thiện web app quản lý sinh viên
Kết hợp tất cả: Flask + SQLite + Login + Template đẹp

(Sinh viên hoàn thiện project dưới hướng dẫn)

---

## Bài Tập Về Nhà: Chuẩn Bị Đồ Án

### Chọn đề tài đồ án cuối khóa
Gợi ý đề tài:
1. **Web quản lý chi tiêu** - Nhập thu/chi, thống kê theo tháng
2. **App quiz online** - Tạo câu hỏi, làm bài, xem điểm
3. **Web blog cá nhân** - Viết bài, bình luận, đăng nhập
4. **Quản lý thư viện** - Mượn/trả sách, tìm kiếm
5. **App đặt đồ ăn** - Menu, giỏ hàng, đặt hàng
6. **Tự chọn đề tài** - Thầy/cô duyệt

### Yêu cầu đồ án
- Có giao diện (Tkinter hoặc Flask)
- Có database (SQLite)
- Có ít nhất 3 chức năng CRUD
- Code có cấu trúc rõ ràng (dùng class/function)
- Có file README mô tả project

---

## Tóm tắt buổi học
- **Flask + SQLite**: CRUD đầy đủ qua web
- **Session**: Quản lý đăng nhập/đăng xuất
- **Deploy**: Đưa web app lên internet
- **Buổi sau**: Đồ án cuối khóa - trình bày sản phẩm
