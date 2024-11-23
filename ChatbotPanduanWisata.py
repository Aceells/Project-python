import re
import random
import difflib

# Sapaan awal
sapaan = ['Halo! Ada yang bisa saya bantu terkait perjalanan Anda?', 'Hai! Selamat datang di Panduan Wisata!', 'Selamat datang! Ada yang ingin Anda tanyakan tentang wisata?']

# Respon umum
respon_umum = {
    "baik|kabar baik|lumayan": "Senang mendengar kabar baik! Ada destinasi yang ingin Anda tanyakan?",
    "kurang baik|buruk": "Maaf mendengar itu. Semoga perjalanan Anda nanti menyenangkan. Apa yang bisa saya bantu?",
    "terima kasih|thanks": "Sama-sama! Jangan ragu untuk bertanya jika butuh informasi lebih lanjut."
}

# Daftar kata kunci destinasi wisata
kata_kunci = [
    'pantai', 'gunung', 'taman nasional', 'museum', 'kuliner', 'budaya', 'belanja', 'alam', 'sejarah',
    'air terjun', 'desa wisata', 'kota besar', 'pemandangan', 'snorkeling', 'diving', 'mendaki', 'relaksasi'
]

# Informasi destinasi wisata
wisata = {
    "pantai|snorkeling|diving|relaksasi": (
        "Rekomendasi Wisata:\n- Pantai Kuta (Bali): Cocok untuk berselancar dan menikmati sunset.\n"
        "- Pantai Tanjung Tinggi (Belitung): Spot snorkeling dengan air jernih.\n"
        "- Pulau Bunaken (Sulawesi Utara): Tempat diving kelas dunia dengan terumbu karang indah."
    ),
    "gunung|mendaki|alam": (
        "Rekomendasi Wisata:\n- Gunung Rinjani (Lombok): Trekking seru dengan pemandangan luar biasa.\n"
        "- Gunung Bromo (Jawa Timur): Tempat terbaik untuk melihat sunrise.\n"
        "- Gunung Semeru (Jawa Timur): Pendakian untuk pecinta tantangan."
    ),
    "museum|sejarah|budaya": (
        "Rekomendasi Wisata:\n- Museum Nasional (Jakarta): Koleksi artefak sejarah Indonesia.\n"
        "- Museum Ullen Sentalu (Yogyakarta): Eksplorasi budaya Jawa.\n"
        "- Museum Angkut (Malang): Wisata edukasi tentang transportasi."
    ),
    "kuliner|belanja": (
        "Rekomendasi Wisata:\n- Malioboro (Yogyakarta): Pusat belanja dan kuliner lokal.\n"
        "- Jalan Braga (Bandung): Suasana unik dengan kafe dan toko antik.\n"
        "- Pasar Santa (Jakarta): Surga makanan unik dan kekinian."
    ),
    "air terjun|taman nasional|desa wisata": (
        "Rekomendasi Wisata:\n- Taman Nasional Komodo (NTT): Habitat asli Komodo dan pemandangan eksotis.\n"
        "- Air Terjun Tumpak Sewu (Jawa Timur): Keindahan air terjun spektakuler.\n"
        "- Desa Wisata Penglipuran (Bali): Desa adat yang asri dan unik."
    )
}

# Fungsi autocorrect untuk koreksi kata
def autocorrect(kata):
    saran = difflib.get_close_matches(kata, kata_kunci)
    if saran:
        return saran[0]
    return kata

# Fungsi untuk memproses input pengguna
def proses_input(input):
    kata = input.split()
    koreksi_kata = [autocorrect(k) for k in kata]
    return ' '.join(koreksi_kata)

# Fungsi untuk mencari respon berdasarkan kata kunci
def cari_respon(pesan):
    for pattern, respons in wisata.items():
        if re.search(pattern, pesan, re.IGNORECASE):
            return respons
    return None

# Program utama chatbot
print("=== Program Chatbot Panduan Wisata ===")
print("Bot \t:", random.choice(sapaan))

while True:
    user_input = input('User \t: ')
    user_input = proses_input(user_input)

    if re.search(r"halo|hello|hei|helo", user_input, re.IGNORECASE):
        print('Bot \t:', random.choice(sapaan))
    elif re.search(r"baik|buruk|terima kasih|thanks", user_input, re.IGNORECASE):
        for pattern, response in respon_umum.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                print("Bot \t:", response)
                break
    elif response := cari_respon(user_input):
        print("Bot \t:", response)
    else:
        print("Bot \t: Maaf, saya belum memiliki informasi tentang itu. Bisa jelaskan lebih spesifik?")

