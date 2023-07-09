from mac_changer import MacChanger
from network_scanner import ScanNetworkTool
from scan import WirelessSecurityTool
def main():
    tool_choices = {
        "1": {
            "tool_name": "Wireless Security Tool",
            "input_prompt": "[+] Input Wi-Fi adapter or wireless card: ",
            "tool_class": WirelessSecurityTool,
            "tool_method": "run_wireless_security_tool"
        },
        "2": {
            "tool_name": "Network Scanner Tool",
            "input_prompt": "[+] Input IP address or IP range to scan: ",
            "output_prompt": "[+] Input output file path: ",
            "scan_arguments_prompt": "[+] Input the scan type: ",
            "tool_class": ScanNetworkTool,
            "tool_method": "run_network_scanner"
        },
        "3": {
            "tool_name": "MAC Changer Tool",
            "input_prompt": "[+] Input interface to change MAC address: ",
            "tool_class": MacChanger,
            "tool_method": "run"
        }
    }

    while True:
        print("[+] Choose a tool:")
        for choice, tool_data in tool_choices.items():
            print(f"{choice}. {tool_data['tool_name']}")

        choice = input("Choice (0 to exit): ")

        if choice == '0':
            break

        tool_data = tool_choices.get(choice)
        if tool_data:
            input_value = input(tool_data['input_prompt'])
            tool_class = tool_data['tool_class']
            tool_method = tool_data['tool_method']

            if "output_prompt" in tool_data:
                output_value = input(tool_data['output_prompt'])
                scan_arguments = input(tool_data['scan_arguments_prompt'])
                tool_instance = tool_class(input_value, output_value, scan_arguments)
            else:
                tool_instance = tool_class()
                setattr(tool_instance, 'interface', input_value)

            getattr(tool_instance, tool_method)()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
