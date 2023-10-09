import re
import csv
import collections

def open_log_file(file_path):
    with open(file_path) as f :
        log = f.read()
        regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = re.findall(regex,log)
        return ip_list
    

if __name__ == "__main__":
    open_log_file('sysmon-events.json')