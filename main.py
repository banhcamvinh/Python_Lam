
# todo
# * Học thuộc bài
# * (1) Công thức for char in str
# * (2) Công thức for index in range(0, len(str)))
# * (3) Công thức while
# * (4) Try except là gì? Khi nào sử dụng
# * (5) Hiểu được Regexp - Kiểm tra regex trong python

# name = "Lâm"

# for char in name:
#     print(char)

# * Range(start, end, step) --> 1,2,3,4,5

# for index in range(0, len(name), 1):
#     print(name[index])

# * 3 cái cần xác định và tái hiện lại
# * (1) bắt đầu -(2) bước nhảy- (3) kết thúc

# index = 0
# while index < len(name):
#     print(name[index])
#     index += 1


# * GUESS NUMBER
# import random
# random_number = random.randint(1, 100)
# print(random_number)
# while True:
#     try:
#         guess_number = int(input("Please guess a number from 1 to 100: "))
#         if guess_number > random_number:
#             print("Too big")
#     except Exception as error:
#         print(f"Please enter a valid number {error}")


# * Bài 3: Mật khẩu mạnh
# * Viết chương trình kiểm tra mật khẩu có đủ mạnh không:
# * Ít nhất 8 ký tự
# * Có ít nhất 1 chữ hoa
# * Có ít nhất 1 chữ thường
# * Có ít nhất 1 số
# * Gợi ý: Dùng các phương thức .isupper(), .islower(), .isdigit() kết hợp vòng lặp

# * BIỂU THỨC CHÍNH QUY - REGEXP
# * (1) Tìm kiếm
# * (2) Replace
# * (2) Validate

# import re

# pwd = "Aa1234567"
# validate_rs = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$", pwd)
# if validate_rs:
#     print("Valid password")
# else:
#     print("Invalid password")


# * GIT
# * (1) GIT repo local - remote github
# * (2) git init --> tạo repo trên local - empty
# * (3) changes --> so với phiên bản trước đó
# 