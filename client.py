import asyncio
import websockets
import config

async def chat(name):
    async with websockets.connect(f'ws://{config.server_ip}:{config.server_port}/{name}') as websocket:
        while True:
            message = input("Message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"- {response}")

def main():
    name = input("Enter name: ")
    print('Starting client')
    asyncio.run(chat(name))

if __name__ == '__main__':
    main()