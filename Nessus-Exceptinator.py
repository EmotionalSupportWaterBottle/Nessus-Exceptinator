#!/bin/python3
### FOR ETHICAL PURPOSES ONLY ###
### https://github.com/EmotionalSupportWaterBottle ###
import ipaddress

def generate_ip_list(cidr, exclude_ips):
    """
    Generate a list of IP ranges from a CIDR block, excluding specific IPs or subnets.

    Args:
        cidr (str): CIDR notation representing the IP range (e.g., "192.168.1.0/22").
        exclude_ips (list): List of IPs or subnets to exclude (e.g., ["192.168.1.5", "192.168.2.0/24"]).

    Returns:
        list: A list of IP ranges or individual IPs as strings.
    """
    try:
        # Convert the CIDR range to an iterable list of IP addresses
        network = ipaddress.ip_network(cidr, strict=False)
    except ValueError as e:
        raise ValueError(f"Invalid CIDR notation: {cidr}") from e

    # Expand exclude_ips to handle individual IPs and subnets
    excluded = set()
    for ip in exclude_ips:
        try:
            if '/' in ip:
                # It's a subnet
                ip_obj = ipaddress.ip_network(ip, strict=False)
                excluded.update(ip_obj.hosts())
            else:
                # It's a single IP
                excluded.add(ipaddress.ip_address(ip))
        except ValueError:
            raise ValueError(f"Invalid IP or subnet in exclude_ips: {ip}")

    # Filter out the excluded IPs
    filtered_ips = [ip for ip in network.hosts() if ip not in excluded]

    # Format consecutive IPs into ranges
    ip_ranges = format_ip_ranges(filtered_ips)

    return ip_ranges

def format_ip_ranges(ip_list):
    """
    Format a list of IPs into ranges.

    Args:
        ip_list (list): List of IP address objects.

    Returns:
        list: A list of IP ranges or individual IPs as strings.
    """
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
    """
    Format a range of IPs as a string.

    Args:
        start_ip (IPv4Address or IPv6Address): Start IP of the range.
        end_ip (IPv4Address or IPv6Address): End IP of the range.

    Returns:
        str: Formatted range (e.g., "192.168.1.1-192.168.1.10" or "192.168.1.1").
    """
    if start_ip == end_ip:
        return str(start_ip)
    else:
        return f"{start_ip}-{end_ip}"

# Example usage
if __name__ == "__main__":
    cidr = "x.x.x.x/x"
    exclude_ips = ["x.x.x.x", "x.x.x.x/x", "x.x.x.x"]

    try:
        ip_list = generate_ip_list(cidr, exclude_ips)
        print("\n".join(ip_list))
    except ValueError as e:
        print(f"Error: {e}")
