from __future__ import print_function

import os
import subprocess
import sys


def ping_subnet(subnet, ping_function=None):
    """Scan a subnet using an injectable ping function."""

    if ping_function is None:
        ping_function = subprocess.call

    if os.name == "posix":
        myping = "ping -c 2 "
    elif os.name in ("nt", "dos", "ce"):
        myping = "ping -n 2 "
    else:
        raise OSError("Unsupported operating system")

    filename = "ping_" + subnet + ".log"

    with open(filename, "w") as log_file:
        for ip in range(2, 255):
            command = myping + subnet + "." + str(ip)

            ret = ping_function(
                command,
                shell=True,
                stdout=log_file,
                stderr=subprocess.STDOUT,
            )

            if ret == 0:
                log_file.write(subnet + "." + str(ip) + " is alive\n")
            else:
                log_file.write(
                    subnet + "." + str(ip) + " did not respond\n"
                )


def main(argv=None):
    if argv is None:
        argv = sys.argv

    filename = argv[0]

    if (
        "-h" in argv
        or "--h" in argv
        or "-help" in argv
        or "--help" in argv
    ):
        print(
            "\nYou need to supply the first octets of the address Usage : "
            + filename
            + " 111.111.111 "
        )
        return

    if len(argv) < 2:
        sys.exit(
            " You need to supply the first octets of the address Usage : "
            + filename
            + " 111.111.111"
        )

    subnet = argv[1]
    ping_subnet(subnet)


if __name__ == "__main__":
    main()
