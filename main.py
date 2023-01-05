# This is a sample Python script.
import argparse
import os.path as path
import re


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_version_xml(file_path):
    import xml.etree.ElementTree as ET
    xmltree = ET.parse(file_path)
    xmlroot = xmltree.getroot()

    for element in xmlroot:
        tag_name = element.tag
        tag_name = re.sub(r'\{.*\}', '', tag_name)
        if tag_name == '':
            continue
        if not 'version' == tag_name:
            continue
        print(element.text)


def get_version_json(file_path):
    import json
    with open(file_path) as file:
        data = json.load(file)

        if data is None:
            print('Json is empty')
            exit(2)
        print(data['version'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project", help="display a square of a given number", choices=['angular', 'maven'])
    parser.add_argument("-f", "--file", help="pom.xml or package.json destination")
    args = parser.parse_args()
    ## print(parser.parse_args())

    file_path = '.'

    if args.file is not None:
        file_path = args.file

    if 'angular' == args.project:
        file_path = f'{file_path}/package.json'

    if 'maven' == args.project:
        file_path = f'{file_path}/pom.xml'

    if not path.exists(file_path):
        print(f'{file_path} not exist')
        exit(1)

    file_name = path.basename(file_path)
    if file_name == 'pom.xml':
        get_version_xml(file_path)
        exit(0)

    if file_name == 'package.json':
        get_version_json(file_path)
        exit(0)
    print(file_name)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
