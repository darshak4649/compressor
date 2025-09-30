
from collections import defaultdict
class Algorithm:

    def compress(self, data: str):
        if not data:
            return b""

        char_map = defaultdict(list)

        for index, byte in enumerate(data):
            char = chr(byte)
            char_map[char].append(index)

    def decompress(self, data: bytes) -> bytes:
        decompressed = bytearray()
        for i in range(0, len(data), 2):
            count = data[i]
            value = data[i+1]
            decompressed.extend([value]*count)
        return bytes(decompressed)