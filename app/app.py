from flask import Flask, jsonify
from collections import Counter
from scapy.all import sniff, IP, UDP, TCP, ARP, Ether
import threading

app = Flask(__name__)

# Global variable stores captured packets
packets = []

# Process packets
def packet_callback(packet):
    if IP in packet:
        protocol_map = {6: "TCP", 17: "UDP"}
        real_protocol = protocol_map.get(packet[IP].proto, "Unknown protocol")

        packets.append({
            "source": packet[IP].src,
            "destination": packet[IP].dst,
            "protocol": real_protocol,
            "length": packet[IP].len
        })

# Capture packets
def sniff_packets(interface):
    sniff(iface=interface, prn=packet_callback, store=False)

@app.route('/packets', methods=['GET'])
def get_packets():
    return jsonify(packet_filter(packets)) 

def packet_filter(packets):
    
    # Amount of captured packets
    total_packets = len(packets)

    # Number of packets by Protocol
    protocol_count = Counter(packet['protocol'] for packet in packets)

    # Top 5 most frecuents origin IP adresses
    source_ips = Counter(packet['source'] for packet in packets)
    top_frecuent_src_ips = source_ips.most_common(5)
    
    # Top 5 most frecuents destination IP adresses
    source_dst = Counter(packet['destination'] for packet in packets)
    top_frecuent_dst_ips = source_dst.most_common(5)

    filtered_packets = {
        'total_packets': total_packets,
        'protocol_count': dict(protocol_count),
        'top5_frecuent_src_ips': top_frecuent_src_ips,
        'top5_frecuent_dst_ips': top_frecuent_dst_ips
    }

    return filtered_packets

if __name__ == "__main__":
    
    # Change the network connection manually
    interface = 'lo'

    # Start sniffing in a separate thread
    sniff_thread = threading.Thread(target=sniff_packets, args=(interface,), daemon=True)
    sniff_thread.start()

    # Start Flask app
    app.run(host='0.0.0.0', port=80)