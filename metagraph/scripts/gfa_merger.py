#!/usr/bin/env python3
import sys
import os


def exec_file_merging(gfa_main_filepath: str, gfa_path_filepaths: []):
    gfa_file = open(gfa_main_filepath, "a")
    next_P_index = 0
    for path_file in gfa_path_filepaths:
        file_reader = open(path_file, 'r')
        lines = file_reader.readlines()
        for line in lines:
            gfa_file.write("{}\t{}".format(next_P_index, line.split("\t",1)[1]))
            next_P_index += 1

def main():
    if len(sys.argv) < 2 or not sys.argv[1].endswith(".gfa"):
        print(f"Usage: {sys.argv[0]} <assembled.gfa> [<alignment.path.gfa> ..]", file=sys.stderr)
        exit(1)

    for file in sys.argv[2:]:
        if not file.endswith(".path.gfa"):
            print("Error: Appended files must have a '.path.gfa' extension "
                  "(outputs generated by 'metagraph align')", file=sys.stderr)
            exit(1)

    gfa_files_to_merge = sys.argv[2:]

    if len(gfa_files_to_merge) == 0:
        dir = os.path.dirname(os.path.abspath(sys.argv[1]))
        print(f"-- Searching for *.path.gfa files in {dir}")
        for file in os.listdir(dir):
            if file.endswith(".path.gfa"):
                print("-- Found: " + file)
                gfa_files_to_merge.append(os.path.join(dir, file))

    if len(gfa_files_to_merge) > 0:
        exec_file_merging(sys.argv[1], gfa_files_to_merge)
        print(f"-- {len(gfa_files_to_merge)} files were appended to {sys.argv[1]}")
    else:
        print(f"-- Nothing to append")


if __name__ == '__main__':
    main()