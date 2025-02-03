# communications/network_manager.py
class NetworkManager:
    def __init__(self):
        self.status = "disconnected"

    def connect(self, address):
        self.status = "connected"
        print(f"Connected to {address}")

    def disconnect(self):
        self.status = "disconnected"
        print("Disconnected")

if __name__ == "__main__":
    nm = NetworkManager()
    nm.connect("192.168.1.1")
    nm.disconnect()
