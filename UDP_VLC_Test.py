import socket
import subprocess
import keyboard
import threading
import sys

# 設定UDP伺服器
UDP_IP = "127.0.0.1"  # 監聽所有IP
UDP_PORT = 12345     # 使用的UDP埠號

# 建立UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def keyboard_listener():
    while True:
        if keyboard.is_pressed('q'):  # 監聽鍵盤事件，當按下'q'鍵時退出程式
            print("Exit command received from keyboard. Exiting program.")
            sys.exit()  # 彈出並結束程式

 # 啟動鍵盤事件監聽線程
keyboard_thread = threading.Thread(target=keyboard_listener)
keyboard_thread.start()

try:
   

    while True:
        # 接收來自客戶端的訊息
        data, addr = sock.recvfrom(1024)
        print("Received message:", data.decode())

        # 根據接收到的指令執行相應的動作
        if data.decode() == "play_video":
            # subprocess.Popen(["vlc", "C:/Users/zoids/Downloads/Test.mp4"])  # 替換為實際的影片路徑
            print("Playing video...")
        elif data.decode() == "play_audio":
            # subprocess.Popen(["vlc", "C:/Users/zoids/Downloads/Test.mp3"])  # 替換為實際的音訊路徑
            print("Playing audio...")

except KeyboardInterrupt:
    print('interrupted!')
