# Buổi 6: Git Cơ Bản - Quản Lý Mã Nguồn

## Mục tiêu buổi học
- Hiểu Git là gì và tại sao lập trình viên nào cũng cần dùng
- Biết các lệnh Git cơ bản: add, commit, push, status
- Đẩy code lên GitHub và clone project về máy
- Làm việc với branch và tạo Pull Request
- Xử lý conflict khi làm việc nhóm

## Thời lượng: 90 phút

| Thời gian | Nội dung |
|-----------|----------|
| 0-5 phút | Ôn nhanh buổi trước |
| 5-20 phút | Git là gì? Cài đặt và cấu hình |
| 20-40 phút | Các lệnh cơ bản: add, commit, status, log |
| 40-55 phút | Làm việc với GitHub: push, clone |
| 55-75 phút | Branch và Pull Request |
| 75-90 phút | Xử lý conflict + Bài tập |

---

## Phần 1: Git Là Gì? (15 phút)

### Tại sao cần Git?

Tưởng tượng bạn đang viết bài luận:
- Bạn lưu file `bai_luan.docx`
- Sửa xong lưu thành `bai_luan_v2.docx`
- Sửa tiếp: `bai_luan_final.docx`
- Rồi: `bai_luan_final_final.docx` 😅

Git giải quyết vấn đề này! Git là **hệ thống quản lý phiên bản** (Version Control System), giúp bạn:
- Lưu lại lịch sử thay đổi của code
- Quay lại phiên bản cũ bất cứ lúc nào
- Làm việc nhóm mà không sợ ghi đè code của nhau
- Thử nghiệm tính năng mới mà không ảnh hưởng code chính

### Git vs GitHub

| Git | GitHub |
|-----|--------|
| Phần mềm cài trên máy | Website lưu trữ code online |
| Quản lý phiên bản | Chia sẻ code, làm việc nhóm |
| Chạy bằng dòng lệnh | Giao diện web đẹp |
| Miễn phí, mã nguồn mở | Miễn phí cho project công khai |

> 💡 Ví dụ dễ hiểu: Git giống như "Save game" trong game - bạn có thể quay lại bất kỳ điểm nào đã lưu!

### Cài đặt Git

```bash
# Kiểm tra Git đã cài chưa
git --version

# Nếu chưa có:
# - macOS: brew install git
# - Windows: Tải từ https://git-scm.com/downloads
# - Linux: sudo apt install git
```

### Cấu hình lần đầu

```bash
# Đặt tên (hiển thị khi commit)
git config --global user.name "Tên Của Bạn"

# Đặt email (nên dùng email GitHub)
git config --global user.email "email@example.com"

# Kiểm tra cấu hình
git config --list
```

---

## Phần 2: Các Lệnh Git Cơ Bản (20 phút)

### Khởi tạo repository (repo)

```bash
# Tạo thư mục project
mkdir du-an-python
cd du-an-python

# Khởi tạo Git trong thư mục này
git init
# Output: Initialized empty Git repository in .../du-an-python/.git/
```

### Vòng đời của file trong Git

```
┌──────────┐     git add     ┌──────────┐    git commit    ┌──────────┐
│ Untracked│ ──────────────► │  Staged  │ ───────────────► │Committed │
│ (Chưa    │                 │ (Sẵn sàng│                  │ (Đã lưu  │
│  theo dõi)│                 │  commit) │                  │  vào Git)│
└──────────┘                 └──────────┘                  └──────────┘
      ▲                                                          │
      │                    Sửa file                               │
      └──────────────────────────────────────────────────────────┘
```

### git status - Xem trạng thái

```bash
# Tạo file mới
echo "print('Hello Git!')" > main.py

# Xem trạng thái
git status
# Output:
# Untracked files:
#   main.py    ← File mới, Git chưa theo dõi
```

### git add - Thêm file vào staging

