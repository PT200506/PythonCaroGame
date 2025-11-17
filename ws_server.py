import asyncio
import websockets

# Danh sách client đang kết nối
connected_clients = set()

async def handler(websocket, path):
    # thêm client mới
    connected_clients.add(websocket)
    print("🔵 Client connected")

    try:
        async for message in websocket:
            # broadcast cho tất cả client khác
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)

    except websockets.exceptions.ConnectionClosed:
        print("🔴 Client disconnected")

    finally:
        connected_clients.remove(websocket)


async def main():
    print("🚀 WebSocket server running on ws://localhost:8765")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # chạy mãi mãi


if __name__ == "__main__":
    asyncio.run(main())
