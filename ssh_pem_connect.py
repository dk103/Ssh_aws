#https://gist.github.com/batok/2352501
#Connecting to server over ssh using pem file
import paramiko
k = paramiko.RSAKey.from_private_key_file("./unencrypted_openssh.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
c.connect( hostname = "34.89.43.76", username = "ec2-user", pkey = k )
print("connected")
commands = [ "hadoop fs -ls /" ]
for command in commands:
	print("Executing {}".format( command ))
	stdin , stdout, stderr = c.exec_command(command)
	print(stdout.read())
	print( "Errors")
	print(stderr.read())
c.close()