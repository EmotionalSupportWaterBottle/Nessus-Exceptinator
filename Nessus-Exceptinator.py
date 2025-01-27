#!/bin/python3
### FOR ETHICAL PURPOSES ONLY ###
### https://github.com/EmotionalSupportWaterBottle ###
import ipaddress

def generate_ip_list(cidr, exclude_ips):
    # Convert the CIDR range to an iterable list of IP addresses
    network = ipaddress.ip_network(cidr, strict=False)
    exclude_ips = {ipaddress.ip_address(ip) for ip in exclude_ips}
    
    # Filter out the excluded IPs
    filtered_ips = [ip for ip in network if ip not in exclude_ips]
    
    # Format consecutive IPs into ranges
    ip_ranges = format_ip_ranges(filtered_ips)
    
    return ip_ranges

def format_ip_ranges(ip_list):
    if not ip_list:
        return []

    result = []
    start_ip = prev_ip = ip_list[0]

    for ip in ip_list[1:]:
        if int(ip) != int(prev_ip) + 1:
            result.append(format_range(start_ip, prev_ip))
            start_ip = ip
        prev_ip = ip

    # Add the last range or IP
    result.append(format_range(start_ip, prev_ip))
    
    return result

def format_range(start_ip, end_ip):
    if start_ip == end_ip:
        return str(start_ip)
    else:
        return f"{start_ip}-{end_ip}"

# Example usage
if __name__ == "__main__":
    cidr = "x.x.x.x/x"
    exclude_ips = ["x.x.x.x", "x.x.x.x", "x.x.x.x", "x.x.x.x", "x.x.x.x", "x.x.x.x", "x.x.x.x", "x.x.x.x", "x.x.x.x"]

    ip_list = generate_ip_list(cidr, exclude_ips)
    print("\n".join(ip_list))

