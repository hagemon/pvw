import argparse
from pvw.op import Operation

parser = argparse.ArgumentParser(prog="pvw", description="Manage python venv environments.", formatter_class=argparse.RawTextHelpFormatter)
subparsers = parser.add_subparsers(dest="command")

# list
list_parser = subparsers.add_parser("ls", help="list all venvs.")
list_parser.add_argument(
    "--show-size", action="store_true", help="whether show sizes of each venv."
)

# config
config_parser = subparsers.add_parser("config", help="get or set pvw config")
config_subparsers = config_parser.add_subparsers(
    help="config operations", dest="config_command", required=True
)
config_set_parser = config_subparsers.add_parser(
    "set",
    help="set value for config item, e.g. `pvw config set venv_path /PATH/TO/VENV_DIR`",
)
config_set_parser.add_argument(
    "params", nargs="*", help="e.g. venv_path=/PATH/TO/VENV_PATH"
)
config_get_parser = config_subparsers.add_parser(
    "get", help="get value of config item, e.g. `pvw config get venv_path"
)
config_get_parser.add_argument("key", help="avaliable option: {venv_path}")


# activate
activate_parser = subparsers.add_parser("activate", help="""activate venv.\nFor Linux/Mac:\nUse `source pvw activate ENV_NAME` to activate venv\nor simply use `source pvw ENV_NAME`.\n\nFor Windows:\nuse `pvw activate ENV_NAME`""")
activate_parser.add_argument("name", help="venv name.")

# create
create_parser = subparsers.add_parser("create", help="create a new venv.")
create_parser.add_argument("name", help="name of venv to create.")

# remove
remove_parser = subparsers.add_parser("rm", help="remove a venv.")
remove_parser.add_argument("name", help="name of venv to remove.")

# move
move_parser = subparsers.add_parser("mv", help="move(rename) venv to another place.")
move_parser.add_argument("source", help="name of source venv.")
move_parser.add_argument("target", help="name of target venv.")

# copy
copy_parser = subparsers.add_parser("cp", help="copy venv.")
copy_parser.add_argument("source", help="name of source venv.")
copy_parser.add_argument("target", help="name of target venv.")


def parse(version):
    parser.add_argument("-v", "--version", action="version", version=f"pvw version {version}")
    try:
        args = parser.parse_args()
        op = Operation(args)
        if args.command == "create":
            op.create()
        elif args.command == "rm":
            op.remove()
        elif args.command == "mv":
            op.move()
        elif args.command == "cp":
            op.copy()
        elif args.command == "config":
            op.config()
        elif args.command == "ls":
            op.show()
        elif args.command == "activate":
            op.activate()
        else:
            parser.print_help()
    except argparse.ArgumentError:
        parser.print_help()


if __name__ == "__main__":
    parse()
