# === BUỔI 2: XỬ LÝ CHUỖI ===

# --- Truy cập ký tự ---
text = "Hello Python"
print(f"Chuỗi: '{text}'")
print(f"Ký tự đầu: text[0] = '{text[0]}'")
print(f"Ký tự cuối: text[-1] = '{text[-1]}'")
print(f"Độ dài: len(text) = {len(text)}")

# --- Cắt chuỗi (slicing) ---
print(f"\n--- Cắt chuỗi ---")
print(f"text[0:5]  = '{text[0:5]}'")    # Hello
print(f"text[6:]   = '{text[6:]}'")      # Python
print(f"text[:5]   = '{text[:5]}'")      # Hello
print(f"text[::2]  = '{text[::2]}'")     # HloPto (lấy cách 1)
print(f"text[::-1] = '{text[::-1]}'")    # nohtyP olleH (đảo ngược)

# --- Phương thức chuỗi ---
ten = "  nguyễn văn minh  "
print(f"\n--- Phương thức chuỗi ---")
print(f"Gốc:    '{ten}'")
print(f"strip:  '{ten.strip()}'")
print(f"upper:  '{ten.strip().upper()}'")
print(f"lower:  '{ten.strip().lower()}'")
print(f"title:  '{ten.strip().title()}'")

# --- Tìm kiếm và thay thế ---
cau = "Tôi yêu lập trình Python, Python rất hay"
print(f"\n--- Tìm kiếm ---")
print(f"Câu: '{cau}'")
print(f"'Python' in cau: {'Python' in cau}")
print(f"cau.count('Python'): {cau.count('Python')}")
print(f"cau.find('Python'): {cau.find('Python')}")
print(f"cau.replace('Python', 'Java'): '{cau.replace('Python', 'Java')}'")

# --- Tách và nối ---
print(f"\n--- Tách và nối ---")
ho_ten = "Nguyễn Văn Minh"
cac_tu = ho_ten.split(" ")
print(f"split: {cac_tu}")
print(f"Họ: {cac_tu[0]}")
print(f"Tên: {cac_tu[-1]}")

tu = ["Xin", "chào", "các", "bạn"]
print(f"join(' '): '{' '.join(tu)}'")
print(f"join('-'): '{'-'.join(tu)}'")

# --- Kiểm tra ký tự ---
print(f"\n--- Kiểm tra ký tự ---")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")     # True - toàn chữ
print(f"'123'.isdigit(): {'123'.isdigit()}")     # True - toàn số
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")  # True - chữ hoặc số
print(f"'ABC'.isupper(): {'ABC'.isupper()}")     # True - toàn hoa
print(f"'abc'.islower(): {'abc'.islower()}")     # True - toàn thường
