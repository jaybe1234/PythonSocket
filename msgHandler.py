class msgHandler:
    def __init__(self):
        self.buffer = []
        self._userNum = 0
        self._connectionList = []


    def addUser(self,conn,addr):
        """
        adding a user
        :param conn: connection object
        :param addr: (str, int) ip and port
        """
        # self.buffer.append([])
        # self._userNum += 1
        pass

    def removeUser(self,conn, addr):
        """
        removing a user
        :param conn: connection object
        :param addr: (str, int) ip and port
        """
        pass



    def msgHandle(self):
        """
        sending messages in buffer
        """
        pass
