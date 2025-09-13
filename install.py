#!/usr/bin/env python3

import sys
from pathlib import Path
from typing import List

def install_scripts():
    print("Installing all scripts...")

    install_dir = Path.home() / '.local' / 'bin'
    scripts_dir = Path.cwd() / 'scripts'

    install_dir.mkdir(parents=True, exist_ok=True)

    source_scripts = [filename for filename in scripts_dir.iterdir() if filename.is_file()]

    for script in source_scripts:
        script_name_no_extension = script.stem
        script_link_path = install_dir / script_name_no_extension

        if script_link_path.is_symlink():
            script_link_path.unlink()

        script_link_path.symlink_to(script)

        print(f"Created symlink at {script_link_path} to script {script.name}")

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
