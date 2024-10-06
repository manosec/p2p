import requests


response = requests.get("http://torrent.mininova.org/announce?uploaded=0&downloaded=0&compact=0&event=started&peer_id=12345678987654321234&port=6881&info_hash=%18%28n%23K%ECt%B7%93S%C5%F1-%F3%1C%18k%CEX%A4&left=0 ")


print(response.content)