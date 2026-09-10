import socket
import sys
from datetime import datetime

# Port umum yang sering dipindai (HTTP, HTTPS, SSH, FTP, RTSP, MikroTik)
TARGET_PORTS = [21, 22, 80, 443, 554, 8080, 8291]

def scan_target(target_host):
    print("=" * 50)
    print(f"MOON Scanner (Hood_1) - Scanning: {target_host}")
    print(f"Waktu Mulai: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"IP Target Terdeteksi: {target_ip}\n")
    except socket.gaierror:
        print("[!] Gagal menyelesaikan nama host.")
        return

    for port in TARGET_PORTS:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # Timeout 1 detik per port
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port:<5} : TERBUKA (OPEN)")
        else:
            print(f"[-] Port {port:<5} : Tertutup")
        s.close()

    print("=" * 50)
    print("Pemindaian Selesai!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("Masukkan IP / Domain Target: ")
    
    if target:
        scan_target(target)
    else:
        print("Target tidak boleh kosong.")