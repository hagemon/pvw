param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$params
)

$PIPE_NAME = "$HOME\.pvw\_envs._cfg"

if ($params.Length -gt 0) {
    # & "python" "-m" "cProfile" "-s" "time" "main.py" $params # for evaluating execution time
    & pvw-py $params
    if (($params[0] -eq "activate") -and (Test-Path $PIPE_NAME)) {
        # activate parameter will create a _envs._cfg file as a pipe to make communication between parent/child process.
        $ps1Path = Get-Content $PIPE_NAME
        & $ps1Path
        Remove-Item $PIPE_NAME
    }
}
else {
    & pvw-py
}

