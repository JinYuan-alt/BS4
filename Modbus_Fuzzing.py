from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.contrib.modbus import *
import random


def generate_malformed_modbus_pdu():
    # Force invalid function codes, corrupt data, or malformed lengths
    malformed_type = random.choice([
        "invalid_func_code",
        "oversized_pdu",
        "zero_length",
        "wrong_endianness",
        "corrupt_header"
    ])

    if malformed_type == "invalid_func_code":
        # Function codes 128-255 are reserved/illegal
        func_code = random.randint(128, 255)
        return bytes([func_code]) + bytes([random.randint(0, 255)])  # Add garbage data

    elif malformed_type == "oversized_pdu":
        # Exceed Modbus max PDU length (253 bytes for TCP)
        oversized_data = bytes([random.randint(1, 127)]) + os.urandom(300)
        return oversized_data

    elif malformed_type == "zero_length":
        # Empty PDU (may break parsers)
        return b''

    elif malformed_type == "wrong_endianness":
        # Valid request but with swapped byte order
        return struct.pack(">H", random.randint(0, 0xFFFF))  # Big-endian in little-endian field

    else:  # "corrupt_header"
        # Random bytes masquerading as a header
        return os.urandom(6)  # Typical Modbus header is 6 bytes


def generate_malformed_adu():
    trans_id = random.randint(0, 0xFFFF)
    unit_id = random.randint(0, 255)
    malformed_pdu = generate_malformed_modbus_pdu()
    return ModbusADURequest(transId=trans_id, unitId=unit_id) / Raw(load=malformed_pdu)


def fuzz_modbus_tcp(target_ip):
    sport = random.randint(1024, 65535)
    pkt = IP(dst=target_ip) / TCP(
        sport=sport,
        dport=502,
        flags="PA",
        seq=random.randint(0, 2 ** 32 - 1),
        ack=random.randint(0, 2 ** 32 - 1),
    ) / generate_malformed_adu()

    send(pkt, verbose=0)
    print(f"[!] Sent MALFORMED packet to {target_ip}")


# Fuzz aggressively
for _ in range(100):  # Send 100 malformed packets
    fuzz_modbus_tcp("192.168.163.10")