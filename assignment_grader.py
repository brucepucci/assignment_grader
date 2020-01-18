import importlib
import os
import shutil
import subprocess
import sys
import unittest
import zipfile

from test import example_assignment_tests

BASE_DIR = os.path.split(os.path.realpath(__file__))[0]
DATA_DIR = os.path.join(BASE_DIR, 'data')


def remove_existsing_directory(path):
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)

def unzip_assignment(name):
    zip_path = os.path.join(DATA_DIR, name)
    landing_path = os.path.join(DATA_DIR, name.split('.')[0])

    remove_existsing_directory(landing_path)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(landing_path)

def convert_notebooks(name):
    landing_path = os.path.join(DATA_DIR, name.split('.')[0])
    notebooks = os.listdir(landing_path)

    for notebook in notebooks:
        subprocess.call(['jupyter', 'nbconvert', '--to', 'python',
                         os.path.join(landing_path, notebook)])

def create_results_directory(name):
    results_path = os.path.join(DATA_DIR, name.split('.')[0] + '_results')
    remove_existsing_directory(results_path)
    if not os.path.exists(results_path):
        os.makedirs(results_path)

def grade_assignment(name):
    results_path = os.path.join(DATA_DIR, name.split('.')[0] + '_results')
    landing_path = os.path.join(DATA_DIR, name.split('.')[0])
    scripts = [f for f in os.listdir(landing_path) if f.endswith('.py')]

    for script in scripts:
        module_name = script.split('.')[0]
        submission = importlib.import_module(
            f'data.{name.split(".")[0]}.{module_name}', package=None)
        tests = importlib.import_module(
            f'test.{name.split(".")[0]}_tests', package=None)
        for obj in dir(submission):
            if not obj.startswith('__'):
                exec(f'tests.{obj} = submission.{obj}')
        suite = unittest.TestLoader().loadTestsFromModule(tests)
        with open(os.path.join(results_path, module_name + '.txt'), 'w') as f:
            unittest.TextTestRunner(f, verbosity=2).run(suite)


def main():
    zip_file_name = sys.argv[1] + '.zip'
    unzip_assignment(zip_file_name)
    convert_notebooks(zip_file_name)
    create_results_directory(zip_file_name)
    grade_assignment(zip_file_name)

main()



