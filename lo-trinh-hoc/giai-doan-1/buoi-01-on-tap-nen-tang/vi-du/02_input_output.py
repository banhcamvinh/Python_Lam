# === BUỔI 1: INPUT / OUTPUT ===

# --- Xuất dữ liệu ---
print("Xin chào lớp!")
print("Hôm nay mình ôn lại Python nhé")

# --- f-string: cách in biến tiện nhất ---
ten = "Minh"
tuoi = 18
print(f"Tôi tên {ten}, năm nay {tuoi} tuổi")

# --- Nhập dữ liệu ---
ten_ban = input("Bạn tên gì? ")
tuoi_ban = int(input("Bạn bao nhiêu tuổi? "))

print(f"\nChào {ten_ban}!")
print(f"Năm sinh của bạn khoảng: {2026 - tuoi_ban}")

# --- Format số đẹp ---
gia = 1500000
print(f"\nGiá sản phẩm: {gia:,}đ")       # 1,500,000đ
print(f"Giá sản phẩm: {gia:,.0f}đ")      # 1,500,000đ

pi = 3.14159265
print(f"Pi làm tròn 2 số: {pi:.2f}")      # 3.14
