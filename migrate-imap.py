#!/usr/bin/env python3

# Script that will build/run an external command to migrate IMAP email from
# one server to another. Only IMAPS, IMAP over SSL is supported.
#
# Incomplete, currently only folder listing on the source server is
# implemented.
#
# TODO
#
# Look at how folder names with international, non-ascii characters are
# handled correctly.

import imaplib, getopt, sys

def setup_connection(host):
    return imaplib.IMAP4_SSL(host)

def print_help():
    print("migrate-imap hostnamefrom fromusername frompassword")
    print("             [--listfolders]")
    print("             [-ht hostnameto] [-htu usernameto] [-htp passwordto]")
    print("             [--excludefolder] [--excludefoldersisrecursive]")
    print()
    print("If --listfolders is specified, do nothing else but list source"\
          " folders and exit.")

if __name__ == '__main__':
    try:
        hostname_from, host_from_username, host_from_password = sys.argv[1:4]
    except ValueError:
        print_help()
        sys.exit(1)
    list_folders = False
    arguments = sys.argv[4:]
    options, arguments = getopt.getopt(arguments, "", ["listfolders",
	"ht", "htu", "htp", "excludefolder", "excludefoldersisrecursive"])
    for options_, arguments in options:
        if options_ == '--listfolders':
            list_folders = True
    connection = setup_connection(hostname_from)
    connection.login(host_from_username, host_from_password)
    if list_folders:
        all_folders = []
        folders = connection.list()[1]
        for folder in folders:
            folder = folder.decode()
            folder_name = str(folder).split('"."')[-1].strip()
            all_folders.append(folder_name[1:-1])
        print(all_folders)
        sys.exit(0)

