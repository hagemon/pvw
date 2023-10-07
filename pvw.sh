#!/bin/bash

PIPE_NAME="$HOME/.pvw/_envs._cfg"
params=("$@")

# Support shorten command to activate venvs, e.g. source pvw env
if [ "$0" != "$BASH_SOURCE" ] && [ "$1" != "activate" ]; then
    params=("activate" "${params[@]}")
fi

if [ $# -gt 0 ]
then
    # python -m cProfile -s time main.py "${params[@]}" # for evaluating execution time
    pvw_py "${params[@]}"
    if [[ "${params[0]}" == "activate" ]] && [ -f "$PIPE_NAME" ]
    then
        # activate parameter will create a _envs._cfg file as a pipe to make communication between parent/child process.
        ps1Path=$(cat "$PIPE_NAME")
        source "$ps1Path"
    fi
    rm -f "$PIPE_NAME"
else
    pvw_py
fi