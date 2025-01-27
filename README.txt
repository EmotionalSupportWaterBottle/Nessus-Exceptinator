FOR ETHICAL PURPOSES ONLY

This tool was created to streamline the process of breaking out the IP space of an organization's network for use by security professionals who use Nessus as a scanning tool. It takes the IP space you provide it, and curates a hyphenated block of IP ranges, excluding all of the exceptions you input. Please make sure to double check the result provided by the script before firing your scans off against those IP ranges.

Here is an example of what this script will do with the following input:

	cidr = "192.168.1.0/22"
	exclude_ips = ["192.168.2.99", "192.168.1.5"]

Here is the result it provides given the above input:

	192.168.0.0-192.168.1.4
	192.168.1.6-192.168.2.98
	192.168.2.100-192.168.3.255

Once you return the above list, you can copy and paste it directly into the targets list in your Nessus scans. 
