# === BÀI THỰC HÀNH: KIỂM TRA MẬT KHẨU ===

def kiem_tra_do_dai(mat_khau, toi_thieu=8):
    """Kiểm tra mật khẩu có đủ dài không"""
    return len(mat_khau) >= toi_thieu

def co_chu_hoa(mat_khau):
    """Kiểm tra có ít nhất 1 chữ hoa"""
    for ky_tu in mat_khau:
        if ky_tu.isupper():
            return True
    return False

def co_chu_thuong(mat_khau):
    """Kiểm tra có ít nhất 1 chữ thường"""
    for ky_tu in mat_khau:
        if ky_tu.islower():
            return True
    return False

def co_so(mat_khau):
    """Kiểm tra có ít nhất 1 chữ số"""
    for ky_tu in mat_khau:
        if ky_tu.isdigit():
            return True
    return False

def danh_gia_mat_khau(mat_khau):
    """Đánh giá độ mạnh, trả về (điểm, danh sách nhận xét)"""
    diem = 0
    nhan_xet = []

    if kiem_tra_do_dai(mat_khau):
        diem += 1
    else:
        nhan_xet.append("❌ Cần ít nhất 8 ký tự")

    if co_chu_hoa(mat_khau):
        diem += 1
    else:
        nhan_xet.append("❌ Cần ít nhất 1 chữ hoa")

    if co_chu_thuong(mat_khau):
        diem += 1
    else:
        nhan_xet.append("❌ Cần ít nhất 1 chữ thường")

    if co_so(mat_khau):
        diem += 1
    else:
        nhan_xet.append("❌ Cần ít nhất 1 chữ số")

    return diem, nhan_xet

# Chương trình chính
mk = input("Nhập mật khẩu: ")
diem, nhan_xet = danh_gia_mat_khau(mk)

print(f"\nĐộ mạnh: {diem}/4 {'🟢' * diem}{'⚪' * (4 - diem)}")

if diem == 4:
    print("✅ Mật khẩu mạnh!")
else:
    print("Cần cải thiện:")
    for nx in nhan_xet:
        print(f"  {nx}")
