import asyncio
import logging

from pieces.pieces.torrent import Torrent
from pieces.pieces.client import TorrentClient

loop = asyncio.get_event_loop()
client = TorrentClient(Torrent(args.torrent))
task = loop.create_task(client.start())

try:
    loop.run_until_complete(task)
except CancelledError:
    logging.warning('Event loop was canceled')