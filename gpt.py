from bencoder import decode, encode
import hashlib
import random
import requests
from urllib.parse import quote_plus

def generate_id():
    # Generates a 20-byte peer ID
    # -PY01- is 6 characters, leaving room for 14 random characters to make 20
    return f"-PY01-{''.join([str(random.randint(0, 9)) for _ in range(14)])}".encode('utf-8')

def sha1_hash(content):
    return hashlib.sha1(content).digest()  # SHA-1 should return a 20-byte binary digest

# Load the torrent file
file_path = './torrents/ubuntu-24.04.1-desktop-amd64.iso.torrent'
with open(file_path, 'rb') as file:
    torrent_content = decode(file.read())

# Generate the required data for the tracker request
info_hash = sha1_hash(encode(torrent_content[b'info']))  # Get binary hash
peer_id = generate_id()  # Must be exactly 20 bytes

# Construct the tracker request URL
params = {
    'tracker_url': torrent_content[b'announce'].decode('utf-8'),
    'info_hash': quote_plus(info_hash),  # URL-encode the binary hash using quote_plus
    'peer_id': quote_plus(peer_id),  # URL-encode peer_id properly
    'left': torrent_content[b'info'][b'length'],  # Remaining bytes to download
    'downloaded': 0,
    'uploaded': 0,
    'compact': 1,
    'port': 6889
}

tracker_request_url = (
    f"{params['tracker_url']}?info_hash={params['info_hash']}&peer_id={params['peer_id']}"
    f"&left={params['left']}&downloaded={params['downloaded']}&uploaded={params['uploaded']}"
    f"&compact={params['compact']}&port={params['port']}"
)

# Send the request to the tracker
response = requests.get(tracker_request_url)

print(response.content)
# Print the response from the tracker
print("Tracker Response:", decode(response.content))
