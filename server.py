import asyncio
import websockets

async def handle_connection(websocket , path):
    print("New client connected")

    try:
        async for message in websocket:
            print(f"Received message from client:{message}")

        response = f"Server received:{message}"
        await websocket.send(response)

    except websockets.exceptions.ConnectionClosed:
        print("Client Disconnected")

start_server = websockets.serve(handle_connection, 'localhost', 8000 )

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()