from pieces.pieces.bencoding import Decoder, Encoder

print(Decoder(b'i123e').decode())

print(Encoder(123).encode())

f = open('./torrents/')