import hashlib
header_hex = ("01000000" +  "0000000000000000000000000000000000000000000000000000000000000000" +  "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a" +  "29ab5f49" +  "ffff001d" +  "1dac2b7c")
header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
print( hash[::-1].encode('hex_codec'))