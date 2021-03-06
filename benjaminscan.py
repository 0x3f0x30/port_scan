import socket
import argparse
from termcolor import colored

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def main():
   p = argparse.ArgumentParser(description="single port scan",
                               epilog="author : BenjaminDG")
   p.add_argument("--host",
                  type=str,
                  dest="host",
                  help="masukan target")

   p.add_argument("--port",
                  type=int,
                  dest="port",
                  help="masukan port")
   inp = p.parse_args()
   print()

   try:
       s.connect((inp.host,inp.port))
       print(colored(f"[+] {inp.host}:{inp.port} terbuka","green"))
   except:
       print(colored(f"[-] {inp.host}:{inp.port} tertutup","red"))

   

if __name__ == "__main__":
    main()



