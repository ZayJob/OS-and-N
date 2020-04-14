import os


def search_files(search_dir, search_assignment):
    result = []
    for root, dirs, files in os.walk(search_dir):
        for file_name in files:
            if file_name.endswith(search_assignment):
                result.append(file_name)
    return result

def dump_to_file(result, file_to_write):
    if not os.path.isfile(file_to_write):
        file_to_write = 'result.txt'

    with open(file_to_write, 'a') as wf:
        wf.write('\n'.join(result))


def main():
    search_dir = input('Enter the dir: ')
    search_assignment = input('Enter the extension: ')
    file_to_write = input('Enter file: ')

    result = search_files(search_dir, search_assignment)
    dump_to_file(result, file_to_write)


if __name__ == '__main__':
    main()