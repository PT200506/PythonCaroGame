import websocket
import threading

SERVER_URL = "wss://caro-ws.onrender.com"  # dùng wss nếu deploy trên Render

def on_message(ws, message):
    print("Nhận dữ liệu:", message)
    # Xử lý đi nước đi đối phương, update board...

def on_open(ws):
    print("Đã kết nối server WebSocket!")

def on_close(ws):
    print("Ngắt kết nối server")

ws = websocket.WebSocketApp(
    SERVER_URL,
    on_message=on_message,
    on_open=on_open,
    on_close=on_close
)

threading.Thread(target=ws.run_forever, daemon=True).start()

