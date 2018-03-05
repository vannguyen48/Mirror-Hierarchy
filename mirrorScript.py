import argparse
import os

def main():
    parse()

def parse():
    parser = argparse.ArgumentParser(description = 'Create a mirror directory hierarchy.')
    parser.add_argument('BASE', type = str,
                  help = 'the path to the directory where files or SQL scripts are located.')
    parser.add_argument('OUTPUT', type = str,
                  help = 'the path to the directory where output CSV files will be stored.')
    args = parser.parse_args()
    assert os.path.isdir(args.BASE), 'Base path is invalid'
    assert os.path.isdir(args.OUTPUT), 'Output path is incorrect'
    extract(args.BASE, args.OUTPUT)

def extract(basepath, outputpath):
    path_list = []
    print(path_list)
    for root, dirs, files in os.walk(basepath):
        level = root.replace(basepath, '').count(os.sep)
        if (level == 0):
            head = os.path.dirname(root)
            print (head)
        else:
            print(root)
            splitpath = root.split(head)
            path_list.append(splitpath[1])
    print(path_list)
    join(path_list, outputpath)

def join(pathlist, outputpath):
    output_path_list = []
    print (outputpath)
    for i in pathlist:
        output_paths = outputpath + i
        output_path_list.append(output_paths)
    create_hierarchy(output_path_list)

def create_hierarchy(output_path_list):
    for i in output_path_list:
        if not os.path.exists(i):
            print (i)
            os.makedirs(i)

if __name__ == '__main__':
    main()
