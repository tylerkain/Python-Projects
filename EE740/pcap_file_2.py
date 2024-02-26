import pyshark


def list_unsuccessful_ftp_logins(pcap_file_path, display_filter='ftp.response.code == 530'):
    """
    Lists packet numbers and their corresponding source/destination IP addresses for unsuccessful FTP login attempts
    indicated by FTP response code 530.

    :param pcap_file_path: The file path to the pcap file.
    """
    cap = pyshark.FileCapture(pcap_file_path, display_filter=display_filter)

    packet = cap[0]
    print(packet)

    link_layer = packet.layers[0]
    print(f"Link Layer: {link_layer.layer_name}")

    cap.close()


pcap_file_path = "pcap_file2.pcapng"  # Replace with your actual file path
list_unsuccessful_ftp_logins(pcap_file_path)
