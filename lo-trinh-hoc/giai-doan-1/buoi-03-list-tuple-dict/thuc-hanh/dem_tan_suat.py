# === BÀI THỰC HÀNH: ĐẾM TẦN SUẤT TỪ ===

cau = input("Nhập một câu: ")
cac_tu = cau.lower().split()

# Đếm bằng dictionary
tan_suat = {}
for tu in cac_tu:
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

# Hiển thị kết quả
print(f"\nCâu: \"{cau}\"")
print(f"Tổng số từ: {len(cac_tu)}")
print(f"Số từ khác nhau: {len(tan_suat)}")

print("\nTần suất:")
for tu, dem in tan_suat.items():
    thanh = "█" * dem
    print(f"  '{tu}': {dem} lần {thanh}")
