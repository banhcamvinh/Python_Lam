# === BÀI THỰC HÀNH: ĐẾM NGUYÊN ÂM ===

cau = input("Nhập một câu: ")
nguyen_am = "aeiouAEIOU"
dem = 0

for ky_tu in cau:
    if ky_tu in nguyen_am:
        dem += 1

print(f"\nCâu: \"{cau}\"")
print(f"Tổng số nguyên âm: {dem}")
print(f"Tổng số ký tự: {len(cau)}")

# Chi tiết từng nguyên âm
print("\nChi tiết:")
for na in "aeiou":
    so_lan = cau.lower().count(na)
    if so_lan > 0:
        thanh = "█" * so_lan  # Vẽ biểu đồ đơn giản
        print(f"  '{na}': {so_lan} lần {thanh}")
