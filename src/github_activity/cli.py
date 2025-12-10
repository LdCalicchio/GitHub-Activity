from argparse import ArgumentParser
from . import functions

def main():
    
    parser = ArgumentParser()
    parser.add_argument(
        dest="username",
        help="Username of the GitHub to be searched",
        type=str
    )

    args = parser.parse_args()

    functions.getEvents(args.username)

if __name__ == "__main__":
    main()