#!/bin/bash

shells=("bash", "sh", "zsh")

output_file="running_shell_scripts.log"

echo "Checking for running shell scripts" > "$output_file"

ps -ef | grep -E "$(IFS="|"; echo "${shells[*]}")" | grep -v grep >> "$output_file"

echo "Finished scanning running scripts. Results have written to $output_file"
