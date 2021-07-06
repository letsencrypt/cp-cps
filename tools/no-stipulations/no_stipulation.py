#!/usr/bin/env python3
import argparse


def make_no_stipulations(old_content: list) -> str:
    new_content = []
    for i in range(len(old_content)):
        curr_line = old_content[i]
        prev_line = old_content[i - 1]
        # Only parse empty lines that appear after a heading.
        if curr_line == "\n" and prev_line[0] == '#':
            if i < len(old_content)-1:
                next_line = old_content[i + 1]
                if next_line[0] == '#' and len(prev_line.split("#")) >= len(next_line.split("#")):
                    new_content.append("No stipulation.")
            else:
                new_content.append("No stipulation.")
        # Only keep lines that aren't newlines.
        elif curr_line != "\n":
            # Strip any trailing newlines from each line.
            new_content.append(curr_line.rstrip())
    
    return "\n\n".join(new_content)+"\n\n"


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
    # Replace the last newline stripped by the readlines method.
    contents.append('\n')
    print(make_no_stipulations(contents))


if __name__ == "__main__":
    main()
