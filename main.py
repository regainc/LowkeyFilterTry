import os
import time
import socket
import requests
from colorama import Fore
from pystyle import Center, Colors, Colorate
import whois
import subprocess



bright_purple = '\033[95;1m'
reset = '\033[0m'
green = '\033[92m'
yellow_color = '\033[93m'
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
    menu_text = """
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
    """
    colored_menu = Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(menu_text))
    print(colored_menu)


# Giriş ekranını göster
show_intro()

#aksiyonlar buraya

whois_results = ""



#WHOIS BOT
def whois_bot():
    global whois_results  # whois_results değişkenini global olarak kullanmak için

    while True:
        # Kullanıcı girişini renklendirmek için renkli metni ekrana yazdırın
        colored_domain_prompt = Colorate.Vertical(Colors.yellow_to_red, "Domain name for whois: ")
        domain_name = input(f"{colored_domain_prompt}")

        if domain_name.lower() == "menu":
            whois_results = ""  # Sorgu sonuçlarını temizle
            return  # Ana menüye dön
        else:
            try:
                whois_info = whois.whois(domain_name)

                if whois_info.status:
                    whois_result = f"Whois Bilgileri:\n"
                    whois_result += f"Alan Adı: {whois_info.domain_name}\n"
                    whois_result += f"Durum: {whois_info.status}\n"
                    whois_result += f"Oluşturulma Tarihi: {whois_info.creation_date}\n"
                    whois_result += f"Son Güncelleme Tarihi: {whois_info.updated_date}\n"
                    whois_result += f"Bitiş Tarihi: {whois_info.expiration_date}\n"
                    whois_result += f"Kayıt Sahibi: {whois_info.registrant_name}\n"

                    # Kullanıcı girişi ve sorgu sonuçlarını aynı renkle yazdırın
                    colored_result = Colorate.Vertical(Colors.yellow_to_red, whois_result)
                    print(f"{colored_domain_prompt}{domain_name}\n{colored_result}")
                else:
                    print(f"{domain_name} için whois bilgisi bulunamadı.")
            except whois.parser.WhoisException as e:
                print(f"Hata: {e}")



#aksiyon bitiş

while True:
    main_menu()
    yellow_input = f"{yellow_color}╔══(root@LowkeyPanel)\n╚>>>> {reset}"  # Sarı renkli giriş istemi
    choice = input(yellow_input)

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
        break  # Ana menüyü sona erdirir ve programı kapatır.
    else:
        print("Geçersiz seçenek! Lütfen 1, 2, 3 veya 4 girin.")
