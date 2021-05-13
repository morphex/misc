#!/usr/bin/env python3

# Script that will build/run an external command to migrate IMAP email from
# one server to another. Only IMAPS, IMAP over SSL is supported.
#
# TODO
#
# Look at how folder names with international, non-ASCII characters are
# handled correctly.
#
# Prints a shell script that will run
#
#   https://github.com/imapsync/imapsync
#

import imaplib, getopt, sys

def setup_connection(host):
    return imaplib.IMAP4_SSL(host)

def print_help():
    print("migrate-imap hostnamefrom usernamefrom passwordfrom")
    print("             [--listfolders]")
    print("             [--hostnameto hostnameto]")
    print("             [--usernameto usernameto]")
    print("             [--passwordto passwordto]")
    print("             [--excludefolder folder]")
    print("             [--excludefoldersisrecursive]")
    print()
    print("If --listfolders is specified, do nothing else but list source"\
          " folders and exit.")

if __name__ == '__main__':
    try:
        hostname_from, host_from_username, host_from_password = sys.argv[1:4]
    except ValueError:
        print_help()
        sys.exit(1)
    hostname_to = host_to_username = host_to_password = ''
    excluded_folders_is_recursive = list_folders = False
    arguments = sys.argv[4:]
    excluded_folders = []
    options, arguments = getopt.getopt(arguments, "", ["listfolders",
	"hostnameto=", "usernameto=", "passwordto=", "excludefolder=",
        "excludedfoldersisrecursive"])
    for options_, arguments in options:
        if options_ == '--listfolders':
            list_folders = True
        if options_ == '--excludedfoldersisrecursive':
            excluded_folders_is_recursive = True
        if options_ == '--excludefolder':
            excluded_folders.append(arguments)
        if options_ == '--hostnameto':
            hostname_to = arguments
        if options_ == '--usernameto':
            host_to_username = arguments
        if options_ == '--passwordto':
            host_to_password = arguments
    connection = setup_connection(hostname_from)
    connection.login(host_from_username, host_from_password)
    all_folders = []
    folders = connection.list()[1]
    for folder in folders:
        folder = folder.decode()
        folder_name = str(folder).split('"."')[-1].strip()
        all_folders.append(folder_name[1:-1])
    if len(all_folders) == 0:
        print('No folders to migrate')
        sys.exit(1)
    if list_folders:
        print(all_folders)
        sys.exit(0)
    exclude = []
    for folder in all_folders:
        for excluded_folder in excluded_folders:
            if excluded_folders_is_recursive:
                if folder.startswith(excluded_folder):
                    exclude.append(folder)
            else:
                if folder == excluded_folder:
                    exclude.append(folder)
    for folder in exclude:
        all_folders.remove(folder)
    print('#!/bin/sh')
    print()
    print('# Excluded folders')
    print('# ', end='')
    print()
    print(exclude)
    print('# Excluded folders and matching folders: %i %i' % (
            len(excluded_folders), len(exclude)))
    print('#')
    print()
    print('./imapsync -host1 %s \\' % hostname_from)
    print('  -user1 %s -password1 %s \\' % (host_from_username,
                host_from_password))
    print('  -host2 %s -user2 %s -password2 %s \\' % (hostname_to,
                host_to_username, host_to_password), end='')
    for folder in all_folders:
        print('\n  -folder %s \\' % folder, end='')
    print()
    print()
