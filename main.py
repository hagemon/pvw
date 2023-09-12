import sys
from shell_executor import sh

def main(args):
    if args:
        cmd = args[0]
        if cmd == 'hello':
            sh.hello()
        elif cmd == 'create':
            print('create')
        elif cmd == 'list':
            print('list')
        elif cmd == 'help':
            print('help')
        else:
            print('unknow parameter', cmd)
    else:
        print('help')

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
