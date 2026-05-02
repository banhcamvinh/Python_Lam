# === BÀI THỰC HÀNH: TRÒ CHƠI ĐOÁN SỐ ===
import random

so_bi_mat = random.randint(1, 100)
so_lan_doan = 0

print("=" * 30)
print("   TRÒ CHƠI ĐOÁN SỐ")
print("=" * 30)
print("Tôi đang nghĩ một số từ 1 đến 100.")
print("Bạn hãy đoán xem đó là số nào!\n")

while True:
    doan = int(input("Nhập số bạn đoán: "))
    so_lan_doan += 1

    if doan < so_bi_mat:
        print("📈 Lớn hơn đi!\n")
    elif doan > so_bi_mat:
        print("📉 Nhỏ hơn đi!\n")
    else:
        print(f"\n🎉 CHÍNH XÁC! Số bí mật là {so_bi_mat}")
        print(f"Bạn đoán đúng sau {so_lan_doan} lần!\n")
        break

# Đánh giá
if so_lan_doan <= 5:
    print("🌟 Xuất sắc! Bạn có trực giác tốt lắm!")
elif so_lan_doan <= 7:
    print("👍 Giỏi lắm! Chiến thuật tốt!")
elif so_lan_doan <= 10:
    print("😊 Khá ổn! Thử dùng phương pháp chia đôi nhé!")
else:
    print("💪 Cần luyện thêm! Mẹo: luôn đoán số ở giữa khoảng còn lại")
