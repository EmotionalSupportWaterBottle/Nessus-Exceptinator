FOR ETHICAL PURPOSES ONLY

This tool was created to streamline the process of breaking out the IP space of an organization's network for use by security professionals who use Nessus as a scanning tool. It takes the IP space you provide it, and curates a hyphenated block of IP ranges, excluding all of the exceptions you input. Please make sure to double check the result provided by the script before firing your scans off against those IP ranges.

Here is an example of what this script will do when it is run:
./Nessus-Exceptinator.py 
Enter IP ranges (comma-separated): 192.168.0.0/16,10.10.10.10-10.10.19.5
Enter IPs to exclude (comma-separated): 192.168.0.0/20,192.168.5.9-192.168.8.5,10.10.10.9
10.10.10.10-10.10.19.5
192.168.15.255-192.168.255.254

Once you return the above list, you can copy and paste it directly into the targets list in your Nessus scans. 
