# Ssh_aws
SSh_pem_connect:-

External link for refernce:-
AWS File transfer:- https://medium.com/better-programming/transfer-file-from-ftp-server-to-a-s3-bucket-using-python-7f9e51f44e351
Connecting to server over ssh using pem file

Using the Putty Private key (ppk) file to connect to remote server ovser ssh
PROBLEM:-
  Doing so putty private key is not possess the same private key format that corresponds to openSSH private key format

Resolution:- 
  Convert the PPK format to openSSH format so that ssh can recognize the key format 
  
Approach:-
  1:- using putty client is one the ways
  2:- convert the ppk file Pem formatted file
  
once converted to pem file then u can use normal ssh way to connect to remote server using pem file as reference

 
