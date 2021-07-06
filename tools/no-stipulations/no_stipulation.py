#!/usr/bin/env python3
import argparse


def make_no_stipulations(old_lines: list) -> str:
    new_lines = []
    for i in range(len(old_lines)):
        curr = old_lines[i]
        if curr == "\n":
            prev_line = old_lines[i - 1]
            next_line = old_lines[i + 1]
            if (prev_line[0], next_line[0]) == ('#', '#') and len(prev_line.split("#")) >= len(next_line.split("#")):
                new_lines.append("No stipulation.\n")
        else:
            new_lines.append(old_lines[i])

    return "\n".join(new_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Replaces empty policy sections with 'No stipulation.'"
    )
    parser.add_argument(
        "-d",
        "--document",
        metavar="PATH",
        type=argparse.FileType("r"),
        required=True,
        help="the path of the policy document to edit",
    )

    args = parser.parse_args()
    contents = args.document.readlines()
    print(make_no_stipulations(contents))


if __name__ == "__main__":
    main()
