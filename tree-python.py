import pathlib

currentPath = pathlib.Path('.')

paths = [currentPath]

# TODO: Implement allowing symlinks to be followed (handle cycles).
followSymlink = False

directoryCount = 0
fileCount = 0

def print_tree(path, indents=''):
    global directoryCount
    global fileCount
    childCount = 0
    totalChildren = 0
    # Count number of children to determine last element in folder.
    for x in path.iterdir():
        totalChildren += 1
    for child in path.iterdir():
        childCount += 1
        # If child is last element, use "└", else use "├" since loop continues.
        if childCount < totalChildren:
            print(indents + '├── ' + str(child.name))
        else:
            print(indents + '└── ' + str(child.name))
        if child.is_dir() and not child.is_symlink():
            directoryCount += 1
            # If last element already processed, next child should not have the
            # "│" which denotes another element on the same level.
            if childCount < totalChildren:
                print_tree(child, indents + '│   ')
            else:
                print_tree(child, indents + '    ')
        elif child.is_file():
            fileCount += 1

print(currentPath)
print_tree(currentPath)
print('\n' + str(directoryCount) + ' directories, ' + str(fileCount) + ' files')