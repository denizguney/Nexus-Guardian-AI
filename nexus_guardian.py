import os
import sys
import time
import psutil
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_ai():
    """Sistemin normal durumunu öğrenen yapay zeka modülü"""
    clear_screen()
    print("="*45)
    print(" NEXUS AI: Sistem Analiz Ediliyor & Öğreniliyor")
    print("="*45)
    
    veriler = []
    # 5 saniyelik baseline (normal durum) verisi toplanıyor
    for i in range(5):
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        veriler.append([cpu, ram])
        print(f" Öğreniliyor... Adım {i+1}/5 | CPU: %{cpu} | RAM: %{ram}")

    # Modeli Eğit (İstisnai durum payı %10)
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(veriler)
    print("\n ÖĞRENME TAMAMLANDI. KORUMA MOTORU AKTİF!\n")
    time.sleep(1.5)
    return model

def monitor_system(model):
    """Canlı sistem gözleme ve anomali tespit döngüsü"""
    clear_screen()
    print("="*45)
    print(" NEXUS KORUMA MOTORU: CANLI SİSTEM GÖZETİMİ")
    print("Süreci durdurmak için 'Ctrl + C' kombinasyonunu kullanın.")
    print("="*45)
    
    try:
        while True:
            c = psutil.cpu_percent(interval=1)
            r = psutil.virtual_memory().percent
            
            # AI Tahmini
            tahmin = model.predict([[c, r]])
            
            if tahmin[0] == 1:
                durum = "OK "
                print(f"[{time.strftime('%H:%M:%S')}] CPU: %{c} | RAM: %{r} -> {durum}")
            else:
                durum = "⚠️ ANOMALİ TESPİT EDİLDİ!"
                print(f"[{time.strftime('%H:%M:%S')}] CPU: %{c} | RAM: %{r} -> {durum}")
                print(">>> UYARI: Olağandışı sistem hareketi reaksiyon gerektirebilir!")
                
                # Şüpheli işlemleri listele ve müdahale mekanizmasını çağır
                # En yüksek CPU tüketen süreci örnek olarak yakalayalım
                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                    try:
                        if proc.info['cpu_percent'] > 50: # %50 üzeri CPU kullanan varsa
                            secure_mitigation(proc.info['pid'])
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
                        
    except KeyboardInterrupt:
        print("\n[!] Nöbet sona erdi. Ana menüye dönülüyor...")
        time.sleep(1.5)

def secure_mitigation(suspicious_pid):
    """Kritik süreç koruma filtresi ve müdahale mekanizması"""
    try:
        proc = psutil.Process(suspicious_pid)
        proc_name = proc.name().lower()
        proc_path = proc.exe()

        # KRİTİK GÜVENLİK FİLTRESİ: Windows sistem dosyalarına dokunma!
        protected_paths = ["C:\\Windows\\System32", "C:\\Windows\\SysWOW64"]
        if any(path in proc_path for path in protected_paths):
            print(f"🛡️ Korumalı sistem dosyası tespit edildi: {proc_name}. Müdahale güvenlik nedeniyle iptal edildi.")
            return

        print(f"\n ŞÜPHELİ SÜREÇ YAKALANDI: {proc_name} (PID: {suspicious_pid})")
        choice = input(f"❓ Kritik Karar: Bu işlemi durdurmak istiyor musun? (evet/hayır): ")

        if choice.lower() == 'evet':
            proc.terminate() 
            print(f" {proc_name} işlemi başarılı bir şekilde sonlandırıldı.")
            
    except Exception as e:
        print(f" Müdahale sırasında hata oluştu: {e}")

def recovery_scan(drive_path):
    """Ham disk analizi yöntemiyle silinmiş JPEG dosyalarını kurtarma (Carving)"""
    clear_screen()
    print("="*45)
    print(f" ADLİ BİLİŞİM: {drive_path} SÜRÜCÜSÜ ANALİZ EDİLİYOR")
    print("="*45)
    
    JPEG_START = b'\xff\xd8\xff\xe0'
    JPEG_END = b'\xff\xd9'
    
    try:
        # Yönetici yetkisi kontrolü için sürücü ham okuma modunda açılır
        with open(drive_path, "rb") as disk:
            print("[*] Sürücü erişimi başarılı. Sektör taranıyor (Büyük disklerde zaman alabilir)...")
            content = disk.read() # Not: Çok büyük disklerde parça parça (chunk) okunması önerilir
            
            start_pos = 0
            found_count = 0
            
            while True:
                start_pos = content.find(JPEG_START, start_pos)
                if start_pos == -1: 
                    break
                
                end_pos = content.find(JPEG_END, start_pos)
                if end_pos == -1: 
                    break
                
                # Bulunan fotoğrafı "recovered_img_X.jpg" adıyla dışarı çıkar
                filename = f"recovered_img_{found_count}.jpg"
                with open(filename, "wb") as f:
                    f.write(content[start_pos:end_pos+2])
                
                found_count += 1
                start_pos = end_pos + 2
                
        print(f"\n İşlem tamamlandı! {found_count} adet silinmiş fotoğraf izi başarıyla kurtarıldı.")
        
    except PermissionError:
        print(" Erişim Reddedildi: Lütfen VS Code'u veya terminali YÖNETİCİ (Administrator) olarak çalıştırın!")
    except Exception as e:
        print(f" Veri kurtarma esnasında hata: {e}")
        
    input("\nDevam etmek için Enter'a basın...")

def main_menu():
    ai_model = None
    while True:
        clear_screen()
        print("="*45)
        print("  NEXUS GUARDIAN AI - SİBER KOMUTA MERKEZİ  ")
        print("="*45)
        print("1.  Anomali Taraması (Sistemi Canlı Koru)")
        print("2.  Veri Kurtarma (Silinen Resimleri Ham Diskten Bul)")
        print("3.  Çıkış")
        print("="*45)
        
        secim = input("Ne yapmak istersin dostum? (1/2/3): ")
        
        if secim == "1":
            if ai_model is None:
                ai_model = initialize_ai()
            monitor_system(ai_model)
        elif secim == "2":
            hedef = input("\nTaranacak sürücü harfini gir (Örn: D, E, F): ").upper().strip()
            if hedef:
                recovery_scan(f"\\\\.\\{hedef}:")
        elif secim == "3":
            print("\n Nexus Guardian kapatılıyor. Güvende kalın dostum!")
            sys.exit()
        else:
            print(" Geçersiz seçim, lütfen tekrar dene.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
