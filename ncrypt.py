import os
import sys
from base64 import b64encode, b64decode
from Crypto.Cipher import AES, Blowfish
from Crypto.Util.Padding import pad, unpad

# Bersihkan terminal saat awal dijalankan
os.system('cls' if os.name == 'nt' else 'clear')

# Daftar opsi algoritma, mode cipher, dan encoding output
algorithms = ["AES", "Blowfish"]
modes = ["CBC", "ECB"]
encodings = ["Base64", "None"]

# Fungsi pembuat objek cipher berdasarkan algoritma & mode
def get_cipher(algo, mode, key, iv):
    mode_map = {
        'CBC': AES.MODE_CBC,
        'ECB': AES.MODE_ECB,
    }
    # Kembalikan objek cipher sesuai pilihan pengguna
    if algo == "AES":
        return AES.new(key, mode_map[mode], iv=iv if mode == "CBC" else None)
    elif algo == "Blowfish":
        return Blowfish.new(key, mode_map[mode], iv=iv if mode == "CBC" else None)

# Fungsi padding key agar sesuai panjang yang diminta algoritma
def pad_key(key, algo):
    if algo == "AES":
        return key.ljust(32, b'\0')[:32]  # Panjang ideal AES: 32 byte
    elif algo == "Blowfish":
        return key.ljust(16, b'\0')[:16]  # Blowfish menerima 4 - 56 byte, ambil 16 byte

# Fungsi untuk proses enkripsi
def run_encrypt():
    print("\n--- ENKRIPSI ---")
    key = input("key: ").encode()  # Ambil key dari user
    raw_text = input("teks: ")  # Ambil plaintext dari user
    plaintext = raw_text.replace("\\n", "\n").encode()  # Konversi \n menjadi newline

    # Tampilkan pilihan dalam bentuk kolom
    print("\nalgoritma:       mode:        encode:")
    print("1. AES           1. CBC       1. Base64")
    print("2. Blowfish      2. ECB       2. None")
    print("\nformat: <algoritma>-<mode>-<encoding>\ncontoh: 1-1-1\n")
    choice = input("input=> ")

    try:
        # Parsing input dan ambil pilihan
        algo_idx, mode_idx, enc_idx = map(int, choice.strip().split("-"))
        algo = algorithms[algo_idx - 1]
        mode = modes[mode_idx - 1]
        encode = encodings[enc_idx - 1]
    except:
        print("❌ Format salah atau pilihan tidak valid.")
        return

    # Buat IV acak, tergantung algoritma
    iv = os.urandom(16 if algo == "AES" else 8)
    padded_key = pad_key(key, algo)  # Pad key-nya
    cipher = get_cipher(algo, mode, padded_key, iv)  # Buat objek cipher
    ciphertext = cipher.encrypt(pad(plaintext, cipher.block_size))  # Enkripsi data

    os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan terminal lagi

    # Encode output (Base64 atau hex)
    if encode == "Base64":
        output = b64encode(iv + ciphertext).decode()
    else:
        output = (iv + ciphertext).hex()

    # Tampilkan hasil
    print("\n✅ Enkripsi berhasil!")
    print("Private key :", key.decode())
    print("Public key  :", output)

# Fungsi untuk proses dekripsi
def run_decrypt():
    print("\n--- DEKRIPSI ---")
    key = input("key: ").encode()
    encrypted_text = input("ciphertext: ")

    # Tampilkan opsi seperti saat enkripsi
    print("\nalgoritma:       mode:        encode:")
    print("1. AES           1. CBC       1. Base64")
    print("2. Blowfish      2. ECB       2. None")
    print("\nformat: <algoritma>-<mode>-<encoding>\ncontoh: 1-1-1\n")
    choice = input("input=> ")

    try:
        # Parsing input pilihan pengguna
        algo_idx, mode_idx, enc_idx = map(int, choice.strip().split("-"))
        algo = algorithms[algo_idx - 1]
        mode = modes[mode_idx - 1]
        encode = encodings[enc_idx - 1]
    except:
        print("❌ Format salah atau pilihan tidak valid.")
        return

    padded_key = pad_key(key, algo)
    iv_size = 16 if algo == "AES" else 8  # Tentukan ukuran IV sesuai algoritma

    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Decode input sesuai metode encoding
        if encode == "Base64":
            data = b64decode(encrypted_text)
        else:
            data = bytes.fromhex(encrypted_text)

        # Pisahkan IV dan ciphertext
        iv = data[:iv_size]
        ciphertext = data[iv_size:]

        cipher = get_cipher(algo, mode, padded_key, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), cipher.block_size)  # Dekripsi

        # Tampilkan hasil
        print("\n✅ Dekripsi berhasil!")
        print("Hasil:", plaintext.decode())
    except:
        print("❌ Gagal mendekripsi! Periksa key, format, atau mode.")

# Fungsi utama (menu awal)
def main():
    print("Pilih salah satu!\n1. Enkripsi\n2. Dekripsi")
    choice = input(">> ")
    os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar

    if choice == "1":
        run_encrypt()
    elif choice == "2":
        run_decrypt()
    else:
        print("Pilihan tidak valid.")

# Eksekusi program jika dijalankan langsung
if __name__ == "__main__":
    main()
