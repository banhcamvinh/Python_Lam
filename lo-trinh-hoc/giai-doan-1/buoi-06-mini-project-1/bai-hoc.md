# Buổi 6: Mini Project 1 - Quản Lý Danh Bạ

## Mục tiêu buổi học
- Tổng hợp kiến thức Giai đoạn 1: biến, vòng lặp, list, dict, hàm, file, try/except
- Xây dựng ứng dụng console hoàn chỉnh từ đầu đến cuối
- Rèn tư duy chia nhỏ bài toán thành các hàm

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-10 phút | Phân tích yêu cầu, thiết kế chương trình |
| 10-25 phút | Code phần lưu/đọc file |
| 25-50 phút | Code các chức năng chính |
| 50-75 phút | Hoàn thiện và test |
| 75-90 phút | Review code, gợi ý cải tiến |

---

## Yêu Cầu Ứng Dụng

### Chức năng
1. Xem danh bạ (hiển thị tất cả liên hệ)
2. Thêm liên hệ mới (tên + số điện thoại)
3. Tìm kiếm theo tên
4. Xóa liên hệ
5. Dữ liệu được lưu vào file (không mất khi tắt chương trình)

### Phân tích thiết kế

```
Cấu trúc dữ liệu:
- Mỗi liên hệ: {"ten": "...", "sdt": "..."}
- Danh bạ: list chứa các dictionary
- Lưu file: mỗi dòng "tên,số_điện_thoại"

Các hàm cần viết:
- doc_danh_ba()      -> đọc từ file, trả về list
- luu_danh_ba(ds)    -> ghi list ra file
- hien_thi(ds)       -> in danh bạ ra màn hình
- them_lien_he(ds)   -> thêm liên hệ mới
- tim_kiem(ds)       -> tìm theo tên
- xoa_lien_he(ds)    -> xóa theo tên
```

---

## Hướng Dẫn Từng Bước

### Bước 1: Đọc/ghi file

```python
FILE_DANH_BA = "danh_ba.txt"

def doc_danh_ba():
    """Đọc danh bạ từ file, trả về list"""
    danh_ba = []
    try:
        with open(FILE_DANH_BA, "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()
                if dong:  # Bỏ qua dòng trống
                    ten, sdt = dong.split(",")
                    danh_ba.append({"ten": ten, "sdt": sdt})
    except FileNotFoundError:
        pass  # File chưa tồn tại, trả về list rỗng
    return danh_ba

def luu_danh_ba(danh_ba):
    """Ghi danh bạ ra file"""
    with open(FILE_DANH_BA, "w", encoding="utf-8") as f:
        for lh in danh_ba:
            f.write(f"{lh['ten']},{lh['sdt']}\n")
```

### Bước 2: Hiển thị danh bạ

```python
def hien_thi(danh_ba):
    """Hiển thị toàn bộ danh bạ"""
    if len(danh_ba) == 0:
        print("📭 Danh bạ trống!")
        return

    print(f"\n📋 Danh bạ ({len(danh_ba)} liên hệ):")
    print("-" * 35)
    for i, lh in enumerate(danh_ba):
        print(f"  {i + 1}. {lh['ten']:<15} | {lh['sdt']}")
    print("-" * 35)
```

### Bước 3: Thêm liên hệ

```python
def them_lien_he(danh_ba):
    """Thêm liên hệ mới"""
    ten = input("Nhập tên: ").strip()
    if not ten:
        print("⚠️ Tên không được để trống!")
        return

    sdt = input("Nhập SĐT: ").strip()
    if not sdt:
        print("⚠️ SĐT không được để trống!")
        return

    # Kiểm tra trùng tên
    for lh in danh_ba:
        if lh["ten"].lower() == ten.lower():
            print(f"⚠️ '{ten}' đã có trong danh bạ!")
            return

    danh_ba.append({"ten": ten, "sdt": sdt})
    luu_danh_ba(danh_ba)
    print(f"✅ Đã thêm {ten} ({sdt})")
```

### Bước 4: Tìm kiếm

```python
def tim_kiem(danh_ba):
    """Tìm liên hệ theo tên"""
    tu_khoa = input("Nhập tên cần tìm: ").strip().lower()
    ket_qua = []

    for lh in danh_ba:
        if tu_khoa in lh["ten"].lower():
            ket_qua.append(lh)

    if len(ket_qua) == 0:
        print(f"🔍 Không tìm thấy '{tu_khoa}'")
    else:
        print(f"\n🔍 Tìm thấy {len(ket_qua)} kết quả:")
        for lh in ket_qua:
            print(f"  📞 {lh['ten']}: {lh['sdt']}")
```

### Bước 5: Xóa liên hệ

```python
def xoa_lien_he(danh_ba):
    """Xóa liên hệ theo tên"""
    ten = input("Nhập tên cần xóa: ").strip()

    for i, lh in enumerate(danh_ba):
        if lh["ten"].lower() == ten.lower():
            xac_nhan = input(f"Xóa {lh['ten']} ({lh['sdt']})? (c/k): ")
            if xac_nhan.lower() == "c":
                danh_ba.pop(i)
                luu_danh_ba(danh_ba)
                print("🗑️ Đã xóa!")
            else:
                print("Đã hủy.")
            return

    print(f"🔍 Không tìm thấy '{ten}'")
```

### Bước 6: Chương trình chính

```python
def main():
    danh_ba = doc_danh_ba()
    print("=" * 35)
    print("   📱 QUẢN LÝ DANH BẠ")
    print("=" * 35)

    while True:
        print("\n1. 📋 Xem danh bạ")
        print("2. ➕ Thêm liên hệ")
        print("3. 🔍 Tìm kiếm")
        print("4. 🗑️  Xóa liên hệ")
        print("0. 🚪 Thoát")

        chon = input("\nChọn: ")

        if chon == "1":
            hien_thi(danh_ba)
        elif chon == "2":
            them_lien_he(danh_ba)
        elif chon == "3":
            tim_kiem(danh_ba)
        elif chon == "4":
            xoa_lien_he(danh_ba)
        elif chon == "0":
            print("Tạm biệt! 👋")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ!")

main()
```

---

## Gợi Ý Cải Tiến (Bài Tập Về Nhà)

### Mức 1: Cơ bản
- Thêm chức năng sửa liên hệ (đổi tên hoặc SĐT)
- Sắp xếp danh bạ theo tên (A-Z)

### Mức 2: Trung bình
- Thêm trường email cho mỗi liên hệ
- Thêm chức năng nhóm (Gia đình, Bạn bè, Công việc)
- Hiển thị số liên hệ trong mỗi nhóm

### Mức 3: Nâng cao
- Xuất danh bạ ra file CSV đẹp
- Nhập danh bạ từ file CSV
- Thêm chức năng backup (sao lưu) danh bạ

---

## Tóm tắt Giai đoạn 1
Sau 6 buổi, các bạn đã nắm được:
- **Nền tảng**: Biến, kiểu dữ liệu, điều kiện, vòng lặp
- **Cấu trúc dữ liệu**: List, Tuple, Dictionary
- **Hàm**: Chia code thành khối nhỏ, tái sử dụng
- **File & Lỗi**: Lưu trữ dữ liệu, xử lý ngoại lệ
- **Giai đoạn 2**: Lập trình hướng đối tượng (OOP) - cách tổ chức code chuyên nghiệp hơn!
