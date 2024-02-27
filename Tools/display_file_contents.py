import argparse


def cat_file(file_path):
    """Function to print the content of the file"""
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except Exception as e:
        print(f"Error opening or reading file: {e}")


def main():
    parser = argparse.ArgumentParser(description="Mimic Unix 'cat' command behavior")
    parser.add_argument('file_path', type=str, help='Path to the file to be displayed')

    args = parser.parse_args()

    cat_file(args.file_path)


if __name__ == '__main__':
    main()
