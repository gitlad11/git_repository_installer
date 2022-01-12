import sys
import os


def change_directory(system):
    directory_path = input('change directory: ')
    state = 'error with changing directory is occurred: '
    if directory_path:
        try:
            print('changing directory to... ' + directory_path)
            os.chdir(directory_path)
        except Exception as e:
            exception_code = e.args[0]
            if exception_code == 13:

                if system == 'posix':
                    trace = os.system('sudo su')
                    if trace == 0:
                        state = 'success login: (current directory is' + os.getcwd() + ')'
                        os.chdir(directory_path)
                    else:
                        state = 'error with changing directory is occurred: ' + e.args[1]
                else:
                    state = 'error with changing directory is occurred: ' + e.args[1]

            else:
                return False
            print(state)
        return directory_path


def npm_handle(folder_name, directory):
    if directory.endswith('/'):
        os.chdir('/' + directory + folder_name)
    else:
        os.chdir('/' + directory + '/' + folder_name)
    npm_code = 999
    npm_code = os.system('npm install')
    if npm_code == 0:
        print('npm packages is installed')
    else:
        print('npm error code:' + str(npm_code))



def git_handle(directory):
    git_state = ''
    git_code = 999
    git_repo = input('git repository: ')
    git_folder_name = input('folder name: ')
    if len(git_folder_name) > 0:
        git_code = os.system('git clone ' + git_repo + ' ' + git_folder_name)
    else:
        git_code = os.system('git clone ' + git_repo + ' ' + 'git_project')
    if git_code == 0:
        print('git repository is cloned')
        if len(git_folder_name):
            npm_handle(git_folder_name, directory)
        else:
            npm_handle('git_project', directory)


def project_starter():
    system = os.name
    if system == 'posix':
        directory = change_directory(system)
        git_exists = os.system('which git')
        if git_exists == 0:
            git_handle(directory)

    else:
        directory = change_directory(system)
        git_exists = os.system('git --version')
        if git_exists == 0:
            git_handle(directory)


if __name__ == '__main__':
    project_starter()
