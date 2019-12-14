import argparse
from init import init as it


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    init = subparsers.add_parser('init')
    init.set_defaults(func=it)

    add = subparsers.add_parser('add')
    add.set_defaults(func=lambda: print("add"))

    commit = subparsers.add_parser('commit')
    commit.set_defaults(func=lambda: print("commit"))

    log = subparsers.add_parser('log')
    log.set_defaults(func=lambda: print("log"))

    config = subparsers.add_parser('config')
    config.set_defaults(func=lambda: print("config"))

    args = parser.parse_args()
    args.func()


if __name__ == "__main__":
    main()
