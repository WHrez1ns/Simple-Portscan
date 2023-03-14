import socket
import time

wordlist = open("<wordlist path>", "r")
ports = wordlist.read().splitlines()
response = "S"


def portscan():
    print("-----------------------------")
    ip = input("Domain/IP: ")
    print("-----------------------------")
    for port in ports:
        port = int(port)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        code = client.connect_ex((ip, port))
        if (code == 0):
            print(port, "OPEN")


while response:
    portscan()
    print("-----------------------------")
    print("Deseja continuar?")
    response = input("s/n: ").upper()
    if response != "S":
        print("-----------------------------")
        print("Encerrando...")
        print("-----------------------------")
        time.sleep(1.5)
        exit()
