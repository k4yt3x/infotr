# infotr

A traceroute tool that also displays IP information.

This tool has only been tested on Linux.

![image](https://user-images.githubusercontent.com/21986859/120411515-f1533a80-c322-11eb-81a6-a57b9cfbcde5.png)

## Quick Start

First, install this tool from PyPI.

```shell
pip install --user -U infotr
```

Since Scapy needs to open raw sockets, this tool requires Python to have the `CAP_NET_RAW` capability to run. You can also run this tool as root. Run the following commands to set/unset the `CAP_NET_RAW` capability for the Python binary. Remember to unset the capability when you're done.

```shell
# set the capability
sudo setcap cap_net_raw=+eip /usr/bin/python3.9

# remove the capability
sudo setcap cap_net_raw=-eip /usr/bin/python3.9
```

Finally, launch this tool via the `infotr` command.

```shell
infotr 1.1.1.1
```

## Full Usages

You can also see the help messages with the `-h/--help` switch.

```console
usage: infotr [-h] [-m MAX] [-t TIMEOUT] host

positional arguments:
  host                  destination hostname

optional arguments:
  -h, --help            show this help message and exit
  -m MAX, --max MAX     maximum number of hops (default: 30)
  -t TIMEOUT, --timeout TIMEOUT
                        ICMP timeout in seconds (default: 2)
```
