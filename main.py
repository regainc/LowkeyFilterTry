import os
import time
import socket
import requests
from colorama import Fore
from pystyle import Center, Colors, Colorate
import whois
import subprocess
import random
import datetime

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
                                  ║ LowkeyFilterApp
                                  ║       LUX       ║
                                  ╚═════════════════╝
                        ╔═════════════════════════════════════╗
                        ║ Programmed By Regarus & Frankovsky  ║
                        ╚═════════════════════════════════════╝
                           〝 Please do not use for illegal 〞                  
                    ╔═════════════════════════════════════════════╗
                    ║                   -Menu-                    ║ 
                    ║ Whois               ╗ ╔            Pending  ║
                    ║ SQLScanner          ║ ║            Pending  ║                         
                    ║ Twitter             ║ ║            Pending  ║
                    ║ Mail-Deleted        ║ ║            Pending  ║
                    ║ Pending             ╝ ╚            Pending  ║ 
                    ╚═════════════════════════════════════════════╝
    """
    colored_menu = Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(menu_text))
    print(colored_menu)


# Giriş ekranını göster
show_intro()

# aksiyonlar buraya

whois_results = ""


# WHOIS BOT
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


def second_main_menu():
    menu_text = """

                ╔═════════════════════════════════════╗
                ║        Lowkey How To Usage ?        ║
                ╚═════════════════════════════════════╝
                  〝 Please do not use for illegal 〞                  
            ╔═════════════════════════════════════════════╗
            ║                 -Commands Menu-                
            ║ "Whois" -get information about the website
            ║ "SQLScanner" -scan for sql vulnerability                        
            ║ "Option 3" -write info
            ║ "Option 4" -write info
            ║ "Option 5" -write info
            ╚═════════════════════════════════════════════╝
        """
    colored_menu = Colorate.Vertical(Colors.green_to_blue, Center.XCenter(menu_text))
    print(colored_menu)


# aksiyon bitiş


# /////////////////////////////////////////////////////////////////////////////

while True:
    main_menu()
    yellow_input = f"{yellow_color}╔══(root@LowkeyPanel)\n╚>>>> {reset}"  # Sarı renkli giriş istemi
    choice = input(yellow_input)

    if choice == 'whois':
        whois_bot()
    elif choice == 'sqlscanner':
        # choice 2 kısmı ////////////////////////////////////////////////////////////////////

        def sql_injection_test(site_url):
            payloads = ["' OR '1'='1", "'; DROP TABLE users--", "1' OR 'a'='a"]

            for payload in payloads:
                test_url = f"{site_url}?id={payload}"
                response = requests.get(test_url)

                if "error" in response.text.lower():
                    result_text = Colorate.Vertical(Colors.red_to_yellow,
                                                    f"Potansiyel SQL Enjeksiyon Açığı Bulundu: {test_url}")
                else:
                    result_text = Colorate.Vertical(Colors.red_to_yellow,
                                                    f"SQL Enjeksiyon Açığı Bulunamadı: {test_url}")

                print(result_text)


        def main():
            print(Colorate.Vertical(Colors.yellow_to_red, Center.XCenter("Lowkey SQLScanner ")))
            site_url = input(Colorate.Vertical(Colors.yellow_to_red, "Website: "))

            # SQL enjeksiyon testini başlatın
            sql_injection_test(site_url)

            # Sonuçları gösterdikten sonra kullanıcıyı bekletin
            input(Colorate.Vertical(Colors.yellow_to_red, "Press any key to see the results..."))


        if __name__ == "__main__":
            main()






    # choice 3 kısmı ////////////////////////////////////////////////////////////////////

    elif choice == '-help':
        # İkinci ana menüyü görüntüle
        second_main_menu()
        second_choice = input(yellow_input)


    def colored_input(prompt):
        return input(Colorate.Vertical(Colors.yellow_to_red, prompt))


    if choice == 'maildeleted':
        print(Colorate.Vertical(Colors.yellow_to_red, "Mail-Deleted Loading..."))

        cevaplar = []  # Sorular ve cevaplar için bir liste oluşturun

        # Kullanıcıya e-posta adresini işlemek isteyip istemediğini sorun
        cevap = colored_input("Which e-mail address do you want to process?: ")
        cevaplar.append(("Which e-mail address do you want to process?", cevap))  # Soru ve cevapları listeye ekleyin

        # İlk soruya verilen cevaba göre ikinci soruyu seçin
        if cevap.lower() == 'gggg':
            ikinci_soru = "gggg / dddd"
        elif cevap.lower() == 'dddd':
            ikinci_soru = "cccc / eeee"

        elif cevap.lower() == 'fffff':
            ikinci_soru = "llll / bbbb"

        else:
            ikinci_soru = "Which one do you choose? (anonim & certain)."

        # İkinci soruyu görüntüleyin ve cevap alın
        ikinci_cevap = colored_input(ikinci_soru + ": ")
        cevaplar.append((ikinci_soru, ikinci_cevap))  # Soru ve cevapları listeye ekleyin

        # 3. soruyu sormak için
        ucuncu_soru = Colorate.Vertical(Colors.yellow_to_red, "Should I use VPN? (Y/n)")
        ucuncu_cevap = colored_input(ucuncu_soru + ": ")
        cevaplar.append((ucuncu_soru, ucuncu_cevap))  # Soru ve cevapları listeye ekleyin

        dorduncu_soru = Colorate.Vertical(Colors.yellow_to_red, "Force deletion of all types of emails? (Y/n)")
        dorduncu_cevap = colored_input(dorduncu_soru + ": ")
        cevaplar.append((dorduncu_soru, dorduncu_cevap))

        # Cevap alındığında "Yükleniyor..." yazısını görüntüleyin ve 5 saniye bekleyin
        print(Colorate.Vertical(Colors.yellow_to_red, "Messages are deleted..."))
        time.sleep(5)

        # Rastgele bir tarih oluşturun ve 10 satır metin oluşturun
        for _ in range(1000):
            yil = random.randint(2022, 2023)
            ay = random.randint(1, 12)
            gun = random.randint(1, 28)  # Basit bir hata yönetimi için 28'i kullanabilirsiniz.

            tarih = datetime.date(yil, ay, gun)
            metin = f"Your emails dated {tarih.strftime('%d-%m-%Y')} are being deleted."
            print(Colorate.Vertical(Colors.yellow_to_red, metin))

            # Her metin satırı yazdırıldıktan sonra 0.5 saniye bekleyin
            time.sleep(0.01)

        # İşlem tamamlandığında soruları ve cevapları görüntüleyin
        print(Colorate.Vertical(Colors.yellow_to_red, "Emails have been deleted.."))
        for soru, cevap in cevaplar:
            print(Colorate.Vertical(Colors.yellow_to_red, f"{soru}: {cevap}"))

        print(Colorate.Vertical(Colors.yellow_to_red, "Total deleted emails: 1000"))

        # Kullanıcıyı bekletin
        input(Colorate.Vertical(Colors.yellow_to_red, "Press the button to continue..."))



    elif choice == '4':
        print("Çıkış yapılıyor...")
        break  # Ana menüyü sona erdirir ve programı kapatır.
    else:
        print("Geçersiz seçenek! Lütfen 1, 2, 3 veya 4 girin.")
