import os
import sys
import shutil

target_path = 'build/python-dash'
target_code = target_path + '/code'
target_assets = target_code + '/assets'
data = ['config.ini']
start_file = 'start_app.bat'

copy_interpreter = True
create_zip = False


def main():

    print('Creates build folder ...')
    if not os.path.exists('build'):
        os.mkdir('build')

    # Python interpreter
    if copy_interpreter:

        print('Copy python interpreter ...')
        if os.path.exists(target_path):
            shutil.rmtree(target_path)

        path_env = sys.executable
        path_env = path_env.replace('python.exe', '')
        shutil.copytree(path_env, target_path)

    # Copy code
    if os.path.exists(target_code):
        shutil.rmtree(target_code)
    os.mkdir(target_code)

    files = os.listdir('.')
    for f in files:
        if '.py' not in f or '.pytest' in f:
            continue  # skip
        shutil.copyfile(f, f'{target_code}/{f}')

    # Needed files
    for d in data:
        shutil.copyfile(d, f'{target_code}/{d}')

    # assets folder
    if os.path.exists(target_assets):
        shutil.rmtree(target_assets)
    shutil.copytree('assets', target_assets)

    # Start up file
    if not os.path.isfile(f'build/{start_file}'):
        shutil.copyfile(start_file, f'build/{start_file}')

    if create_zip:
        print('Create zip folder ...')
        if os.path.isfile('python-dash.zip'):
            os.remove('python-dash.zip')
        shutil.make_archive('python-dash', 'zip', 'build')

    print('Finished!')


if __name__ == '__main__':
    main()
