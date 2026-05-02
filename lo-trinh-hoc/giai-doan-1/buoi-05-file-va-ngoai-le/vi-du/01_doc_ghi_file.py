# === BUỔI 5: ĐỌC GHI FILE ===

# --- Ghi file ---
print("--- Ghi file ---")
with open("ket_qua.txt", "w", encoding="utf-8") as f:
    f.write("Kết quả học tập\n")
    f.write("================\n")
    f.write("Toán: 8\n")
    f.write("Lý: 7\n")
    f.write("Hóa: 9\n")
print("✅ Đã ghi file ket_qua.txt")

# --- Đọc toàn bộ ---
print("\n--- Đọc toàn bộ file ---")
with open("ket_qua.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
    print(noi_dung)

# --- Đọc từng dòng ---
print("--- Đọc từng dòng ---")
with open("ket_qua.txt", "r", encoding="utf-8") as f:
    for i, dong in enumerate(f):
        print(f"  Dòng {i + 1}: {dong.strip()}")

# --- Nối thêm (append) ---
print("\n--- Nối thêm ---")
with open("ket_qua.txt", "a", encoding="utf-8") as f:
    f.write("Tin: 10\n")
    f.write("Anh: 8\n")
print("✅ Đã thêm 2 dòng")

# --- Đọc lại để kiểm tra ---
print("\n--- File sau khi thêm ---")
with open("ket_qua.txt", "r", encoding="utf-8") as f:
    print(f.read())

# --- Lưu và đọc danh sách ---
print("--- Lưu danh sách sinh viên ---")
sinh_vien = [
    {"ten": "Minh", "diem": 8.5},
    {"ten": "Lan", "diem": 7.0},
    {"ten": "Hùng", "diem": 9.0}
]

with open("sinh_vien.txt", "w", encoding="utf-8") as f:
    for sv in sinh_vien:
        f.write(f"{sv['ten']},{sv['diem']}\n")

print("Đọc lại:")
with open("sinh_vien.txt", "r", encoding="utf-8") as f:
    for dong in f:
        ten, diem = dong.strip().split(",")
        print(f"  {ten}: {float(diem):.1f}")
