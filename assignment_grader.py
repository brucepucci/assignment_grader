import importlib
import itertools
import os
import shutil
import subprocess
import sys
import unittest
import zipfile

import pandas as pd

BASE_DIR = os.path.split(os.path.realpath(__file__))[0]
DATA_DIR = os.path.join(BASE_DIR, 'data')


def remove_existsing_directory(path):
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)

def unzip_assignment(zip_path, name):
    landing_path = os.path.join(DATA_DIR, name.split('.')[0])

    remove_existsing_directory(landing_path)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(landing_path)

def convert_notebooks(name):
    landing_path = os.path.join(DATA_DIR, name.split('.')[0])
    notebooks = os.listdir(landing_path)
    FNULL = open(os.devnull, 'w')
    for notebook in notebooks:
        subprocess.call(['jupyter', 'nbconvert', '--to', 'python',
                         os.path.join(landing_path, notebook)],
                        stdout=FNULL, stderr=subprocess.STDOUT)

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
            f'test.{name.split(".")[0]}', package=None)
        for obj in dir(submission):
            if not obj.startswith('__'):
                exec(f'tests.{obj} = submission.{obj}')
        suite = unittest.TestLoader().loadTestsFromModule(tests)
        with open(os.path.join(results_path, module_name + '.test.txt'), 'w') as f:
            unittest.TextTestRunner(f, verbosity=2).run(suite)

def _get_delimiter(test_output):
    return next(i for i, line in enumerate(test_output) if line.startswith('==='))

def _parse_tests(tests, student):
    result = list()
    for test in tests:
        tmp = test.split(' ')
        test_names = tmp[0]
        test_class = tmp[1][1:-1].split('.')[-1]
        test_result = tmp[-1]
        result.append({
            'student_name': student,
            'test_name': test_names,
            'test_class': test_class,
            'test_result': test_result,
            'test_correct': test_result == 'ok',
        })
    return result


def assignment_summary(name):
    results_path = os.path.join(DATA_DIR, name.split('.')[0] + '_results')
    results = os.listdir(results_path)

    records = list()
    for result in results:
        student = result.split('_', 1)[0]
        with open(os.path.join(results_path, result), 'rt') as f:
            text = f.read().split('\n')
        delimiter = _get_delimiter(text)
        tests = text[:delimiter]
        tests = list(filter(None, tests))
        summary = _parse_tests(tests, student)
        for record in summary:
            records.append(record)
    return pd.DataFrame(records)

def write_summary(df, name):
    results_path = os.path.join(DATA_DIR, name.split('.')[0] + '_results')
    df.to_csv(os.path.join(results_path, 'detail.csv'), index=False)

    grades = pd.DataFrame(
        df.groupby('student_name').test_correct.mean().astype(float))
    grades.to_csv(os.path.join(results_path, 'grades.csv'))

    grades = pd.DataFrame(
        df.groupby('test_class').test_correct.mean().astype(float))
    grades.to_csv(os.path.join(results_path, 'problem.csv'))

    grades = pd.DataFrame(
        df.groupby(['test_class', 'test_name']).test_correct.mean().astype(float))
    grades.to_csv(os.path.join(results_path, 'test.csv'))

def clean_dirs(name):
    results_path = os.path.join(DATA_DIR, name.split('.')[0] + '_results')
    landing_path = os.path.join(DATA_DIR, name.split('.')[0])
    graded_files = [f for f in os.listdir(results_path) if f.endswith('.test.txt')]
    ipynb_files = [f for f in os.listdir(landing_path) if f.endswith('.ipynb')]
    py_files = [f for f in os.listdir(landing_path) if f.endswith('.py')]

    for gf in graded_files:
        student_name = gf.split('_', 1)[0]
        student_dir = os.path.join(results_path, student_name)
        os.mkdir(student_dir)
        shutil.move(os.path.join(results_path, gf),
                    os.path.join(student_dir, f'{student_name}_graded.txt'))
        for pf in py_files:
            if pf.startswith(student_name):
                shutil.move(os.path.join(landing_path, pf),
                            os.path.join(student_dir, f'{student_name}.py'))
        for ipf in ipynb_files:
            if ipf.startswith(student_name):
                shutil.move(os.path.join(landing_path, ipf),
                            os.path.join(student_dir, f'{student_name}.ipynb'))
    shutil.rmtree(landing_path)

if __name__ == '__main__':
    zip_file_loc = sys.argv[1]
    test_file_loc = sys.argv[2]

    zip_file_name = os.path.basename(zip_file_loc).split('.')[0]
    test_file_name = os.path.basename(test_file_loc).split('.')[0]

    print('Unzipping')
    unzip_assignment(zip_file_loc, test_file_name)
    print('Converting Notebooks')
    convert_notebooks(test_file_name)
    create_results_directory(test_file_name)
    print('Grading')
    grade_assignment(test_file_name)
    df = assignment_summary(test_file_name)
    print('Summarizing')
    write_summary(df, test_file_name)
    print('Cleaning Up')
    clean_dirs(test_file_name)

