from pkg_resources import resource_filename
import os


def main():
    hello_path = os.path.abspath(resource_filename('resources', 'hello.txt'))
    print('reading from resource: %s' % hello_path)
    with open(hello_path, 'r') as file:
        print(file.read())

if __name__ == '__main__':
    main()
