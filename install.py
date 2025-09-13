#!/usr/bin/env python3

import sys
from pathlib import Path
import os
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

    print("...done.")

def install_aider_main_config():
    print("Installing aider main config...")

    xdg_config_home = Path(os.getenv('XDG_CONFIG_HOME', Path.home() / '.config'))
    aider_config_file = xdg_config_home / 'aider' / '.aider.conf.yaml'
    aider_config_file.parent.mkdir(parents=True, exist_ok=True)

    source_config_file = Path('aider/config.yaml')

    if aider_config_file.is_file():
        aider_config_file.unlink()

    aider_config_file.write_text(source_config_file.read_text())
    aider_config_file.chmod(0o600)

    openai_api_key = input("Please enter your OpenAI API key: ")

    with aider_config_file.open('r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.startswith('openai-api-key:'):
                file.write(f'openai-api-key: {openai_api_key}\n')
            else:
                file.write(line)
        file.truncate()

    aider_config_file.chmod(0o400)

    print("...done.")

def install_aider_conventions():
    print("Installing aider conventions...")

    xdg_config_dir = Path(os.getenv('XDG_CONFIG_DIR', Path.home() / '.config'))
    aider_config_dir = xdg_config_dir / 'aider'
    aider_config_dir.mkdir(parents=True, exist_ok=True)

    conventions_file = Path('aider/conventions')
    conventions_link_path = aider_config_dir / 'aider-conventions.txt'

    if conventions_link_path.is_symlink():
        conventions_link_path.unlink()

    conventions_link_path.symlink_to(conventions_file)

    print(f"Created symlink at {conventions_link_path} to conventions file {conventions_file}")

    print("...done.")

def install_aider_configs():
    install_aider_conventions()
    install_aider_main_config()

target_map = {
    'scripts': install_scripts,
    'aider': install_aider_configs,
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
