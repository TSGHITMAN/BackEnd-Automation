import paramiko as paramiko
from utilities.configuration import *
# connection setup
username = getConfig()['ssh']['username']
password = getConfig()['ssh']['password']
host = getConfig()['ssh']['host']
port = getConfig()['ssh']['port']
ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# run commands
stdin, stdout, stderr = ssh.exec_command("ls -a")
print(stdout.readlines())

# upload file
sftp = ssh.open_sftp()
destinationPath = "script.py"
localPath = "batchfiles/script.py"
sftp.put(localPath, destinationPath)
ssh.close()





