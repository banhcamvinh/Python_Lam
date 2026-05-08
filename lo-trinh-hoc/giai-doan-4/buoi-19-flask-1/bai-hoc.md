# Buổi 19: Web App Với Flask (Phần 1)

## Mục tiêu buổi học
- Hiểu web app hoạt động thế nào (client-server)
- Cài đặt và tạo app Flask đầu tiên
- Biết cách tạo route, template HTML, xử lý form

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Web hoạt động thế nào? |
| 5-20 phút | Flask cơ bản, route |
| 20-40 phút | Template HTML với Jinja2 |
| 40-55 phút | Form và xử lý dữ liệu |
| 55-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Phần 1: Flask Cơ Bản (15 phút)

### Cài đặt

```bash
pip install flask
```

### App đầu tiên

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def trang_chu():
    return "<h1>Xin chào! 👋</h1><p>Đây là web app đầu tiên</p>"

@app.route("/about")
def gioi_thieu():
    return "<h1>Giới thiệu</h1><p>App được viết bằng Flask + Python</p>"

if __name__ == "__main__":
    app.run(debug=True)
```

Chạy: `python app.py` → Mở trình duyệt: `http://127.0.0.1:5000`

### Route với tham số

```python
@app.route("/chao/<ten>")
def chao(ten):
    return f"<h1>Xin chào {ten}! 👋</h1>"

# Truy cập: /chao/Minh → "Xin chào Minh!"
```

---

## Phần 2: Template HTML (20 phút)

### Cấu trúc thư mục

```
my_app/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── about.html
└── static/
    └── style.css
```

### Template cơ bản (Jinja2)

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}App{% endblock %}</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 0 auto; padding: 20px; }
        nav { background: #2196F3; padding: 10px; margin-bottom: 20px; }
        nav a { color: white; margin-right: 15px; text-decoration: none; }
    </style>
</head>
<body>
    <nav>
        <a href="/">🏠 Trang chủ</a>
        <a href="/sinh-vien">📋 Sinh viên</a>
    </nav>
    {% block content %}{% endblock %}
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}
{% block title %}Trang chủ{% endblock %}
{% block content %}
    <h1>Xin chào! 👋</h1>
    <p>Đây là web app quản lý sinh viên</p>
{% endblock %}
```

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def trang_chu():
    return render_template("index.html")
```

### Truyền dữ liệu vào template

```python
@app.route("/sinh-vien")
def danh_sach_sv():
    sinh_vien = [
        {"ten": "Minh", "diem": 8.5},
        {"ten": "Lan", "diem": 7.0},
        {"ten": "Hùng", "diem": 9.2},
    ]
    return render_template("sinh_vien.html", ds=sinh_vien)
```

```html
<!-- templates/sinh_vien.html -->
{% extends "base.html" %}
{% block content %}
    <h1>📋 Danh sách sinh viên</h1>
    <table border="1" cellpadding="8">
        <tr><th>STT</th><th>Tên</th><th>Điểm</th></tr>
        {% for sv in ds %}
        <tr>
            <td>{{ loop.index }}</td>
            <td>{{ sv.ten }}</td>
            <td>{{ sv.diem }}</td>
        </tr>
        {% endfor %}
    </table>
    <p>Tổng: {{ ds|length }} sinh viên</p>
{% endblock %}
```

---

## Phần 3: Form & Xử Lý Dữ Liệu (15 phút)

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
sinh_vien = []  # Tạm lưu trong list

@app.route("/them", methods=["GET", "POST"])
def them_sv():
    if request.method == "POST":
        ten = request.form["ten"]
        diem = float(request.form["diem"])
        sinh_vien.append({"ten": ten, "diem": diem})
        return redirect(url_for("danh_sach_sv"))

    return render_template("them.html")
```

```html
<!-- templates/them.html -->
{% extends "base.html" %}
{% block content %}
    <h1>➕ Thêm sinh viên</h1>
    <form method="POST">
        <p>Tên: <input type="text" name="ten" required></p>
        <p>Điểm: <input type="number" name="diem" step="0.1" required></p>
        <button type="submit">Thêm</button>
    </form>
{% endblock %}
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (25 phút)

### Bài thực hành: Web app Todo List
Tạo web app todo list đơn giản với Flask:
- Trang chủ: hiển thị danh sách todo
- Form thêm todo mới
- Nút xóa todo

(Sinh viên code theo hướng dẫn của giảng viên)

---

## Bài Tập Về Nhà

### Bài 1: Trang web cá nhân
Tạo web cá nhân với Flask: trang chủ, giới thiệu, liên hệ

### Bài 2: Web quản lý ghi chú
Chuyển sổ ghi chú sang web app với Flask

---

## Tóm tắt buổi học
- **Flask**: Framework web nhẹ cho Python
- **Route**: Định nghĩa URL → hàm xử lý
- **Template**: HTML + Jinja2 để hiển thị dữ liệu
- **Form**: Nhận dữ liệu từ người dùng qua POST
- **Buổi sau**: Flask phần 2 - Database, Login, Deploy
