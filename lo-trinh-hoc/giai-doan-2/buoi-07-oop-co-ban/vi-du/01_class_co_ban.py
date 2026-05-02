# === BUỔI 7: CLASS CƠ BẢN ===

class SinhVien:
    def __init__(self, ten, tuoi, diem):
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem

    def gioi_thieu(self):
        print(f"Xin chào! Tôi là {self.ten}, {self.tuoi} tuổi")

    def xep_loai(self):
        if self.diem >= 8.0:
            return "Giỏi"
        elif self.diem >= 6.5:
            return "Khá"
        elif self.diem >= 5.0:
            return "TB"
        return "Yếu"

    def __str__(self):
        return f"{self.ten} | {self.tuoi} tuổi | Điểm: {self.diem} | {self.xep_loai()}"


# --- Tạo object ---
sv1 = SinhVien("Minh", 18, 8.5)
sv2 = SinhVien("Lan", 19, 6.0)
sv3 = SinhVien("Hùng", 18, 9.2)

# --- Gọi phương thức ---
sv1.gioi_thieu()
sv2.gioi_thieu()

# --- In object (dùng __str__) ---
print(f"\n--- Danh sách ---")
for sv in [sv1, sv2, sv3]:
    print(f"  {sv}")
