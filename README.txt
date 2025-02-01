FOR ETHICAL PURPOSES ONLY

This tool was created to streamline the process of breaking out the IP space of an organization's network for use by security professionals who use Nessus as a scanning tool. It takes the IP space you provide it, and curates a hyphenated block of IP ranges, excluding all of the exceptions you input. Please make sure to double check the result provided by the script before firing your scans off against those IP ranges.

Here is an example of what this script will do with the following input:

	if __name__ == "__main__":
		ip_range = "10.10.10.0/10" ### Can be CIDR notation or a hyphenated range ###
		exclude_ips = ["10.10.10.90", "10.10.10.252-10.10.11.60", "10.10.15.0/24"]  ### Can be CIDRs, ranges, or single IPs ###


Here is the result it provides given the above input:

	10.0.0.1-10.10.10.89
	10.10.10.91-10.10.10.251
	10.10.11.61-10.10.15.0
	10.10.15.255-10.63.255.254

Once you return the above list, you can copy and paste it directly into the targets list in your Nessus scans. 
