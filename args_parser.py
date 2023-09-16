import argparse
from op import create_op, remove_op, relocate_op, config_op, check_python_validation

parser = argparse.ArgumentParser(description="Manage python venv environments")
subparsers = parser.add_subparsers(help="Options to manage venvs", dest="command")

# list
list_parser = subparsers.add_parser("list", help="List all environment.")

# config
config_parser = subparsers.add_parser("config", help="Config in vim.")
config_subparsers = config_parser.add_subparsers(
    help="Options in configuration", dest="config_command"
)
config_set_parser = config_subparsers.add_parser("set")
config_set_parser.add_argument("key")
config_set_parser.add_argument("value")
config_get_parser = config_subparsers.add_parser("get")
config_get_parser.add_argument("key")


# activate
activate_parser = subparsers.add_parser("activate", help="Activate venv")
activate_parser.add_argument("name", help="venv name")

# create
create_parser = subparsers.add_parser("create", help="Create a new venv.")
create_parser.add_argument("name", help="Name of venv to create")

# remove
remove_parser = subparsers.add_parser("remove", help="remove environment")
remove_parser.add_argument(
    "-f", "--force", action="store_true", help="force remove item"
)
remove_parser.add_argument("name", help="Name of venv to remove")

# relocate
relocate_parser = subparsers.add_parser("relocate", help="Relocate help")
relocate_parser.add_argument("name", help="Name of venv to relocate")
relocate_parser.add_argument(
    "--dest",
    help="target path of item to relocate (REQUIRED)",
    action="store",
    required=True,
)

try:
    args = parser.parse_args()
    if not check_python_validation():
        print("Python not installed")
    if args.command == "create":
        create_op(args)
    elif args.command == "remove":
        remove_op(args)
    elif args.command == "relocate":
        relocate_op(args)
    elif args.command == "config":
        config_op(args)
    else:
        parser.print_help()
except argparse.ArgumentError as e:
    print(f"Error: {e}")
    parser.print_help()
