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
                user = input('login to get permission: ')
                password = input('password: ')
                if system == 'posix':
                    trace = os.system('echo ' + password + '| sudo -S ls /tmp')
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
        return True

def npm_handle():
    npm_code = 999
    npm_code = os.system('npm install')
    if npm_code == 0:
        print('npm packages is installed')
    else:
        print('npm error code:' + str(npm_code))
def git_handle():
    git_state = ''
    git_code = 999
    git_repo = input('git repository: ')
    git_code = os.system('git clone ' + git_repo)
    if git_code == 0:
        print('git repository is cloned')


def project_starter():
    system = os.name
    if system == 'posix':
        change_directory(system)
        git_exists = os.system('which git')
        if git_exists == 0:
            git_handle()
    else:
        change_directory(system)
        git_exists = os.system('git --version')
        if git_exists == 0:
            git_handle()

if __name__ == '__main__':
    project_starter()
