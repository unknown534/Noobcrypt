# 🔐 Noobcrypt

**Noobcrypt** adalah alat enkripsi dan dekripsi berbasis Python (CLI) yang ringan dan sederhana, mendukung algoritma AES dan Blowfish, serta mode CBC dan ECB. Dirancang untuk pengguna awam (noob friendly) namun tetap kuat untuk penggunaan offline.

---

## 🚀 Fitur

- 🔑 Enkripsi & Dekripsi teks menggunakan:
  - Algoritma: `AES`, `Blowfish`
  - Mode: `CBC`, `ECB`
  - Output: `Base64`, `Hex`
- 🧠 Antarmuka CLI interaktif
- 📦 Berjalan offline (tidak butuh internet)
- 💡 Mendukung input multiline (`\n`)

---

## 🖥️ Cara Menjalankan

### 📋 Persyaratan

- Python 3.6+
- Modul `pycryptodome`

### 📦 Instalasi Dependensi

```bash
git clone https://github.com/unknown534/Noobcrypt.git

pip3 install -r requirements.txt

▶️ Menjalankan

python3 tool.py


---

🧪 Contoh Penggunaan

1. Enkripsi

Pilih salah satu!
1. Enkripsi
2. Dekripsi
>> 1

--- ENKRIPSI ---
key: password
teks: http://example.com\nbaris kedua

algoritma:       mode:        encode:
1. AES           1. CBC       1. Base64
2. Blowfish      2. ECB       2. None

format: <algoritma>-<mode>-<encoding>
contoh: 1-1-1

input=> 1-1-1

✅ Enkripsi berhasil!
Private key : password
Public key  : iA0FsMPr...

2. Dekripsi

Pilih salah satu!
1. Enkripsi
2. Dekripsi
>> 2

--- DEKRIPSI ---
key: password
ciphertext: iA0FsMPr...

input=> 1-1-1

✅ Dekripsi berhasil!
Hasil: http://example.com
baris kedua


---

📁 Struktur File

.
├── tool.py          # Skrip utama CLI
├── requirements.txt # Dependensi
├── README.md        # Dokumentasi proyek
