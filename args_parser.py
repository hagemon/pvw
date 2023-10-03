import argparse
from op import Operation

parser = argparse.ArgumentParser(description="Manage python venv environments")
subparsers = parser.add_subparsers(dest="command")

# list
list_parser = subparsers.add_parser("ls", help="List all venvs.")
list_parser.add_argument(
    "--show-size", action="store_true", help="Whether show sizes of each venv."
)

# config
config_parser = subparsers.add_parser("config", help="Get or set pvw config")
config_subparsers = config_parser.add_subparsers(
    help="Config operations", dest="config_command", required=True
)
config_set_parser = config_subparsers.add_parser(
    "set",
    help="Set value for config item, e.g. `pvw config set venv_path /PATH/TO/VENV_DIR`",
)
config_set_parser.add_argument(
    "params", nargs="*", help="E.g. venv_path=/PATH/TO/VENV_PATH"
)
config_get_parser = config_subparsers.add_parser(
    "get", help="Get value of config item, e.g. `pvw config get venv_path"
)
config_get_parser.add_argument("key", help="Avaliable option: {venv_path}")


# activate
activate_parser = subparsers.add_parser("activate", help="Activate venv.")
activate_parser.add_argument("name", help="Venv name.")

# create
create_parser = subparsers.add_parser("create", help="Create a new venv.")
create_parser.add_argument("name", help="Name of venv to create.")

# remove
remove_parser = subparsers.add_parser("rm", help="Remove a venv.")
remove_parser.add_argument("name", help="Name of venv to remove.")

# move
move_parser = subparsers.add_parser("mv", help="Move(rename) venv to another place.")
move_parser.add_argument("source", help="Name of source venv.")
move_parser.add_argument("target", help="Name of target venv.")

# copy
copy_parser = subparsers.add_parser("cp", help="Copy venv.")
copy_parser.add_argument("source", help="Name of source venv.")
copy_parser.add_argument("target", help="Name of target venv.")


def parse():
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
