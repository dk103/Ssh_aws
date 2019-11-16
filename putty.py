#ref:-https://medium.com/better-programming/transfer-file-from-ftp-server-to-a-s3-bucket-using-python-7f9e51f44e35

import paramiko

def open_ftp_connection(ftp_host, ftp_port, ftp_username): 
#   ...
#   Opens ftp connection and returns connection object
#   ...
  client = paramiko.SSHClient()
  k = paramiko.RSAKey.from_private_key_file("./unencrypted_openssh.pem")
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  print("connecting")
  client.load_system_host_keys() 
  client.connect( hostname = "34.89.43.76", username = "ec2-user", pkey = k )
  print('connected')
  commands = [ "hadoop fs -ls /" ]
  for command in commands:
      print("Executing {}".format( command ))
      stdin , stdout, stderr = client.exec_command(command)
      print(stdout.read())
      print( "Errors")
      print(stderr.read())
  ftp_client =None
  try: 
    ftp_client = client.open_sftp()
  except Exception as e: 
     return 'conn_error' 
  with  ftp_client.open('src1.txt') as remote_file:
         for line in remote_file:
            print(line)
         print(remote_file._get_size())

  return None ,None

val,tran = open_ftp_connection("34.89.43.76",22,"ec2-user")
