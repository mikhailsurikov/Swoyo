import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("distance", help="Расстояние в километрах")
    parser.add_argument("--speed", default=60, help="Скорость")
    args = parser.parse_args()

    print(f'Время в пути: {args.distance / args.speed} ч')


if __name__ == "__main__":
    sys.exit(main())
