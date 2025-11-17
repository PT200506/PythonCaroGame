import os
import asyncio
import websockets

PORT = int(os.environ.get("PORT", 8765))

async def handler(ws, path):
    print("Client connected!")
    async for message in ws:
        print("Received:", message)

async def main():
    print(f"Server running on port {PORT}")
    async with websockets.serve(handler, "0.0.0.0", PORT):
        await asyncio.Future()

asyncio.run(main())
