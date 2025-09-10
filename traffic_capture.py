# from scapy.all import sniff

# def packet_callback(packet):
#     try:
#         src = packet[0][1].src
#         dst = packet[0][1].dst
#         proto = packet[0][1].name
#         size = len(packet)
#         print(f"Source: {src}, Destination: {dst}, Protocol: {proto}, Size: {size} bytes")
#     except Exception as e:
#         print("Packet skipped:", e)

# sniff(prn=packet_callback, count=10)


#old=======================================================

from scapy.all import sniff
import socket

def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return ip

def packet_callback(packet):
    try:
        src = packet[0][1].src
        dst = packet[0][1].dst
        proto = packet[0][1].name
        size = len(packet)
        dst_name = resolve_hostname(dst)
        print(f"Source: {src}, Destination: {dst_name}, Protocol: {proto}, Size: {size} bytes")
    except Exception as e:
        print("Packet skipped:", e)

sniff(prn=packet_callback, count=10)
