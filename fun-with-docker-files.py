#!/usr/bin/env python3

import sys

def main():
    exit_code = 0
    for file_path in sys.argv[1:]:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines, start=1):
                if "FROM:" in line and ":latest" in line:
                    print(f'"{file_path}" contains ":latest" on line {line_num}', file=sys.stderr)
                    exit_code = 1
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
