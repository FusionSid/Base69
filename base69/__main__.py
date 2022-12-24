import argparse

from base69 import encode_base69_int, decode_base69_int


def main() -> None:
    parser = argparse.ArgumentParser()

    # Integer Encoding & Decoding
    parser.add_argument("-ei", "--encodeint", type=int)
    parser.add_argument("-di", "--decodeint", type=str)

    # Text Encoding & Decoding
    # parser.add_argument("-et", "--encodetext", type=str)
    # parser.add_argument("-dt", "--decodetext", type=str)

    # Float Encoding & Decoding
    # parser.add_argument("-ef", "--encodefloat", type=float)
    # parser.add_argument("-df", "--decodefloat", type=str)

    # Other Options
    parser.add_argument("--pypi", action="store_true")
    parser.add_argument("--github", action="store_true")

    # Parse Args
    args = parser.parse_args()

    if args.encodeint is not None:
        print(encode_base69_int(args.encodeint))
    elif args.decodeint is not None:
        print(decode_base69_int(args.decodeint))
    elif args.pypi:
        print("https://pypi.org/project/Base-69/")
    elif args.github:
        print("https://github.com/micfun123/Base69")


if __name__ == "__main__":
    main()
