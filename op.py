from shell_executor import sh
from config import config_path

def create_op(args):
    print(f'Creating item: {args.name}')


def remove_op(args):
    if args.force:
        print(f'Removing item {args.name} (forced)')
    else:
        print(f'Removing item {args.name}')


def relocate_op(args):
    if args.dest:
        print(f'Relocating item {args.name} to {args.dest}')


def list_op():
    print('list')


def activate_op(args):
    print(f'activate venv {args.name}')


def config_op(args):
    if args.config_command == 'set':
        pass
    elif args.config_command == 'get':
        pass
    else: # empty
        sh.edit_file(config_path())

def check_python_validation():
    return sh.check_python_version()


class Operation:
    def __init__(self, args) -> None:
        self.args = args

    def args_checker(func):
        def wrapper_func(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f'Error: {e}')
        return wrapper_func


    def create(self):
        print(f'Creating item: {self.args.name}')