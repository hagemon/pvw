import argparse
from op import create_op, remove_op, relocate_op

parser = argparse.ArgumentParser(description='Manage python venv environments')
subparsers = parser.add_subparsers(help='Options to manage venvs', dest='command')

list_parser = subparsers.add_parser('list', help='List all environment.')

config_parser = subparsers.add_parser('config_parser', help='Config in vim.')


create_parser = subparsers.add_parser('create', help='Create a new venv.')
create_parser.add_argument('env_name', help='Name of venv to create')

remove_parser = subparsers.add_parser('remove', help='remove environment')
remove_parser.add_argument('-f', '--force', action='store_true', help='force remove item')
remove_parser.add_argument('env_name', help='Name of venv to remove')

relocate_parser = subparsers.add_parser('relocate', help='Relocate help')
relocate_parser.add_argument('env_name', help='Name of venv to relocate')
relocate_parser.add_argument('--dest', help='target path of item to relocate (REQUIRED)', action='store', required=True)

try:
    args = parser.parse_args()
    if args.command == 'create':
        create_op(args)
    elif args.command == 'remove':
        remove_op(args)
    elif args.command == 'relocate':
        relocate_op(args)
    else:
        parser.print_help()
except argparse.ArgumentError as e:
    print(f'Error: {e}')
    parser.print_help()
