from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("shlomi", "123", "/home/shlomi/Desktop/Shlomi FTP/", perm="elradfmwMT")
#authorizer.add_anonymous("/home/shlomi/Desktop/Shlomi FTP/")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
