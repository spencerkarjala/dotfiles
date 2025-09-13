#!/usr/bin/env python3

import sys
from typing import List

def install_scripts():
    print("Installing all scripts...")
    # Placeholder for scripts installation logic

target_map = {
    'scripts': install_scripts,
    # Add more targets and their corresponding functions here
}

def install_targets(targets: List[str]) -> None:
    for target in targets:
        if target in target_map:
            target_map[target]()
        else:
            print(f"Unknown target: {target}")

def install_all():
    print("Installing all components...")
    install_targets(target_map.keys())

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
