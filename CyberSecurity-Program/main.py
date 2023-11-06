# Importing the necessary modules
from mac_changer import MacChanger
from portscanner import PortScan

def main():
    tool_choices = {
        "1": {
            "tool_name": "MAC Changer Tool",
            "input_prompt": "[+] Input interface to change MAC address: ",
            "tool_class": MacChanger,
            "tool_method": "run"
        },
        "2": {
            "tool_name": "PortScanner",
            "input_prompt": "[+] Input IP address: ",
            "port_prompt": "[+] Input Port range: ",
            "tool_class": PortScan,
            "tool_method": "scan"
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

            if "port_prompt" in tool_data:  # Check if PortScanner tool is chosen
                port_range = input(tool_data['port_prompt'])
                tool_instance = tool_class(input_value, port_range)  # Initialize PortScan instance
                getattr(tool_instance, tool_method)()  # Call the scan method
            else:  # MAC Changer tool is chosen
                tool_instance = tool_class(input_value)  # Initialize MacChanger instance
                getattr(tool_instance, tool_method)()  # Call the run method
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
