class msgHandler:
    def __init__(self):
        self.buffer = []
        self._userNum = 0
        self.connectionList = []


    def addUser(self,conn,addr):
        """
        adding a user
        :param conn: connection object
        :param addr: (str, int) ip and port
        """
        # self.buffer.append([])
        self.connectionList.append((conn,addr))
        self._userNum += 1

    def removeUser(self,conn, addr):
        """
        removing a user
        :param conn: connection object
        :param addr: (str, int) ip and port
        """
        self.connectionList.remove((conn,addr))



    def msgHandle(self):
        """
        sending messages in buffer
        """
        pass
