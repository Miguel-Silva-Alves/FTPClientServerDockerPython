# Import Module
import ftplib



class FTPConnection():
    def __init__(self, host="0.0.0.0", user="user", password="123123", port=None) -> None:
        self.ftpserver = None
        self.host = host
        self.user = user
        self.password = password
        self.port = port
    
    def connect(self):
        self.ftpserver = ftplib.FTP(self.host)
        self.ftpserver.connect(host=self.host, port=self.port)
        self.ftpserver.login(user=self.user, passwd=self.password)
        self.ftpserver.encoding = "utf-8"
    
    def getFiles(self, pwd="/"):
        if pwd != "/":
            self.ftpserver.cwd('files/')
        return self.ftpserver.dir()
    
    def saveFile(self, path):
        # Read file in binary mode
        try:
            with open(path, "rb") as file:
                # Command for Uploading the file "STOR filename"
                self.ftpserver.storbinary(f"STOR {path}", file)
            return True
        except Exception as e:
            print(str(e))
            return False

    def getFile(self, inp, out):
        
        
        try:
            # Write file in binary mode
            with open(out, "wb") as file:
                # Command for Downloading the file "RETR filename"
                self.ftpserver.retrbinary(f"RETR {inp}", file.write)
            return True
        except Exception as e:
            print(str(e))
            return False
    
    def close(self):
        self.ftpserver.quit()


print("TEST FTP Connection")

# Fill Required Information
HOSTNAME = "0.0.0.0"
USERNAME = "user"
PASSWORD = "123"
PORT = 21

ftp = FTPConnection(HOSTNAME, USERNAME, PASSWORD, PORT)
ftp.connect()

# GET FILES
ftp.getFiles()

# # UPLOAD FILE

# filename = "TEST.txt"
# if ftp.saveFile(filename):
#     print('Save')
# else:
#     print('Not save')

# # DOWNLOAD FILE

# filenameInp = "TEST.txt"
# filenameOut = "recuperado.txt"

# if ftp.getFile(filenameInp, filenameOut):

#     # Display the content of downloaded file
#     file= open(filenameOut, "r")
#     print('File Content:', file.read())
# else:
#     print("Not found!")


ftp.close()