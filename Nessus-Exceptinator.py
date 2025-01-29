#!/bin/python3
### FOR ETHICAL PURPOSES ONLY ###
### https://github.com/EmotionalSupportWaterBottle ###

import ipaddress
import re

def parse_ip_or_range(ip_input):
    """Parse an IP, CIDR, or IP range and return a set of IP addresses."""
    ip_set = set()
    
    # Handle CIDR notation
    if '/' in ip_input:
        try:
            network = ipaddress.ip_network(ip_input, strict=False)
            ip_set.update(network.hosts())
        except ValueError:
            raise ValueError(f"Invalid CIDR notation: {ip_input}")
    
    # Handle IP range (e.g., 192.168.1.10-192.168.1.20)
    elif '-' in ip_input:
        try:
            start_ip, end_ip = ip_input.split('-')
            start_ip, end_ip = ipaddress.ip_address(start_ip), ipaddress.ip_address(end_ip)
            
            if start_ip > end_ip:
                raise ValueError(f"Invalid range: {ip_input}. Start IP must be lower than End IP.")
            
            for ip_int in range(int(start_ip), int(end_ip) + 1):
                ip_set.add(ipaddress.ip_address(ip_int))
        except ValueError:
            raise ValueError(f"Invalid IP range: {ip_input}")
    
    # Handle single IP
    else:
        try:
            ip_set.add(ipaddress.ip_address(ip_input))
        except ValueError:
            raise ValueError(f"Invalid IP address: {ip_input}")
    
    return ip_set

def generate_ip_list(ip_range, exclude_list):
    """
    Generate a list of IP ranges from an IP range, CIDR, or individual IPs, excluding specific IPs or subnets.
    """
    included_ips = parse_ip_or_range(ip_range)
    excluded_ips = set()
    
    for exclude in exclude_list:
        excluded_ips.update(parse_ip_or_range(exclude))
    
    # Compute remaining IPs after exclusion
    remaining_ips = sorted(included_ips - excluded_ips)
    
    return format_ip_ranges(remaining_ips)

def format_ip_ranges(ip_list):
    """Format a sorted list of IPs into hyphenated ranges."""
    if not ip_list:
        return []
    
    result = []
    start_ip = prev_ip = ip_list[0]
    
    for ip in ip_list[1:]:
        if int(ip) != int(prev_ip) + 1:
            result.append(format_range(start_ip, prev_ip))
            start_ip = ip
        prev_ip = ip
    
    # Append last range
    result.append(format_range(start_ip, prev_ip))
    
    return result

def format_range(start_ip, end_ip):
    """Format a range of IPs as a string."""
    return str(start_ip) if start_ip == end_ip else f"{start_ip}-{end_ip}"

# Example Usage
if __name__ == "__main__":
    ip_range = "x.x.x.x/x"
    exclude_ips = ["x.x.x.x", "x.x.x.x-x.x.x.x", "x.x.x.x/x"]  # Can be CIDRs, ranges, or single IPs
    
    try:
        ip_list = generate_ip_list(ip_range, exclude_ips)
        print("\n".join(ip_list))
    except ValueError as e:
        print(f"Error: {e}")
