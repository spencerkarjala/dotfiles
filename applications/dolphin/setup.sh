#!/bin/bash
systemd_target_path="$HOME/.config/systemd/user"
startup_target_path="$HOME/.config/plasma-workspace/env"
script_path="$(realpath "$0")"
source_path="$(dirname "$script_path")"
systemd_file_name='dolphin-runner.service'
startup_file_name='import-gui-session.sh'

mkdir -p "$systemd_target_path"
mkdir -p "$startup_target_path"

rm -f "$systemd_target_path/$systemd_file_name"
rm -f "$startup_target_path/$startup_file_name"
ln -s "$source_path/$systemd_file_name" "$systemd_target_path/$systemd_file_name"
ln -s "$source_path/$startup_file_name" "$startup_target_path/$startup_file_name"

systemctl --user daemon-reload
systemctl --user enable --now dolphin-runner.service

