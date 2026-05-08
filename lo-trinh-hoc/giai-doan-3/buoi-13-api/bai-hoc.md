# Buổi 13: API Cơ Bản

## Mục tiêu buổi học
- Hiểu API là gì và cách hoạt động
- Biết cách gọi API bằng thư viện requests
- Xử lý dữ liệu JSON từ API
- Xây dựng ứng dụng đơn giản dùng API

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-20 phút | API là gì? HTTP cơ bản |
| 20-40 phút | Thư viện requests |
| 40-55 phút | Xử lý JSON từ API |
| 55-80 phút | Thực hành có hướng dẫn |
| 80-90 phút | Bài tập + giao bài về nhà |

---

## Phần 1: API Là Gì? (15 phút)

### Giải thích đơn giản
API giống như người phục vụ ở nhà hàng:
- Bạn (client) gọi món → Người phục vụ (API) mang yêu cầu vào bếp (server)
- Bếp nấu xong → Người phục vụ mang đồ ăn (dữ liệu) ra cho bạn

### HTTP Methods
- **GET**: Lấy dữ liệu (xem menu)
- **POST**: Gửi dữ liệu mới (đặt món)
- **PUT**: Cập nhật dữ liệu (đổi món)
- **DELETE**: Xóa dữ liệu (hủy món)

### Cài đặt requests

```bash
pip install requests
```

---

## Phần 2: Thư Viện requests (20 phút)

### GET - Lấy dữ liệu

```python
import requests

# Gọi API đơn giản
response = requests.get("https://api.github.com")
print(f"Status code: {response.status_code}")  # 200 = OK
print(f"Dữ liệu: {response.json()}")

# API với tham số
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)
posts = response.json()
print(f"Số bài viết: {len(posts)}")
for post in posts[:3]:
    print(f"  - {post['title']}")
```

### Xử lý lỗi

```python
import requests

def goi_api(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Lỗi nếu status != 200
        return response.json()
    except requests.exceptions.ConnectionError:
        print("❌ Không kết nối được!")
    except requests.exceptions.Timeout:
        print("❌ Hết thời gian chờ!")
    except requests.exceptions.HTTPError as e:
        print(f"❌ Lỗi HTTP: {e}")
    return None
```

---

## Phần 3: Ví Dụ Thực Tế (15 phút)

### Tra cứu thông tin GitHub user

```python
import requests

def tra_cuu_github(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 404:
        print(f"❌ Không tìm thấy user '{username}'")
        return

    if response.status_code != 200:
        print(f"❌ Lỗi: {response.status_code}")
        return

    user = response.json()
    print(f"\n👤 {user['name'] or username}")
    print(f"📍 {user.get('location', 'Không rõ')}")
    print(f"📦 Repos: {user['public_repos']}")
    print(f"👥 Followers: {user['followers']}")
    print(f"🔗 {user['html_url']}")

# Sử dụng
username = input("Nhập GitHub username: ")
tra_cuu_github(username)
```

### Lấy ảnh ngẫu nhiên

```python
import requests

def lay_anh_cho():
    """Lấy ảnh chó ngẫu nhiên từ Dog API"""
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        data = response.json()
        print(f"🐕 Ảnh chó: {data['message']}")
    else:
        print("❌ Không lấy được ảnh")

lay_anh_cho()
```

---

## Phần 4: Thực Hành Có Hướng Dẫn (25 phút)

### Bài thực hành: App tra cứu từ điển

```python
import requests

def tra_tu(tu):
    """Tra từ điển tiếng Anh dùng Free Dictionary API"""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{tu}"
    response = requests.get(url)

    if response.status_code == 404:
        print(f"❌ Không tìm thấy từ '{tu}'")
        return

    data = response.json()[0]
    print(f"\n📖 {data['word']}")

    if "phonetic" in data:
        print(f"🔊 Phát âm: {data['phonetic']}")

    for meaning in data.get("meanings", []):
        loai_tu = meaning["partOfSpeech"]
        print(f"\n  [{loai_tu}]")
        for i, defn in enumerate(meaning["definitions"][:3]):
            print(f"    {i + 1}. {defn['definition']}")
            if "example" in defn:
                print(f"       Ví dụ: {defn['example']}")

# Chương trình chính
print("=== 📖 TỪ ĐIỂN ANH-ANH ===")
print("Nhập 'q' để thoát\n")

while True:
    tu = input("Nhập từ cần tra: ").strip()
    if tu.lower() == "q":
        break
    if tu:
        tra_tu(tu)
```

---

## Bài Tập Về Nhà

### Bài 1: Tra cứu tỷ giá
Dùng API tỷ giá (exchangerate-api.com) để tra cứu tỷ giá USD, EUR, JPY sang VND

### Bài 2: App tin tức
Dùng NewsAPI để lấy tin tức mới nhất theo chủ đề

---

## Tóm tắt buổi học
- **API**: Cầu nối giữa ứng dụng và server
- **requests**: Thư viện Python gọi API
- **GET**: Lấy dữ liệu, **POST**: Gửi dữ liệu
- **JSON**: Định dạng dữ liệu phổ biến nhất từ API
- **Buổi sau**: Xử lý dữ liệu nâng cao
