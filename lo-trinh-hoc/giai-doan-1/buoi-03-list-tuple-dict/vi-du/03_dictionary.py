# === BUỔI 3: DICTIONARY (TỪ ĐIỂN) ===

# --- Tạo dictionary ---
sinh_vien = {
    "ten": "Nguyễn Văn Minh",
    "tuoi": 18,
    "lop": "CNTT01",
    "diem_tb": 8.5
}

print("--- Thông tin sinh viên ---")
for key, value in sinh_vien.items():
    print(f"  {key}: {value}")

# --- Truy cập ---
print(f"\nTên: {sinh_vien['ten']}")
print(f"Tuổi: {sinh_vien['tuoi']}")
print(f"Email: {sinh_vien.get('email', 'Chưa có')}")  # An toàn

# --- Thêm, sửa, xóa ---
print("\n--- Thêm/Sửa/Xóa ---")
sinh_vien["email"] = "minh@gmail.com"  # Thêm
sinh_vien["tuoi"] = 19                  # Sửa
print(f"Sau thêm email và sửa tuổi: {sinh_vien}")

del sinh_vien["lop"]                    # Xóa
print(f"Sau xóa lớp: {sinh_vien}")

# --- Kiểm tra key ---
print(f"\n'ten' có trong dict? {'ten' in sinh_vien}")
print(f"'lop' có trong dict? {'lop' in sinh_vien}")

# --- List chứa Dictionary (rất phổ biến!) ---
print("\n--- Danh bạ ---")
danh_ba = [
    {"ten": "Minh", "sdt": "0901234567"},
    {"ten": "Lan", "sdt": "0912345678"},
    {"ten": "Hùng", "sdt": "0923456789"},
]

for i, nguoi in enumerate(danh_ba):
    print(f"  {i + 1}. {nguoi['ten']}: {nguoi['sdt']}")

# Thêm liên hệ mới
danh_ba.append({"ten": "Trang", "sdt": "0934567890"})
print(f"\nSau khi thêm Trang, có {len(danh_ba)} liên hệ")
