import os

# Kullanıcının girişinden tüm kelimeleri al ve küçük harflere dönüştür
user_input = input("Bir metin girin: ")
words = user_input.lower().split()

# Bilgi dosyalarının bulunduğu dizini belirtin
knowledge_dir = "Info/"
files = os.listdir(knowledge_dir)

found = False
file_name = ""

# Her dosyayı tek tek kontrol et
for file in files:
    if file.endswith(".txt"):
        # Dosyayı UTF-8 olarak aç ve içinde arama yap
        with open(os.path.join(knowledge_dir, file), "r", encoding="utf-8") as f:
            content = f.read().lower()
            # Her kelimenin metinde olup olmadığını kontrol et
            if any(word in content for word in words):
                found = True
                file_name = file
                break

# Sonucu yazdır
if found:
    print("Bulundu! Dosya adı:", file_name)
else:
    print("Bulunamadı.")
