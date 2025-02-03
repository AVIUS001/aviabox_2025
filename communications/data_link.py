# communications/data_link.py
class DataLink:
    def __init__(self):
        self.buffer = []

    def send(self, data):
        print(f"Sending data: {data}")
        self.buffer.append(data)

    def receive(self):
        if self.buffer:
            data = self.buffer.pop(0)
            print(f"Received data: {data}")
            return data
        else:
            print("No data")
            return None

if __name__ == "__main__":
    dl = DataLink()
    dl.send("Hello")
    dl.receive()
