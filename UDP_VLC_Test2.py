
import vlc
import socket
import threading

# 建立 VLC 媒體播放器實例
instance = vlc.Instance('--no-xlib')  # 在 Linux 上，加上 --no-xlib 選項可以避免 X11 佈局錯誤
player = instance.media_player_new()

# 載入影片列表
media_list = [
    'Video\Test.mp4',
    'Video\Test2.mp4',
    'Video\Test3.mp4'
]

# 預設播放第一個影片
current_media_index = 0
media = instance.media_new(media_list[current_media_index])
player.set_media(media)

# 播放影片
player.toggle_fullscreen()
player.play()
player.audio_set_volume(0)

# 監聽 UDP 訊息並切換影片
def udp_listener():
    UDP_IP = "127.0.0.1"  # 設置 UDP 伺服器的 IP
    UDP_PORT = 12345  # 設置 UDP 伺服器的埠號

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode()
        if message.startswith("play"):
            video_index = int(message.split("/")[1])
            play_video(video_index)
        elif message.startswith("exit"):
            exit()

# 切換播放指定索引的影片
def play_video(index):
    global current_media_index
    if index >= 0 and index < len(media_list):
        current_media_index = index
        media = instance.media_new(media_list[current_media_index])
        player.set_media(media)
        player.toggle_fullscreen()
        player.play()
        player.audio_set_volume(0)

# 啟動 UDP 訊息監聽線程
udp_thread = threading.Thread(target=udp_listener)
udp_thread.start()

# 等待 UDP 訊息監聽線程結束
udp_thread.join()

# 釋放資源
player.release()
instance.release()
