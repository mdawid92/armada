import argparse
import os
import subprocess


def get_hook_path(hook_name):
    microservice_name = os.environ['MICROSERVICE_NAME']
    hooks_dir = os.path.join('/opt', microservice_name, 'hooks')
    if os.path.isdir(hooks_dir):
        path = os.path.join(hooks_dir, hook_name)
        if os.path.isfile(path):
            return path

    return None


def run_hook(hook_name):
    hook_path = get_hook_path(hook_name)
    if hook_path:
        return subprocess.check_output(hook_path)
    else:
        print('no hook found')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('hook', nargs=1)
    args = parser.parse_args()
    output = run_hook(args.hook[0])
    print(output)
