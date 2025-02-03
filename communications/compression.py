# communications/compression.py
import zlib

class Compression:
    def compress(self, data: bytes) -> bytes:
        return zlib.compress(data)

    def decompress(self, data: bytes) -> bytes:
        return zlib.decompress(data)

if __name__ == "__main__":
    comp = Compression()
    original = b"Sample data for compression."
    compressed = comp.compress(original)
    decompressed = comp.decompress(compressed)
    print("Original:", original)
    print("Compressed:", compressed)
    print("Decompressed:", decompressed)
