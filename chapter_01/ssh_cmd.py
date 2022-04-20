from http import client
from sys import stderr, stdout
import paramiko


def ssh_command(ip, port, user, password, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,port=port,username=user,password=password)
    
    
    _, stdout, stderr = client.exec_command(cmd)
    output =stdout.readline() + stderr.readline()
    
    if output:
        print("----OUTPUT---")
        
        #print(output)
        
        for line in output:
            print(line.strip())


def main():
    import getpass
    user =input("Username :")
    #user = getpass.getuser() - to get user name from host username
    password = getpass.getpass() # password won't be visible while typing
    
    
    ip = input("Enter server ip : ")
    port = input("Port No : ") or 22
    cmd = input("Enter Command  : ") or 'id'
    ssh_command(ip, port, user, password, cmd)
    
            
            
if __name__ == "__main__":
    main()