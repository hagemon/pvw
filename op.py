def create_op(args):
    print(f'Creating item: {args.env_name}')


def remove_op(args):
    if args.force:
        print(f'Removing item {args.env_name} (forced)')
    else:
        print(f'Removing item {args.env_name}')


def relocate_op(args):
    if args.dest:
        print(f'Relocating item {args.env_name} to {args.dest}')