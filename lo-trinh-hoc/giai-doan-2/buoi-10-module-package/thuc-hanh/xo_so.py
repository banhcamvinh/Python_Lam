# === BÀI THỰC HÀNH: XỔ SỐ PYTHON ===
import random
from datetime import datetime


def tao_ve_so():
    """Tạo vé số ngẫu nhiên 6 số (1-45)"""
    return sorted(random.sample(range(1, 46), 6))


def kiem_tra_trung(ve_cua_ban, ve_trung):
    """Đếm số trùng khớp"""
    trung = []
    for so in ve_cua_ban:
        if so in ve_trung:
            trung.append(so)
    return trung


def tinh_giai_thuong(so_trung):
    """Tính giải thưởng"""
    giai = {
        6: "JACKPOT - 10,000,000,000đ 🎉🎉🎉",
        5: "Giải nhất - 100,000,000đ 🎉",
        4: "Giải nhì - 10,000,000đ",
        3: "Giải ba - 500,000đ",
        2: "Giải khuyến khích - 50,000đ",
    }
    return giai.get(so_trung, "Không trúng 😢")


# Chương trình chính
print("=" * 40)
print("   🎰 XỔ SỐ PYTHON")
print(f"   {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print("=" * 40)

ket_qua = tao_ve_so()

print("\nChọn 6 số từ 1 đến 45:")
ve_cua_ban = []
for i in range(6):
    while True:
        try:
            so = int(input(f"  Số thứ {i + 1}: "))
            if 1 <= so <= 45 and so not in ve_cua_ban:
                ve_cua_ban.append(so)
                break
            else:
                print("  ⚠️ Số không hợp lệ hoặc đã chọn!")
        except ValueError:
            print("  ⚠️ Nhập số!")

ve_cua_ban.sort()

print(f"\n🎱 Kết quả: {ket_qua}")
print(f"🎫 Vé bạn:  {ve_cua_ban}")

trung = kiem_tra_trung(ve_cua_ban, ket_qua)
print(f"\n✨ Trùng: {trung} ({len(trung)} số)")
print(f"🏆 {tinh_giai_thuong(len(trung))}")
