# === BÀI THỰC HÀNH: TỪ ĐIỂN ANH-ANH ===
import requests


def tra_tu(tu):
    """Tra từ điển tiếng Anh dùng Free Dictionary API"""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{tu}"

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError:
        print("❌ Không có kết nối mạng!")
        return

    if response.status_code == 404:
        print(f"❌ Không tìm thấy từ '{tu}'")
        return

    data = response.json()[0]
    print(f"\n📖 {data['word']}")

    if "phonetic" in data:
        print(f"🔊 Phát âm: {data['phonetic']}")

    for meaning in data.get("meanings", []):
        loai_tu = meaning["partOfSpeech"]
        print(f"\n  [{loai_tu}]")
        for i, defn in enumerate(meaning["definitions"][:3]):
            print(f"    {i + 1}. {defn['definition']}")
            if "example" in defn:
                print(f"       Ví dụ: {defn['example']}")


# Chương trình chính
print("=== 📖 TỪ ĐIỂN ANH-ANH ===")
print("Nhập 'q' để thoát\n")

while True:
    tu = input("Nhập từ cần tra: ").strip()
    if tu.lower() == "q":
        print("Tạm biệt! 👋")
        break
    if tu:
        tra_tu(tu)
