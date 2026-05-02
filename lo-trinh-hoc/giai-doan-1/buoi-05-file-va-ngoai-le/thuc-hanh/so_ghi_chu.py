# === BÀI THỰC HÀNH: SỔ GHI CHÚ ===
import os

FILE_GHI_CHU = "ghi_chu.txt"

def xem_ghi_chu():
    """Đọc và hiển thị tất cả ghi chú"""
    if not os.path.exists(FILE_GHI_CHU):
        print("📝 Chưa có ghi chú nào!")
        return

    with open(FILE_GHI_CHU, "r", encoding="utf-8") as f:
        cac_dong = f.readlines()

    if len(cac_dong) == 0:
        print("📝 Chưa có ghi chú nào!")
        return

    print(f"\n📋 Có {len(cac_dong)} ghi chú:")
    for i, dong in enumerate(cac_dong):
        print(f"  {i + 1}. {dong.strip()}")

def them_ghi_chu():
    """Thêm ghi chú mới"""
    noi_dung = input("Nhập ghi chú: ")
    with open(FILE_GHI_CHU, "a", encoding="utf-8") as f:
        f.write(noi_dung + "\n")
    print("✅ Đã thêm ghi chú!")

def xoa_ghi_chu():
    """Xóa một ghi chú theo số thứ tự"""
    xem_ghi_chu()

    try:
        with open(FILE_GHI_CHU, "r", encoding="utf-8") as f:
            cac_dong = f.readlines()
    except FileNotFoundError:
        return

    if len(cac_dong) == 0:
        return

    try:
        stt = int(input("Nhập STT cần xóa: "))
        if 1 <= stt <= len(cac_dong):
            da_xoa = cac_dong.pop(stt - 1)
            with open(FILE_GHI_CHU, "w", encoding="utf-8") as f:
                f.writelines(cac_dong)
            print(f"🗑️ Đã xóa: {da_xoa.strip()}")
        else:
            print("⚠️ STT không hợp lệ!")
    except ValueError:
        print("⚠️ Vui lòng nhập số!")

# Chương trình chính
while True:
    print("\n=== SỔ GHI CHÚ ===")
    print("1. Xem ghi chú")
    print("2. Thêm ghi chú")
    print("3. Xóa ghi chú")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        xem_ghi_chu()
    elif chon == "2":
        them_ghi_chu()
    elif chon == "3":
        xoa_ghi_chu()
    elif chon == "0":
        print("Tạm biệt! 👋")
        break
    else:
        print("⚠️ Lựa chọn không hợp lệ!")
