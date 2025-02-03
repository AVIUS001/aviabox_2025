# communications/protocol_handler.py
class ProtocolHandler:
    def __init__(self):
        self.protocol = "DefaultProtocol"

    def encode(self, message):
        return message.encode("utf-8")

    def decode(self, byte_message):
        return byte_message.decode("utf-8")

if __name__ == "__main__":
    ph = ProtocolHandler()
    encoded = ph.encode("Test")
    print(ph.decode(encoded))
