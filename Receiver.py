class Receiver:
    def __init__(self ,input_socks, output_queue):
        self.input_socks = input_socks
        self.output_queue = output_queue
        self.start()


    def start(self):
        while True:
            for sock in self.input_socks:
                input_ = sock.recv()
                if input_:
                    self.output_queue.put((input_, sock))


    def return_socket(self, sock):
        self.input_socks.add(sock)


    def remove(self, sock):
        self.input_socks.remove(sock)
