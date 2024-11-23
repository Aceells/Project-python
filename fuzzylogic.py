class FuzzyKemiringanTanah:
    def __init__(self):
        # Batasan untuk setiap variabel
        self.min_kadar_air = 5
        self.max_kadar_air = 50
        self.min_curah_hujan = 0
        self.max_curah_hujan = 300
        self.min_kemiringan = 0
        self.max_kemiringan = 45

    def fuzzy_kadar_air_rendah(self, x):
        if x <= 15:
            return 1
        elif x >= 35:
            return 0
        else:
            return (35 - x) / (35 - 15)

    def fuzzy_kadar_air_tinggi(self, x):
        if x <= 15:
            return 0
        elif x >= 35:
            return 1
        else:
            return (x - 15) / (35 - 15)

    def fuzzy_curah_hujan_rendah(self, x):
        if x <= 50:
            return 1
        elif x >= 150:
            return 0
        else:
            return (150 - x) / (150 - 50)

    def fuzzy_curah_hujan_tinggi(self, x):
        if x <= 50:
            return 0
        elif x >= 150:
            return 1
        else:
            return (x - 50) / (150 - 50)

    def fuzzy_kemiringan_landai(self, alpha):
        return self.min_kemiringan + alpha * (15 - self.min_kemiringan)

    def fuzzy_kemiringan_sedang(self, alpha):
        return 15 + alpha * (30 - 15)

    def fuzzy_kemiringan_curam(self, alpha):
        return 30 + alpha * (45 - 30)

    def inferensi(self, kadar_air, curah_hujan):
        # Fuzzifikasi
        kadar_air_rendah = self.fuzzy_kadar_air_rendah(kadar_air)
        kadar_air_tinggi = self.fuzzy_kadar_air_tinggi(kadar_air)
        curah_hujan_rendah = self.fuzzy_curah_hujan_rendah(curah_hujan)
        curah_hujan_tinggi = self.fuzzy_curah_hujan_tinggi(curah_hujan)

        # Rule-based inference
        alpha1 = min(kadar_air_rendah, curah_hujan_rendah)
        z1 = self.fuzzy_kemiringan_landai(alpha1)

        alpha2 = min(kadar_air_rendah, curah_hujan_tinggi)
        z2 = self.fuzzy_kemiringan_sedang(alpha2)

        alpha3 = min(kadar_air_tinggi, curah_hujan_rendah)
        z3 = self.fuzzy_kemiringan_sedang(alpha3)

        alpha4 = min(kadar_air_tinggi, curah_hujan_tinggi)
        z4 = self.fuzzy_kemiringan_curam(alpha4)

        # Defuzzifikasi (weighted average)
        total_alpha = alpha1 + alpha2 + alpha3 + alpha4
        if total_alpha == 0:
            return (self.min_kemiringan + self.max_kemiringan) / 2

        z = (alpha1 * z1 + alpha2 * z2 + alpha3 * z3 + alpha4 * z4) / total_alpha
        return z

def main():
    print("\n=== SISTEM FUZZY TSUKAMOTO PENENTUAN TINGKAT KEMIRINGAN TANAH ===")
    fuzzy = FuzzyKemiringanTanah()

    # Input dari pengguna
    kadar_air = float(input("Masukkan kadar air tanah (5-50%): "))
    curah_hujan = float(input("Masukkan curah hujan (0-300 mm): "))

    # Hitung hasil kemiringan
    hasil_kemiringan = fuzzy.inferensi(kadar_air, curah_hujan)

    # Tampilkan hasil
    print("\n=== HASIL PERHITUNGAN ===")
    print(f"Kadar Air Tanah: {kadar_air:.1f}%")
    print(f"Curah Hujan: {curah_hujan:.1f} mm")
    print(f"Tingkat Kemiringan Tanah yang Direkomendasikan: {hasil_kemiringan:.1f} derajat")

if __name__ == "__main__":
    main()
