param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$params
)

$PIPE_NAME= ".\_envs._cfg"

if ($params.Length -gt 0) {
    & "python" "main.py" $params
    if (($params[0] -eq "activate") -and (Test-Path $PIPE_NAME)) {
        # activate parameter will create a _envs._cfg file as a pipe to make communication between parent/child process.
        $ps1Path = Get-Content "_envs._cfg"
        & $ps1Path
        Remove-Item $PIPE_NAME
    }
}
else {
    & "python" "main.py"
}

