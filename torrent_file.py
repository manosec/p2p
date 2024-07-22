from bencoder import decode, encode


ben_code_string = '4:mano'
ben_code_int = 'i123e'
ben_code_list  = 'l4:mano5:manore'
ben_code_dict = 'd4:mano5:manor7:machine4:lovee'


print(decode(ben_code_int))
print(encode(decode(ben_code_int)))

file = open('ubuntu-24.04-desktop-amd64.iso.torrent', 'rb')

torrent_content = decode(file.read())

print(torrent_content)