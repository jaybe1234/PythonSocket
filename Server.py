import socket
import threading
from msgHandler import msgHandler

class Server:
    def __init__(self, port):
        self.ip = "10.148.0.5"#socket.gethostbyname(socket.gethostname())
        self.port = port
        print(self.ip, self.port)
        self.userNum = 0
        self.Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.Server.bind((self.ip, self.port))
        except socket.error as e:
            print("[EXCEPTION]",e)
        self._msghandler = msgHandler()


    def client_handler(self, conn, addr):
        """
        handling client threads
        :param conn: connection object
        :param addr: (str, int) ip and port
        """
        self._msghandler.addUser(conn, addr)
        self.userNum += 1
        while True:
            try:
                conn.sendall("bamlor".encode("utf-8"))
                data = conn.recv(2048).decode("utf-8")
                if data:
                    for i in self._msghandler.connectionList:
                        conn_i,_ = i
                        conn_i.sendall(data.encode("utf-8"))
                    print(f"[ECHO] {data}")
                    if data == "disconnect":
                        break
            except Exception as e:
                print(f"[EXCEPTION]", e)
                break
        self._msghandler.removeUser(conn,addr)
        conn.close()
        self.userNum -= 1
        print(f"[USER DISCONNECTED]")


    def authenticate(self,conn, addr):
        """
        logged-in user authenticaton
        :param conn: connection object
        :param addr: (str, int) ip and port
        """
        pass

    def initialize(self):
        """
        server initialization and main loop
        """
        print("[STARTING] Server is starting...")
        self.Server.listen(10)
        print("[READY] Server is ready")
        try:
            while True:
                conn, addr  = self.Server.accept()
                self.authenticate(conn, addr)
                thread = threading.Thread(target=self.client_handler, args=(conn, addr))
                thread.start()
                print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")
        except KeyBoardInterrupt:
            print("[SERVER CLOSING]")
            self.Server.close()

if __name__ == "__main__":
    s = Server(5050)
    s.initialize()
