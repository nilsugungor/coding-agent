from functions.run_python_file import run_python_file

# 1. Kullanım talimatlarını basmalı (Parametresiz çalıştırma)
print("--- Test 1: main.py (No Args) ---")
print(run_python_file("calculator", "main.py"))
print("-" * 30)

# 2. Hesap makinesini çalıştırma (Parametre ile: "3 + 5")
print("\n--- Test 2: main.py (With Args '3 + 5') ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("-" * 30)

# 3. Hesap makinesinin kendi testlerini çalıştırma
print("\n--- Test 3: tests.py ---")
print(run_python_file("calculator", "tests.py"))
print("-" * 30)

# 4. Güvenlik Testi: Üst klasöre çıkmaya çalışma (Hata dönmeli)
print("\n--- Test 4: ../main.py (Should Error) ---")
print(run_python_file("calculator", "../main.py"))
print("-" * 30)

# 5. Olmayan dosya testi (Hata dönmeli)
print("\n--- Test 5: nonexistent.py (Should Error) ---")
print(run_python_file("calculator", "nonexistent.py"))
print("-" * 30)

# 6. Python dosyası olmayan dosya testi (Hata dönmeli)
print("\n--- Test 6: lorem.txt (Should Error) ---")
print(run_python_file("calculator", "lorem.txt"))
print("-" * 30)