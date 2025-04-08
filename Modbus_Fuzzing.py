from scapy.all import *
from scapy.layers.inet import IP, TCP
import random
import string


def generate_random_payload():
    base = b"\x00" * random.randint(10, 100)
    junk = bytes(random.choices(range(0x20, 0x7E), k=random.randint(5, 50)))  # readable junk
    split = random.randint(0, len(base))
    return base[:split] + junk + base[split:]


def polymorphic_packet(target_ip):
    flags_pool = ["S", "A", "R", "F", "U", "P"]
    flag_combo = ''.join(random.sample(flags_pool, k=random.randint(1, 3)))  # Mix flags

    tcp_opts = [
        ('MSS', random.randint(0, 1460)),
        ('WScale', random.randint(0, 14)),
        ('NOP', None),
        ('Timestamp', (random.randint(0, 2 ** 32 - 1), 0))
    ]
    random.shuffle(tcp_opts)

    pkt = IP(dst=target_ip, ttl=random.randint(1, 255)) / TCP(
        sport=random.randint(1024, 65535),
        dport=random.randint(1, 65535),
        flags=flag_combo,
        seq=random.randint(0, 2 ** 32 - 1),
        ack=random.randint(0, 2 ** 32 - 1),
        window=random.randint(0, 65535),
        urgptr=random.randint(0, 65535),
        options=tcp_opts[:random.randint(1, len(tcp_opts))]
    ) / Raw(load=generate_random_payload())

    send(pkt, verbose=0)
    print(f"Sent polymorphic TCP packet with flags={flag_combo}")


# Send multiple packets to test
for _ in range(10):
    polymorphic_packet("192.168.163.10")  # Replace with your target IP
