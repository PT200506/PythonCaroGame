import asyncio
import websockets
import json

SERVER_URL = "wss://caro-ws.onrender.com"   # Nếu chạy LAN thì đổi thành IP máy chủ

async def connect_to_server(on_message):
    try:
        async with websockets.connect(SERVER_URL) as websocket:
            print("Đã kết nối tới server WebSocket!")

            # Lắng nghe tin nhắn từ server
            async for message in websocket:
                data = json.loads(message)
                on_message(data)

    except Exception as e:
        print("Lỗi kết nối:", e)


async def send_move(x, y):
    """Gửi nước đi lên server"""
    try:
        async with websockets.connect(SERVER_URL) as websocket:
            msg = json.dumps({"type": "move", "x": x, "y": y})
            await websocket.send(msg)
    except Exception as e:
        print("Lỗi gửi nước:", e)
