# server_wan.py
import asyncio
import websockets
import json

# Lưu trữ 2 kết nối client
clients = []

async def handler(websocket):
    global clients

    # Thêm client mới
    clients.append(websocket)
    print(f"Client connected. Tổng client: {len(clients)}")

    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"Received: {data}")

            # Gửi dữ liệu cho client còn lại
            for client in clients:
                if client != websocket:
                    await client.send(json.dumps(data))

    except websockets.ConnectionClosed:
        print("Client disconnected.")
    finally:
        clients.remove(websocket)
        print(f"Client removed. Tổng client: {len(clients)}")

async def main():
    print("Server WebSocket đang chạy trên ws://localhost:8765")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # chạy vĩnh viễn

if __name__ == "__main__":
    asyncio.run(main())
