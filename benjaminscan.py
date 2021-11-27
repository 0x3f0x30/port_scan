import socket
import argparse

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

   try:
       s.connect((inp.host,inp.port))
       print(f"[+] {inp.host}:{inp.port} open")
   except:
       print(f"[-] {inp.host}:{inp.port} close")

   

if __name__ == "__main__":
    main()



