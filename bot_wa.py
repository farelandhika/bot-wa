import pyautogui
import time

def validasi_nomor(nomor):
    """Validasi format nomor WhatsApp"""
    nomor = nomor.replace("+", "").replace("-", "").replace(" ", "")
    if not nomor.isdigit():
        return False
    if len(nomor) < 10:
        return False
    return True

def kirim_pesan_wa():
    """Fungsi untuk mengirim pesan WhatsApp otomatis"""
    
    # Input dari pengguna
    print("=" * 50)
    print("🤖 BOT PENGIRIM PESAN WHATSAPP OTOMATIS")
    print("=" * 50)
    
    # Input nomor WhatsApp
    while True:
        nomor = input("\n📱 Masukkan nomor WhatsApp (contoh: 08123456789): ").strip()
        if validasi_nomor(nomor):
            break
        print("❌ Format nomor tidak valid! Coba lagi.")
    
    # Input jumlah pesan
    while True:
        try:
            jumlah_kirim = int(input("📝 Berapa pesan yang ingin dikirim? (1-100): ").strip())
            if 1 <= jumlah_kirim <= 100:
                break
            print("❌ Jumlah harus antara 1-100!")
        except ValueError:
            print("❌ Masukkan angka yang valid!")
    
    # Input pesan template
    pesan_template = input("💬 Template pesan (gunakan {n} untuk nomor urut): ").strip()
    if not pesan_template:
        pesan_template = "Pesan otomatis-{n}"
    
    print(f"\n✅ Target nomor: {nomor}")
    print(f"📊 Total pesan: {jumlah_kirim}")
    print("\n⏳ Buka WhatsApp Web dan klik chat target dalam 10 detik...")
    
    # Delay sebelum mulai
    for countdown in range(10, 0, -1):
        print(f"   Siap dalam {countdown}...", end='\r')
        time.sleep(1)
    
    print("\n🚀 Mulai mengirim pesan...\n")
    
    terkirim = 0
    gagal = 0
    
    # Loop untuk mengirim pesan
    for i in range(1, jumlah_kirim + 1):
        try:
            # Format pesan dengan nomor urut
            pesan = pesan_template.format(n=i)
            
            # Ketik pesan
            pyautogui.write(pesan, interval=0.05)
            time.sleep(0.2)
            
            # Tekan Enter untuk mengirim
            pyautogui.press("enter")
            
            terkirim += 1
            print(f"✅ [{i}/{jumlah_kirim}] Pesan terkirim: {pesan}")
            
            # Jeda antar pesan untuk menghindari spam
            time.sleep(0.5)
            
        except Exception as e:
            gagal += 1
            print(f"❌ [{i}/{jumlah_kirim}] Error: {str(e)}")
            time.sleep(1)
    
    # Tampilkan ringkasan
    print("\n" + "=" * 50)
    print("📊 RINGKASAN PENGIRIMAN")
    print("=" * 50)
    print(f"✅ Berhasil: {terkirim}")
    print(f"❌ Gagal: {gagal}")
    print(f"📈 Total: {terkirim + gagal}")
    print(f"🎯 Tingkat Keberhasilan: {(terkirim / jumlah_kirim * 100):.1f}%")
    print("=" * 50)

if __name__ == "__main__":
    try:
        kirim_pesan_wa()
    except KeyboardInterrupt:
        print("\n\n⚠️ Program dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\n❌ Error fatal: {str(e)}")
