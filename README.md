# Proof of concept for Smurf Attack on IPv4 and IPv6

For this attack we wanted to observe how an amplifier network is able to
CPU throttle a virual machine/server and increase the response time.

For this PoC we created a setup of vms for linux and windows using a
Ubuntu 18.04.6 Server image from [osboxes.org](https://www.osboxes.org/).
We are going to configure 2 network adapters on them: Bridged Adapter and
Host Only Adapter.

First we boot only one vm and we install the required packages:

```
sudo apt-get install nmap hping3 thc-ipv6 python3-pip ssh
```

Then we are going to install the required python modules:

```
pip install scapy
```

Then we have to make sure that the following network tunables are disabled:

```
net.ipv4.icmp_echo_ignore_all
net.ipv4.icmp_echo_ignore_broadcasts
net.ipv4.icmp_ratelimit
net.ipv6.icmp.echo_ignore_multicast
net.ipv6.icmp.echo_ignore_all
net.ipv6.icmp.ratelimit
```

Notice: depending on the OS version some of those may not be enabled/installed
already.

Then we have to clone the vms an change their names and hostnames in order to distinguish them.

In the folder `scripts` we can find the python scripts used to test if the infrastructure is
vulnerable.

In `proofs` are added screenshots and recordings with our attempts.