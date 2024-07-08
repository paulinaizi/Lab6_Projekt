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


def convert_file(input_path, output_path):
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

    with open(output_path, 'w', encoding='utf-8') as output_file:
        if output_format == '.xml':
            xml_data = xmltodict.unparse(data, pretty=True)
            output_file.write(xml_data)
        elif output_format == '.json':
            json.dump(data, output_file, indent=4)
        else:
            raise ValueError(f'Unsupported file extension: {output_format} (Output file)')


def main():
    if len(sys.argv) != 3:
        print("Use: 'project.exe pathFile1 pathFile2'")
        return

    try:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        convert_file(input_path, output_path)
        print(f'Successfully converted {input_path} to {output_path}')
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f'Conversion failed: {e}')


if __name__ == '__main__':
    main()
