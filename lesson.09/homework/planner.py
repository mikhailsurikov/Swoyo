import argparse
import datetime
import re
import sys
import math

DATE_PATTERN = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")
DATE_FORMAT = "%d.%m.%Y"


def parse_date(value):
    """Проверяет формат дд.мм.гггг регуляркой и возвращает datetime."""
    if not DATE_PATTERN.match(value):
        raise argparse.ArgumentTypeError(
            f"Дата '{value}' не соответствует формату дд.мм.гггг")
    try:
        return datetime.strptime(value, DATE_FORMAT)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Некорректная дата '{value}': {e}")


def positive_int(value):
    try:
        n = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' не является целым числом")
    if n <= 0:
        raise argparse.ArgumentTypeError(f"Значение должно быть > 0, получено {n}")
    return n


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Планировщик работы.")
    parser.add_argument("start", type=parse_date, help="Дата начала (дд.мм.гггг)")
    parser.add_argument("deadline", type=parse_date, help="Дедлайн (дд.мм.гггг)")
    parser.add_argument("--tasks", type=positive_int, default=30,
                        help="Количество задач (по умолчанию 30)")
    parser.add_argument("--per-day", type=positive_int, default=5,
                        help="Задач в день (по умолчанию 5)")
    args = parser.parse_args()

    available_days = (args.deadline - args.start).days
    if available_days < 0:
        print("Ошибка: дедлайн раньше даты начала.")
        return 1
    days_needed = math.ceil(args.tasks / args.per_day)
    print(f"Начало работы: {args.start.strftime(DATE_FORMAT)}")
    print(f"Дедлайн:            {args.deadline.strftime(DATE_FORMAT)}")
    print(f"Всего задач:        {args.tasks}")
    print(f"Задач в день:       {args.per_day}")
    print(f"Необходимо дней:   {days_needed}")
    print(f"Запас: {available_days} дней")
    print()

    if days_needed <= available_days:
        print("Не успеете выполнить задачи")
        return 0
    else:
        short = days_needed - available_days
        print(f"Не хватает дней: {short}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
