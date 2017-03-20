class Client(object):
    
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
    
    def __enter__(self):
        import smtplib
        self.client = smtplib.SMTP()
        self.client.connect(self.server)
        self.client.login(self.username, self.password)
        return self.client
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.quit()
