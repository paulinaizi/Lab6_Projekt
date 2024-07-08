import sys


def main():
    if len(sys.argv) != 3:
        print("Use: 'project.exe pathFile1 pathFile2'")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2]


if __name__ == '__main__':
    main()
