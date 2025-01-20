import asyncio
import websockets
import config
from pprint import pprint

connected_clients = set()

async def handle_client(websocket):
    print('Got client', websocket.request.path)
    connected_clients.add(websocket)
    user = websocket.request.path[1:]

    try:
        async for message in websocket:
            print(f'Received from {user}: {message}')
            for client in connected_clients:
                if client != websocket:
                    print(f'sending to {client.request.path[1:]}')
                    await client.send(f'{user}: {message}')
                    print('sent')
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(
        handle_client,
        config.server_ip,
        config.server_port,
        ping_timeout=60,
        ping_interval=10
    )
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())