from scapy.all import *
from scapy.layers.inet import IP, TCP

# Define the target IP and port
TARGET_IP = "192.168.183.1"  # Replace with the target Modbus device IP
TARGET_PORT = 502            # Default Modbus TCP port

# Craft a Modbus TCP packet
# MBAP Header
transaction_id = 0x0001      # Transaction ID (arbitrary)
protocol_id = 0x0000         # Protocol ID (0x0000 for Modbus)
length = 0x0006              # Length of remaining bytes (6 for this example)
unit_id = 0x01               # Unit ID (slave ID)

# PDU (Read Holding Registers - Function Code 0x03)
function_code = 0x03         # Function code for reading holding registers
starting_address = 0x0000    # Starting register address
quantity = 0x0001            # Number of registers to read

# Build the packet
mbap_header = struct.pack(">HHHB", transaction_id, protocol_id, length, unit_id)
pdu = struct.pack(">BHH", function_code, starting_address, quantity)
modbus_packet = mbap_header + pdu

#function_code = 0x06
#register_address = 0x0001  # Register address to write to
#value = 0x1234            # Value to write
#pdu = struct.pack(">BHH", function_code, register_address, value)
#modbus_packet = mbap_header + pdu
#send(IP(dst=TARGET_IP)/TCP(dport=TARGET_PORT)/Raw(load=modbus_packet))
# Send the packet

response = sr1(IP(dst=TARGET_IP)/TCP(dport=TARGET_PORT)/Raw(load=modbus_packet), timeout=2)

# Check the response
if response:
    print("Response received:")
    print(response.show())
else:
    print("No response received")