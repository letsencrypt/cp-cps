#!/usr/bin/env python3
import argparse


def make_no_stipulations(old_content: list) -> str:
    new_content = []
    for i in range(len(old_content)):
        curr_line = old_content[i]
        # Unconditionally append the first line to avoid index wrap-around.
        if i == 0:
            new_content.append(curr_line)
            continue
        prev_line = old_content[i - 1]
        if curr_line == "\n":
            if prev_line[0] == "#":
                if i < len(old_content) - 1:
                    next_line = old_content[i + 1]
                    if next_line[0] == "#" and len(prev_line.split("#")) >= len(next_line.split("#")):
                        new_content.append(curr_line + "No stipulation.\n\n")
                    else:
                        new_content.append(curr_line)
                else:
                    new_content.append(curr_line + "No stipulation.\n\n")
            else:
                new_content.append(curr_line)
        else:
            new_content.append(curr_line)

    return "".join(new_content)


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
        help="path to the policy document to edit you wish to edit",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        type=argparse.FileType("w"),
        required=True,
        help="path to output the edited policy document",
    )

    args = parser.parse_args()
    contents = args.document.readlines()
    args.document.close()

    new_content = make_no_stipulations(contents)
    args.output.write(new_content)
    args.output.close()


if __name__ == "__main__":
    main()