```bash
# Thêm 1 file cụ thể
git add main.py

# Thêm tất cả file đã thay đổi
git add .

# Xem lại trạng thái
git status
# Output:
# Changes to be committed:
#   new file: main.py    ← Sẵn sàng commit
```

### git commit - Lưu thay đổi

```bash
# Commit với message mô tả
git commit -m "Thêm file main.py - chương trình Hello Git"

# Output:
# [main abc1234] Thêm file main.py - chương trình Hello Git
# 1 file changed, 1 insertion(+)
```

> 💡 **Mẹo viết commit message tốt:**
> - Ngắn gọn, rõ ràng (dưới 50 ký tự)
> - Mô tả BẠN ĐÃ LÀM GÌ, không phải tại sao
> - Ví dụ tốt: "Thêm chức năng đăng nhập", "Sửa lỗi tính điểm"
> - Ví dụ xấu: "update", "fix", "abc"

### git log - Xem lịch sử

```bash
# Xem lịch sử commit
git log

# Xem ngắn gọn hơn
git log --oneline
# Output:
# abc1234 Thêm file main.py - chương trình Hello Git
```

### Ví dụ thực hành liên tục

```bash
# 1. Tạo project
mkdir quan-ly-todo
cd quan-ly-todo
git init

# 2. Tạo file đầu tiên
echo "# Quản Lý Todo" > README.md
git add README.md
git commit -m "Khởi tạo project với README"

# 3. Thêm code
# (Tạo file todo.py với nội dung)
git add todo.py
git commit -m "Thêm chức năng hiển thị todo"

# 4. Sửa code
# (Sửa file todo.py)
git add todo.py
git commit -m "Thêm chức năng thêm todo mới"

# 5. Xem lịch sử
git log --oneline
# Output:
# def5678 Thêm chức năng thêm todo mới
# abc1234 Thêm chức năng hiển thị todo
# 9876fed Khởi tạo project với README
```

---

## Phần 3: Làm Việc Với GitHub (15 phút)

### Tạo repository trên GitHub

