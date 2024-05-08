import socket

# 設定UDP伺服器
UDP_IP = "0.0.0.0"  # 監聽所有IP
UDP_PORT = 5005     # 使用的UDP埠號

# 建立UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("UDP伺服器已啟動，正在監聽埠號", UDP_PORT)

while True:
    # 接收來自客戶端的訊息
    data, addr = sock.recvfrom(1024)
    print("Received message:", data.decode())