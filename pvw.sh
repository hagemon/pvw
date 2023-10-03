#!/bin/bash

PIPE_NAME="./_envs._cfg"
params=("$@")

if [ $# -gt 0 ]
then
    # python -m cProfile -s time main.py "${params[@]}" # for evaluating execution time
    ./pvw_py "${params[@]}"
    if [[ "${params[0]}" == "activate" ]] && [ -f "$PIPE_NAME" ]
    then
        # activate parameter will create a _envs._cfg file as a pipe to make communication between parent/child process.
        ps1Path=$(cat "_envs._cfg")
        "$ps1Path"
        rm "$PIPE_NAME"
    fi
else
    ./pvw_py
fi