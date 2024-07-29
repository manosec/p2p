from bencoder import decode, encode
import hashlib
import random
import requests

def generate_id():
    # Generates a peer ID with a specific format
    return f"-P001-{''.join([str(random.randint(0, 9)) for _ in range(12)])}".encode('utf-8')

def sha1_hash(content):
    return hashlib.sha1(content).hexdigest()

# Load the torrent file
file_path = 'torrents/ubuntu-22.04.4-desktop-amd64.iso.torrent'
with open(file_path, 'rb') as file:
    torrent_content = decode(file.read())

# Generate the required data for the tracker request
#Encoding using bencode because we are sending this to the tracker server
info_hash = sha1_hash(encode(torrent_content[b'info']))
peer_id = generate_id()

# Construct the tracker request URL
params = {
    'tracker_url': torrent_content[b'announce'].decode('utf-8'),
    'info_hash': requests.utils.quote(info_hash),
    'peer_id': peer_id.decode('utf-8'),
    'left': torrent_content[b'info'][b'length'],
    'downloaded': 0,
    'uploaded': 0,
    'compact': 1,
    'port':6889
}

print(params)

tracker_request_url = f"{params['tracker_url']}?info_hash={params['info_hash']}&peer_id={params['peer_id']}&left={params['left']}&downloaded={params['downloaded']}&uploaded={params['uploaded']}&compact={params['compact']}&port={params['port']}"
print(tracker_request_url)
# Send the request to the tracker
response = requests.get(tracker_request_url)

# Print the response from the tracker
print("Tracker Response:", decode(response.content))