# === BÀI THỰC HÀNH: KIỂM TRA NĂM NHUẬN ===
# Quy tắc:
# - Chia hết cho 400 -> năm nhuận
# - Chia hết cho 100 (nhưng không chia hết 400) -> KHÔNG phải
# - Chia hết cho 4 -> năm nhuận
# - Còn lại -> KHÔNG phải

nam = int(input("Nhập năm cần kiểm tra: "))

if nam % 400 == 0:
    print(f"{nam} là năm nhuận ✅")
elif nam % 100 == 0:
    print(f"{nam} KHÔNG phải năm nhuận ❌")
elif nam % 4 == 0:
    print(f"{nam} là năm nhuận ✅")
else:
    print(f"{nam} KHÔNG phải năm nhuận ❌")

# Thử với các năm: 2000, 1900, 2024, 2025
