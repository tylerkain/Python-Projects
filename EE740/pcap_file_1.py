import pyshark


def print_first_filtered_packet(pcap_file_path, display_filter='http.request.method == "POST"'):
    """
    Prints the first packet that matches the display filter from a pcap file and information about its link layer.

    :param pcap_file_path: The file path to the pcap file.
    :param display_filter: The display filter to apply. Defaults to filtering HTTP POST requests.
    """
    cap = pyshark.FileCapture(pcap_file_path, display_filter=display_filter)

    packet = cap[0]
    print(packet)

    link_layer = packet.layers[0]
    print(f"Link Layer: {link_layer.layer_name}")

    cap.close()


pcap_file_path = "pcap_file1.pcapng"  # Replace with your actual file path
print_first_filtered_packet(pcap_file_path)
