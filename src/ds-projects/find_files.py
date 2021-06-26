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

    if suffix is None or path == "" or path is None:
        return []
        
    paths = []

    def _find_files_helper(suffix, path):

        for file in os.listdir(path):

            full_path = os.path.join(path, file)

            if not os.path.isdir(full_path) and file.endswith(suffix):
                paths.append(full_path)
            elif os.path.isdir(full_path):
                _find_files_helper(suffix, full_path)

        return sorted(paths)
    
    return _find_files_helper(suffix, path)

"""
/Users/eapmartins/temp/file1.py
/Users/eapmartins/temp/file2.py
/Users/eapmartins/temp/folder2/file3.py
/Users/eapmartins/temp/folder3/file1.java
"""

assert find_files(".py", "") == []
assert find_files(".py", None) == []
assert len(find_files(".py", "/Users/eapmartins/temp/")) == 3
assert find_files(".py", "/Users/eapmartins/temp/") == ["/Users/eapmartins/temp/file1.py", "/Users/eapmartins/temp/file2.py", "/Users/eapmartins/temp/folder2/file3.py"]