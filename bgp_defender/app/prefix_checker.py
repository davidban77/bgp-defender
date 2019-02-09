# Fuction that passes an ip prefix as and spits it out as a netaddr object
import argparse
import netaddr
from netaddr import IPAddress, IPNetwork


parser = argparse.ArgumentParser(
    description="Introduce the ip address to validate. this might be a public ip address")
parser.add_argument('-ip', '--ip_address', type=str,
                    required=True, help="add ip address to validate")
parser.add_argument('-mask', '--subnet_mask', type=str, required=False,
                    help='subnet mask in four octect format. ie: 255.255.255.255')
parser.add_argument('-len', '--prefix_len', type=int, required=False,
                    help='prefix lenght of the subnet mask. ie: 32')
args = parser.parse_args()


def ip_checker(ip_address):
    try:
        if not IPAddress(args.ip_address).is_private():
            ip_address = IPAddress(args.ip_address)
            return ip_address
        else:
            print('ip address provided not public')
    except netaddr.core.AddrFormatError:
        print(
            f'AddrFormatError: failed to detect a valid IP address from {ip_address}')
        return False


def mask_checker(mask):
    try:
        subnet_mask = IPAddress(args.subnet_mask)
        if subnet_mask.is_netmask() == True:
            return subnet_mask
        else:
            print(f'{args.subnet_mask} is not a valid mask')
            return False
    except netaddr.core.AddrFormatError:
        print(f'failed to detect a valid subnet mask from {mask}')
        return False


def prefixlen_checker(prefix_len):
    try:
        prexlen = IPNetwork(args.ip_address)
        prexlen.prefixlen = args.prefix_len
        return prexlen
    except netaddr.core.AddrFormatError:
        print(f'AddrFormatError: {args.prefix_len} is not a valid prefixlen')
        return False


def main():
    if args.prefix_len:
        return(prefixlen_checker(args.prefix_len))
    elif args.subnet_mask:
        if mask_checker(args.subnet_mask) == False or None:
            pass
        else:
            ipprefix = IPNetwork(
                str(ip_checker(args.ip_address)) + '/' + str(mask_checker(args.subnet_mask)))
            return(ipprefix)
    elif ip_checker(args.ip_address) == False:
        pass
    else:
        return(IPNetwork(ip_checker(args.ip_address)))
