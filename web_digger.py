# ====== CREATED BY MIRZUHAIBCODINGS ======

import socket
import os
import time

os.system('clear')

print("\033[1;36m")
print("██╗░░░░░███████╗██████╗░  ██████╗░██╗██╗░██████╗░███████╗██████╗░")
print("██║░░░░░██╔════╝██╔══██╗  ██╔══██╗██║██║██╔════╝░██╔════╝██╔══██╗")
print("██║░░░░░█████╗░░██████╔╝  ██████╔╝██║██║██║░░██╗░█████╗░░██████╔╝")
print("██║░░░░░██╔══╝░░██╔═══╝░  ██╔═══╝░██║██║██║░░╚██╗██╔══╝░░██╔══██╗")
print("███████╗███████╗██║░░░░░  ██║░░░░░██║██║╚██████╔╝███████╗██║░░██║")
print("╚══════╝╚══════╝╚═╝░░░░░  ╚═╝░░░░░╚═╝╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝\n")

print("🔥 TOOL NAME      : WEB--DIGGER")
print("👑 CREATED BY     : MIRZUHAIBCODINGS")
print("📅 DATE           : 2025\n")

url = input("🌐 Enter Website URL (without https://): ")

try:
    ip = socket.gethostbyname(url)
    print("\n🔍 IP Address of", url, "is ➤", ip)
except socket.gaierror:
    print("\n❌ Error: Website not found or invalid URL.")

print("\n🔚 THANKS FOR USING OUR TOOL ")
