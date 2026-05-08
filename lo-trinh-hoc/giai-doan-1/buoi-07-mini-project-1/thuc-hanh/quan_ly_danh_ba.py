# === MINI PROJECT 1: QUẢN LÝ DANH BẠ ===

FILE_DANH_BA = "danh_ba.txt"


def doc_danh_ba():
    """Đọc danh bạ từ file, trả về list"""
    danh_ba = []
    try:
        with open(FILE_DANH_BA, "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()
                if dong:
                    ten, sdt = dong.split(",")
                    danh_ba.append({"ten": ten, "sdt": sdt})
    except FileNotFoundError:
        pass
    return danh_ba


def luu_danh_ba(danh_ba):
    """Ghi danh bạ ra file"""
    with open(FILE_DANH_BA, "w", encoding="utf-8") as f:
        for lh in danh_ba:
            f.write(f"{lh['ten']},{lh['sdt']}\n")


def hien_thi(danh_ba):
    """Hiển thị toàn bộ danh bạ"""
    if len(danh_ba) == 0:
        print("📭 Danh bạ trống!")
        return

    print(f"\n📋 Danh bạ ({len(danh_ba)} liên hệ):")
    print("-" * 35)
    for i, lh in enumerate(danh_ba):
        print(f"  {i + 1}. {lh['ten']:<15} | {lh['sdt']}")
    print("-" * 35)


def them_lien_he(danh_ba):
    """Thêm liên hệ mới"""
    ten = input("Nhập tên: ").strip()
    if not ten:
        print("⚠️ Tên không được để trống!")
        return

    sdt = input("Nhập SĐT: ").strip()
    if not sdt:
        print("⚠️ SĐT không được để trống!")
        return

    # Kiểm tra trùng
    for lh in danh_ba:
        if lh["ten"].lower() == ten.lower():
            print(f"⚠️ '{ten}' đã có trong danh bạ!")
            return

    danh_ba.append({"ten": ten, "sdt": sdt})
    luu_danh_ba(danh_ba)
    print(f"✅ Đã thêm {ten} ({sdt})")


def tim_kiem(danh_ba):
    """Tìm liên hệ theo tên"""
    tu_khoa = input("Nhập tên cần tìm: ").strip().lower()
    ket_qua = []

    for lh in danh_ba:
        if tu_khoa in lh["ten"].lower():
            ket_qua.append(lh)

    if len(ket_qua) == 0:
        print(f"🔍 Không tìm thấy '{tu_khoa}'")
    else:
        print(f"\n🔍 Tìm thấy {len(ket_qua)} kết quả:")
        for lh in ket_qua:
            print(f"  📞 {lh['ten']}: {lh['sdt']}")


def xoa_lien_he(danh_ba):
    """Xóa liên hệ theo tên"""
    ten = input("Nhập tên cần xóa: ").strip()

    for i, lh in enumerate(danh_ba):
        if lh["ten"].lower() == ten.lower():
            xac_nhan = input(f"Xóa {lh['ten']} ({lh['sdt']})? (c/k): ")
            if xac_nhan.lower() == "c":
                danh_ba.pop(i)
                luu_danh_ba(danh_ba)
                print("🗑️ Đã xóa!")
            else:
                print("Đã hủy.")
            return

    print(f"🔍 Không tìm thấy '{ten}'")


def main():
    danh_ba = doc_danh_ba()

    print("=" * 35)
    print("   📱 QUẢN LÝ DANH BẠ")
    print("=" * 35)

    while True:
        print("\n1. 📋 Xem danh bạ")
        print("2. ➕ Thêm liên hệ")
        print("3. 🔍 Tìm kiếm")
        print("4. 🗑️  Xóa liên hệ")
        print("0. 🚪 Thoát")

        chon = input("\nChọn: ")

        if chon == "1":
            hien_thi(danh_ba)
        elif chon == "2":
            them_lien_he(danh_ba)
        elif chon == "3":
            tim_kiem(danh_ba)
        elif chon == "4":
            xoa_lien_he(danh_ba)
        elif chon == "0":
            print("Tạm biệt! 👋")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ!")


main()
