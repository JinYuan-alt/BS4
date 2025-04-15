import socket
# Prompt user for coil address
coil_address = int(input("Enter the coil address (1-9999): "))
# Validate coil address input
if coil_address < 1 or coil_address > 9999:
    print("Invalid coil address. Please enter a value between 1 and 9999.")
    exit(1)
# Prompt user for desired coil state (on or off)
coil_state = input("Enter the coil state (on/off): ").strip().lower()
# Validate coil state input
if coil_state not in ["on", "off"]:
    print("Invalid state. Please enter 'on' or 'off'.")
    exit(1)
# Adjust coil address to 0-based (subtract 1)
coil_address -= 1
# Prepare the Modbus packet
coil_address_bytes = coil_address.to_bytes(2, byteorder='big')
# Set the coil state (0xFF00 for ON, 0x0000 for OFF)
if coil_state == "on":
    coil_value = bytes.fromhex("FF 00")
elif coil_state == "off":
    coil_value = bytes.fromhex("00 00")
# Modbus packet format: Transaction ID, Protocol, Length, Unit ID, Function Code, Coil address, Value
modbus_packet = bytes.fromhex("00 01 00 00 00 06 01 05") + coil_address_bytes + coil_value
target_ip = "192.168.163.10"
target_port = 502
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(3)
    s.connect((target_ip, target_port))
    s.send(modbus_packet)
    response = s.recv(1024)
    print("Response:", response.hex())
