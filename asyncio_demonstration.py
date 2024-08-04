import asyncio
from random import randint

async def do_some(ip, port):
    print(f"Connection is about to be establish with {ip} on {port}")
    reader, writer = await asyncio.open_connection(ip, port)

    print(f"Connection established with {ip} on {port}")
    await asyncio.sleep(randint(0, 5))

    writer.close()
    print(f"Connection Closed with {ip}")


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()

    work = [
        asyncio.ensure_future(do_some('8.8.8.8', '53')),
        asyncio.ensure_future(do_some('8.8.4.4', '53'))
    ]

    event_loop.run_until_complete(asyncio.gather(*work))