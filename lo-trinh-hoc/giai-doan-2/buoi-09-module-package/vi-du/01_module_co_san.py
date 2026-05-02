# === BUỔI 9: MODULE CÓ SẴN ===

# --- math ---
import math
print("--- math ---")
print(f"Pi: {math.pi:.4f}")
print(f"sqrt(144): {math.sqrt(144)}")
print(f"ceil(4.2): {math.ceil(4.2)}")
print(f"floor(4.8): {math.floor(4.8)}")

# --- random ---
import random
print("\n--- random ---")
print(f"Số ngẫu nhiên 1-100: {random.randint(1, 100)}")
print(f"Chọn ngẫu nhiên: {random.choice(['Toán', 'Lý', 'Hóa'])}")

ds = [1, 2, 3, 4, 5]
random.shuffle(ds)
print(f"Xáo trộn: {ds}")

# --- datetime ---
from datetime import datetime, date
print("\n--- datetime ---")
print(f"Bây giờ: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

ngay_sinh = date(2005, 8, 15)
tuoi = (date.today() - ngay_sinh).days // 365
print(f"Sinh 15/08/2005 -> Tuổi: {tuoi}")

# --- os ---
import os
print("\n--- os ---")
print(f"Thư mục hiện tại: {os.getcwd()}")

# --- json ---
import json
print("\n--- json ---")
du_lieu = {"ten": "Minh", "tuoi": 18, "mon": ["Toán", "Tin"]}
json_str = json.dumps(du_lieu, ensure_ascii=False, indent=2)
print(f"JSON:\n{json_str}")

# Đọc lại từ JSON string
doc_lai = json.loads(json_str)
print(f"\nĐọc lại: {doc_lai['ten']}, {doc_lai['tuoi']} tuổi")
