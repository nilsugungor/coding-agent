from functions.get_file_content import get_file_content

# 1. Lorem Ipsum Testi (Zaten çalışıyor)
print("--- Testing lorem.txt (Truncation Check) ---")
print(get_file_content("calculator", "lorem.txt"))

# 2. main.py Testi (def main(): burada çıkıyor)
print("\n--- Testing main.py ---")
print(get_file_content("calculator", "main.py"))

# 3. calculator.py Testi (def _apply_operator burada çıkıyor)
print("\n--- Testing pkg/calculator.py ---")
print(get_file_content("calculator", "pkg/calculator.py"))

# 4. Hata Testi (Dışarı çıkma)
print("\n--- Testing /bin/cat (Should Error) ---")
print(get_files_info_output := get_file_content("calculator", "/bin/cat"))

# 5. Hata Testi (Olmayan dosya)
print("\n--- Testing non-existent file (Should Error) ---")
print(get_file_content("calculator", "pkg/does_not_exist.py"))