1. Vào [github.com](https://github.com) → Đăng ký tài khoản (miễn phí)
2. Click nút **"New"** hoặc **"+"** → **"New repository"**
3. Đặt tên repo (ví dụ: `quan-ly-todo`)
4. Chọn **Public** (công khai) hoặc **Private** (riêng tư)
5. Click **"Create repository"**

### Push code lên GitHub

```bash
# Kết nối repo local với GitHub (chỉ làm 1 lần)
git remote add origin https://github.com/username/quan-ly-todo.git

# Đổi tên nhánh mặc định thành main (nếu cần)
git branch -M main

# Đẩy code lên GitHub lần đầu
git push -u origin main

# Từ lần sau, chỉ cần:
git push
```

### Clone - Tải project từ GitHub về máy

```bash
# Clone repo về máy (tạo thư mục mới)
git clone https://github.com/username/quan-ly-todo.git

# Clone xong, vào thư mục project
cd quan-ly-todo

# Xem code đã có sẵn
ls
```

> 💡 **Khi nào dùng clone?**
> - Khi bạn muốn tải project của người khác về học
> - Khi bạn đổi máy tính và muốn lấy code về
> - Khi bạn muốn đóng góp vào project mã nguồn mở

### Quy trình làm việc hàng ngày

```bash
# 1. Viết code...

# 2. Xem đã thay đổi gì
git status

# 3. Thêm file đã sửa
git add .

# 4. Commit
git commit -m "Mô tả thay đổi"

# 5. Push lên GitHub
git push
```

---

## Phần 4: Branch - Nhánh (20 phút)

### Branch là gì?

Branch giống như **tạo bản sao** của code để thử nghiệm mà không ảnh hưởng code chính.

```
          ┌── commit ── commit ── (feature/login)
         /
main: ──●──●──●──●──●──●
                    \
                     └── commit ── (fix/bug-diem)
```

- **main**: Nhánh chính, code ổn định
- **feature/xxx**: Nhánh phát triển tính năng mới
- **fix/xxx**: Nhánh sửa lỗi

### Các lệnh branch cơ bản

```bash
# Xem danh sách branch (dấu * là branch hiện tại)
git branch
# Output:
# * main

# Tạo branch mới
git branch feature/them-xoa-todo

# Chuyển sang branch mới
git checkout feature/them-xoa-todo
# Hoặc dùng lệnh mới hơn:
git switch feature/them-xoa-todo

# Tạo + chuyển sang branch mới (gộp 2 bước)
git checkout -b feature/them-xoa-todo
# Hoặc:
git switch -c feature/them-xoa-todo
```

### Quy trình làm việc với branch

```bash
# 1. Đang ở main, tạo branch mới cho tính năng
git checkout -b feature/them-xoa-todo

# 2. Code tính năng mới...
git add .
git commit -m "Thêm chức năng xóa todo"

# 3. Push branch lên GitHub
git push -u origin feature/them-xoa-todo

# 4. Quay lại main
git checkout main
```

### Pull Request (PR) - Gộp code vào main

Pull Request là cách **đề xuất gộp code** từ branch của bạn vào branch chính. Đây là quy trình chuẩn khi làm việc nhóm.

**Các bước tạo Pull Request trên GitHub:**

1. Push branch lên GitHub: `git push -u origin feature/them-xoa-todo`
2. Vào GitHub → Sẽ thấy thông báo "Compare & pull request" → Click vào
3. Viết tiêu đề và mô tả thay đổi
4. Click **"Create pull request"**
5. Người review xem code → Approve → **"Merge pull request"**
6. Xóa branch đã merge (GitHub sẽ gợi ý)

**Sau khi merge trên GitHub:**

```bash
# Quay lại main và cập nhật code mới nhất
git checkout main
git pull

# Xóa branch local đã merge
git branch -d feature/them-xoa-todo
```

---

## Phần 5: Xử Lý Conflict (15 phút)

### Conflict là gì?

Conflict xảy ra khi **2 người sửa cùng 1 dòng** trong cùng 1 file. Git không biết giữ phiên bản nào nên yêu cầu bạn quyết định.

### Ví dụ tạo conflict

```bash
# Giả sử file todo.py có dòng:
# tieu_de = "Danh sách việc cần làm"

# Người A sửa thành:
# tieu_de = "📋 Todo List"

# Người B sửa thành:
# tieu_de = "Danh sách công việc hôm nay"

# Khi merge → CONFLICT!
```

### Conflict trông như thế nào?

Khi có conflict, Git sẽ đánh dấu trong file:

```python
<<<<<<< HEAD
tieu_de = "📋 Todo List"
=======
tieu_de = "Danh sách công việc hôm nay"
>>>>>>> feature/doi-tieu-de
```

Giải thích:
- `<<<<<<< HEAD`: Code của bạn (branch hiện tại)
- `=======`: Ranh giới giữa 2 phiên bản
- `>>>>>>> feature/doi-tieu-de`: Code từ branch đang merge vào

### Cách xử lý conflict

**Bước 1:** Mở file có conflict

**Bước 2:** Chọn giữ phiên bản nào (hoặc kết hợp cả hai)

```python
# Xóa các dấu <<<, ===, >>> và giữ code bạn muốn:
tieu_de = "📋 Danh sách công việc hôm nay"
```

**Bước 3:** Add và commit

```bash
git add todo.py
git commit -m "Xử lý conflict: chọn tiêu đề kết hợp"
```

### Mẹo tránh conflict

1. **Pull thường xuyên**: `git pull` trước khi code
2. **Branch nhỏ**: Mỗi branch chỉ làm 1 việc, merge nhanh
3. **Giao tiếp**: Nói cho nhóm biết bạn đang sửa file nào
4. **Không sửa cùng file**: Phân chia công việc rõ ràng

---

## Phần 6: Tổng Hợp Các Lệnh Git Quan Trọng

### Bảng tóm tắt

| Lệnh | Công dụng | Ví dụ |
|------|-----------|-------|
| `git init` | Khởi tạo repo mới | `git init` |
| `git status` | Xem trạng thái file | `git status` |
| `git add` | Thêm file vào staging | `git add .` |
| `git commit` | Lưu thay đổi | `git commit -m "message"` |
| `git log` | Xem lịch sử | `git log --oneline` |
| `git push` | Đẩy code lên remote | `git push` |
| `git pull` | Kéo code mới về | `git pull` |
| `git clone` | Tải repo về máy | `git clone <url>` |
| `git branch` | Quản lý nhánh | `git branch feature/x` |
| `git checkout` | Chuyển nhánh | `git checkout main` |
| `git merge` | Gộp nhánh | `git merge feature/x` |

### File .gitignore

File `.gitignore` cho Git biết **không theo dõi** những file/thư mục nào:

```bash
# Tạo file .gitignore
# Nội dung ví dụ cho project Python:

# File Python compiled
__pycache__/
*.pyc

# File môi trường
.env
venv/

# File hệ điều hành
.DS_Store
Thumbs.db

# File IDE
.vscode/
.idea/

# File dữ liệu tạm
*.db
*.log
```

> 💡 Luôn tạo `.gitignore` ngay khi bắt đầu project!

---

## Bài Tập Thực Hành Tại Lớp

### Bài 1: Tạo repo đầu tiên
1. Tạo thư mục `bai-tap-git`
2. Khởi tạo Git (`git init`)
3. Tạo file `hello.py` với nội dung `print("Hello Git!")`
4. Add và commit file
5. Sửa file, thêm dòng `print("Tôi đã biết dùng Git!")`
6. Add và commit lần 2
7. Xem lịch sử bằng `git log --oneline`

### Bài 2: Push lên GitHub
1. Tạo repo mới trên GitHub
2. Kết nối repo local với GitHub
3. Push code lên
4. Kiểm tra trên GitHub xem code đã lên chưa

### Bài 3: Làm việc với branch
1. Tạo branch `feature/them-tinh-nang`
2. Chuyển sang branch mới
3. Thêm file `tinh_nang.py`
4. Commit và push branch lên GitHub
5. Tạo Pull Request trên GitHub
6. Merge PR
7. Quay lại main và pull code mới

---

## Bài Tập Về Nhà

### Bài 1: Đưa Mini Project lên GitHub
- Lấy bài Quản lý danh bạ (hoặc bất kỳ bài tập nào đã làm)
- Tạo repo trên GitHub
- Push code lên với commit message rõ ràng
- Thêm file README.md mô tả project

### Bài 2: Thực hành branch
- Tạo branch `feature/them-tinh-nang`
- Thêm 1 tính năng mới vào project
- Push branch và tạo Pull Request
- Tự merge PR

### Bài 3 (Nâng cao): Giả lập conflict
- Tạo 2 branch khác nhau, cùng sửa 1 file
- Merge branch 1 vào main
- Merge branch 2 vào main → Sẽ gặp conflict
- Xử lý conflict và commit

---

## Tóm tắt buổi học
- **Git**: Hệ thống quản lý phiên bản, lưu lịch sử code
- **Quy trình cơ bản**: `git add` → `git commit` → `git push`
- **GitHub**: Nơi lưu trữ code online, chia sẻ và làm việc nhóm
- **Branch**: Tạo nhánh để phát triển tính năng mà không ảnh hưởng code chính
- **Pull Request**: Cách gộp code an toàn, có review
- **Conflict**: Xảy ra khi 2 người sửa cùng chỗ, cần xử lý thủ công
- **Buổi sau**: Mini Project 1 - Tổng hợp kiến thức Giai đoạn 1!
