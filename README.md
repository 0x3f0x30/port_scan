#sebelum pakai,lakukanlah ini

#untuk termux

apt update && upgrade -y

apt install git -y

apt install python -y

pip install sockets argparse termcolor

git clone https://github.com/BenjaminXN/port_scan.git

cd port_scan

python benjaminscan.py --help
