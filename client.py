import asyncio
import websockets

async def chat():
    async with websockets.connect('ws://localhost:12345') as websocket:
        while True:
            message = input("Message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"- {response}")

if __name__ == '__main__':
    print('Starting client')
    asyncio.run(chat())