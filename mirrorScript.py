import argparse
import os

def main():
    """
    Main function.

    """
    parse()

def parse():
    """
    Function to process input and parse command-line arguments.

    Args:
        BASE (str): the base directory containing the file hierarchy.
        OUTPUT (str): the output directory containing the location of the output file hierarchy.

    Returns:
        returns 0 if no error found.

    """
    parser = argparse.ArgumentParser(description = 'Create a mirror directory hierarchy.')
    parser.add_argument('BASE', type = str,
                  help = 'the path to the directory where files or SQL scripts are located.')
    parser.add_argument('OUTPUT', type = str,
                  help = 'the path to the directory where output CSV files will be stored.')
    args = parser.parse_args()
    assert os.path.isdir(args.BASE), 'Base path is invalid'
    assert os.path.isdir(args.OUTPUT), 'Output path is incorrect'
    extract(args.BASE, args.OUTPUT)
    return 0

def extract(basepath, outputpath):
    """
    Function to extract the base path and record the file hierarchy.

    Args:
        basepath: the base directory containing the file hierarchy.
        outputpath: output hierarchy containing the location of the output hierarchy.

    """
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
    """
    Composes output hierarchy.

    Args:
        pathlist: list containing directories that needs to be created in output directory.
        outputpath: directory containing the location of ouput directory hierarchy.

    """
    output_path_list = []
    print (outputpath)
    for i in pathlist:
        output_paths = outputpath + i
        output_path_list.append(output_paths)
    create_hierarchy(output_path_list)

def create_hierarchy(output_path_list):
    """
    Creates directory hierarchy in output location.

    Args:
        output_path_list: list containing all mirrored file hierarchy.

    """
    for i in output_path_list:
        if not os.path.exists(i):
            print (i)
            os.makedirs(i)

if __name__ == '__main__':
    """
    Performs a main check so that this script can run on its own (rather than being imported from another module).

    """
    main()
