# === BUỔI 8: KẾ THỪA ===

class DongVat:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def keu(self):
        print("...")

    def __str__(self):
        return f"{self.ten} ({self.tuoi} tuổi)"


class Cho(DongVat):
    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi)
        self.giong = giong

    def keu(self):
        print(f"{self.ten}: Gâu gâu! 🐕")

    def __str__(self):
        return f"{self.ten} ({self.tuoi} tuổi) - Giống: {self.giong}"


class Meo(DongVat):
    def keu(self):
        print(f"{self.ten}: Meo meo! 🐱")


class Chim(DongVat):
    def keu(self):
        print(f"{self.ten}: Chíp chíp! 🐦")

    def bay(self):
        print(f"{self.ten} đang bay~")


# --- Sử dụng ---
print("=== VƯỜN THÚ ===\n")

dong_vat = [
    Cho("Buddy", 3, "Corgi"),
    Meo("Mimi", 2),
    Chim("Tweety", 1),
]

for dv in dong_vat:
    print(dv)
    dv.keu()
    print()
