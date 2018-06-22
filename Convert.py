

import subprocess
import os


def files():
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Source'))
    files_list = os.listdir(path='.')
    return files_list


def create_res_dir():
    res_dir = os.path.join(os.path.dirname(__file__), 'Result')
    if not os.path.exists(res_dir):
        os.makedirs('Result')


def convert_img(file_list):
    source = os.path.join(os.path.dirname(__file__), 'Source')
    result = os.path.join(os.path.dirname(__file__), 'Result')
    for i in file_list:
        input_path = os.path.join(source, i)
        output_path = os.path.join(result, i)
        os.chdir(os.path.dirname(__file__))
        subprocess.Popen('convert ' + input_path + ' -resize 200 ' + output_path)


if __name__ == '__main__':
    create_res_dir()
    convert_img(files())
