import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    files = os.listdir(path)
    paths = []

    for file in files:

        full_path = path + file

        if file.endswith(suffix):
            paths.append(full_path)

        if os.path.isdir(full_path):
            file = find_files(suffix, full_path + "/")
            paths.append(file)

    return paths


print(find_files(".py", "/Users/eapmartins/temp/"))

