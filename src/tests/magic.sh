# pvw wrapper start
alias pvw="pvw_wrapper"

function pvw_wrapper {
        local commands=("ls" "rm" "create" "cp" "mv" "config")
        if [ "$1" = "activate" ]; then
                shift
                source pvw "$@"
        elif [ $# -gt 0 ] && [[ ! " ${commands[@]} " =~ " $1 " ]] && [ "${1:0:1}" != "-" ]; then
                source pvw activate "$@"
        else
                command pvw "$@"
        fi
}
# pvw wrapper end