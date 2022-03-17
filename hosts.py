import csv
import os.path
import sys


def hostsinput(filename):
    with open(filename, 'r') as file:
        for row in file:
            dfrow = input("Enter in cfg name, ex df-17.cfg: ")
            split_hostname = row.split(".",1)
            hostname_only = split_hostname[0]
            file = open(dfrow, 'a')
            with open(dfrow) as readfile:
                if row in readfile.read():
                    print(row + "Already exists")
                    continue
                else:
                    file.write(f"\ndefine host {{ \nuse linux-server\nhostname {hostname_only}\nalias {hostname_only}\naddress {row}hostgroup linux-desktops\n}}\n")
                    print(row + "Added.")
                    file.close()

hostsinput(input("Enter in csv-file: "))

