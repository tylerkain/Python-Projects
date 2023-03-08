import subprocess

def monitor_mode(interface): 
    '''enable monitor mode '''
    print(f'changing {interface} to monitor mode')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['iwconfig', interface, 'mode', 'monitor'])
    subprocess.call(['ifconfig', interface, 'up'])