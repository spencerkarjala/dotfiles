#!/usr/bin/env python3

import sys

def install_all():
    print("Installing all components...")

def install_targets(targets):
    for target in targets:
        print(f"Installing {target}...")

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print("Usage: ./install.py <all|target1 target2 ...>")
        sys.exit(1)

    if sys.argv[1] == 'all':
        install_all()
    else:
        install_targets(sys.argv[1:])

if __name__ == "__main__":
    main()
