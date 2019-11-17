#https://gist.github.com/batok/2352501
#Connecting to server over ssh using pem file
import paramiko
import os
import time
from contextlib import closing

print(os.getcwd())
k = paramiko.RSAKey.from_private_key_file("./unencrypted_openssh.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
c.connect( hostname = "34.89.43.76", username = "ec2-user", pkey = k )
print("connected")
commands = [ "ls -l","cd hadoopmigration && pwd && ls -l" ]
for command in commands:
	print("Executing {}".format( command ))
	stdin , stdout, stderr = c.exec_command(command)
	while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
            time.sleep(1)
 
	stdoutstring = stdout.readlines()
	print( stdoutstring)
	stderrstring = stderr.readlines()
	print( stderrstring)
	print("-------------------------------------------------------")
	stdout.flush()
c.close()

# use sftp that is better with above using command all the command one by one will be
# be executed from /home/ec2-user/

print("-------------------------")
with closing(c.open_sftp()) as sftp:
	# cd into remote directory
	sftp.chdir("hadoopmigration")
	# download all files in it to destdir directory
	for filename in sftp.listdir():
		print(filename)