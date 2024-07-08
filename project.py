import sys
import xmltodict
import json
import os


def validate_xml(file_content):
    try:
        data = xmltodict.parse(file_content)
        return data
    except Exception:
        print(f"Invalid XML file")
        raise


def validate_json(file_content):
    try:
        data = json.loads(file_content)
        return data
    except ValueError:
        print("Invalid JSON file")
        raise


def main():
    if len(sys.argv) != 3:
        print("Use: 'project.exe pathFile1 pathFile2'")
        return
    try:
        input_path = sys.argv[1]
        output_path = sys.argv[2]

        input_format = os.path.splitext(input_path)[-1].lower()
        output_format = os.path.splitext(output_path)[-1].lower()

        with open(input_path, 'r', encoding='utf-8') as input_file:
            input_content = input_file.read()

            if input_format == '.xml':
                data = validate_xml(input_content)
            elif input_format == '.json':
                data = validate_json(input_content)
            else:
                raise ValueError(f'Unsupported file extension {input_format} (Input file)')
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
