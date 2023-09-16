import os
import time
import socket
import requests
from colorama import Fore
from pystyle import Center, Colors, Colorate
import whois
import subprocess

# 'python-whois' paketini otomatik olarak yükle
subprocess.call(["sudo", "apt-get", "install", "python-whois"])

bright_purple = '\033[95;1m'
reset = '\033[0m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
bold = '\033[1m'


# Giriş ekranı tasarımı
def show_intro():
    print(Colorate.Vertical(Colors.red_to_yellow, Center.XCenter("""

             ██▓        ▒█████      █     █░    ██ ▄█▀   ▓█████    ▓██   ██▓   
            ▓██▒       ▒██▒  ██▒   ▓█░ █ ░█░    ██▄█▒    ▓█   ▀     ▒██  ██▒   
            ▒██░       ▒██░  ██▒   ▒█░ █ ░█    ▓███▄░    ▒███        ▒██ ██░   
            ▒██░       ▒██   ██░   ░█░ █ ░█    ▓██ █▄    ▒▓█  ▄      ░ ▐██▓░   
            ░██████▒   ░ ████▓▒░   ░░██▒██▓    ▒██▒ █▄   ░▒████▒     ░ ██▒▓░   
            ░ ▒░▓  ░   ░ ▒░▒░▒░    ░ ▓░▒ ▒     ▒ ▒▒ ▓▒   ░░ ▒░ ░      ██▒▒▒    
            ░ ░ ▒  ░     ░ ▒ ▒░      ▒ ░ ░     ░ ░▒ ▒░    ░ ░  ░    ▓██ ░▒░    
              ░ ░      ░ ░ ░ ▒       ░   ░     ░ ░░ ░       ░       ▒ ▒ ░░     
                ░  ░       ░ ░         ░       ░  ░         ░  ░    ░ ░        
                                                              ░ ░    
                                LowkeyPanel is Loading...       

    """)))
    time.sleep(2)  # Sistem yüklendi simülasyonu için 2 saniye bekletin
    os.system('cls' if os.name == 'nt' else 'clear')  # Ekranı temizle (Windows ve Linux/Unix için)


# Ana menü tasarımı
def main_menu():
    menu = f"""
    {bright_purple}
                              ╔═════════════════╗
                              ║ LowkeyFilterApp ║
                              ╚═════════════════╝
                    ╔═════════════════════════════════════╗
                    ║ Programmed By Regarus & Frankovsky  ║
                    ╚═════════════════════════════════════╝
                       〝 Please do not use for illegal 〞                  
               ╔═════════════════════════════════════════════╗
               ║                   -Menu-                    ║ 
               ║ Whois               ╗ ╔            XXXXXXX  ║
               ║ Instagram           ║ ║            XXXXXXX  ║                         
               ║ Twitter             ║ ║            XXXXXXX  ║
               ║ Twitch              ║ ║            XXXXXXX  ║
               ║ Social              ╝ ╚            XXXXXXX  ║ 
               ╚═════════════════════════════════════════════╝
    {reset}"""
    print(menu)


# Giriş ekranını göster
show_intro()

while True:
    main_menu()

    choice = input("⋙⋙")




    def whois_bot():
        while True:
            domain_name = input(
                "Write Domain Name: ")

            if domain_name.lower() == "menu":
                whois_results = ""
                return  # Ana menüye dön
            else:
                try:
                    whois_info = whois.whois(domain_name)

                    if whois_info.status:
                        print("Whois Bilgileri:")
                        print(f"Alan Adı: {whois_info.domain_name}")
                        print(f"Durum: {whois_info.status}")
                        print(f"Oluşturulma Tarihi: {whois_info.creation_date}")
                        print(f"Son Güncelleme Tarihi: {whois_info.updated_date}")
                        print(f"Bitiş Tarihi: {whois_info.expiration_date}")
                        print(f"Kayıt Sahibi: {whois_info.registrant_name}")
                    else:
                        print(f"{domain_name} için whois bilgisi bulunamadı.")
                except whois.parser.WhoisException as e:
                    print(f"Hata: {e}")

    if choice == 'whois':
        whois_bot()

    elif choice == '2':
        print("Seçenek 2'yi seçtiniz. Yapabileceğiniz işlemler burada.")
        # Seçenek 2'ye ait işlemleri burada ekleyin
    elif choice == '3':
        print("Seçenek 3'ü seçtiniz. Yapabileceğiniz işlemler burada.")
        # Seçenek 3'e ait işlemleri burada ekleyin
    elif choice == '4':
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçenek! Lütfen 1, 2, 3 veya 4 girin.")
