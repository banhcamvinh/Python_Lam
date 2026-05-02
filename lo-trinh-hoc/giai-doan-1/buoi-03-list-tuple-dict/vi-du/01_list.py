# === BUỔI 3: LIST (DANH SÁCH) ===

# --- Tạo list ---
mon_hoc = ["Toán", "Lý", "Hóa", "Tin", "Anh"]
diem = [8, 7, 9, 6, 10]

print("--- Danh sách môn học ---")
for i, mon in enumerate(mon_hoc):
    print(f"  {i + 1}. {mon}")

# --- Truy cập và cắt ---
print(f"\nMôn đầu tiên: {mon_hoc[0]}")
print(f"Môn cuối: {mon_hoc[-1]}")
print(f"3 môn đầu: {mon_hoc[:3]}")

# --- Thêm, sửa, xóa ---
print("\n--- Thao tác trên list ---")
mon_hoc.append("Văn")
print(f"Sau append('Văn'): {mon_hoc}")

mon_hoc.insert(2, "Sinh")
print(f"Sau insert(2, 'Sinh'): {mon_hoc}")

mon_hoc.remove("Lý")
print(f"Sau remove('Lý'): {mon_hoc}")

mon_hoc.pop()
print(f"Sau pop(): {mon_hoc}")

# --- Sắp xếp và thống kê ---
print("\n--- Thống kê điểm ---")
print(f"Điểm gốc: {diem}")

diem.sort()
print(f"Sắp xếp tăng: {diem}")

diem.sort(reverse=True)
print(f"Sắp xếp giảm: {diem}")

print(f"Cao nhất: {max(diem)}")
print(f"Thấp nhất: {min(diem)}")
print(f"Tổng: {sum(diem)}")
print(f"Trung bình: {sum(diem) / len(diem):.1f}")

# --- Kiểm tra phần tử ---
print(f"\n10 có trong list? {10 in diem}")
print(f"5 có trong list? {5 in diem}")
print(f"Số 8 xuất hiện {diem.count(8)} lần")
