import asyncio
import websockets

# Define the client behavior
async def connect_to_server():
    async with websockets.connect('ws://localhost:8000') as websocket:
        # Send a message to the server
        message = "Hello, Aliva!"
        await websocket.send(message)
        print(f"Sent message to server: {message}")

        # Receive and print the response from the server
        response = await websocket.recv()
        print(f"Received response from server: {response}")

# Run the client
asyncio.get_event_loop().run_until_complete(connect_to_server())
