import socket, time

PORT = 3333 #socket to be used and shown on wireshark
INTERVAL = 5 #seconds between each packet send

with open("credentials.txt", "r") as f:
    lines = f.readlines()
    USERNAME = lines[0].strip()
    PASSWORD = lines[1].strip()

msg = f"username={USERNAME}&password={PASSWORD}".encode()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print(f"Sending every {INTERVAL}s on UDP {PORT}  ->  {msg.decode()}")
print("Wireshark filter:  udp.port == 3333")
print("Ctrl+C to stop.\n")

while True:
    sock.sendto(msg, ("255.255.255.255", PORT))
    print("sent", time.strftime("%H:%M:%S"))
    time.sleep(INTERVAL)