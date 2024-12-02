FILEPATH = 'files/todos.txt'


def get_todos(filepath_local=FILEPATH):
    """ Read the text file and
    return the list of items.
    :param filepath_local:
    :return: todos
    """
    with open(filepath_local, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath_local=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath_local, 'w') as file:
        file.writelines(todos_arg)




if __name__ == '__main__':
    print('Hello')
    print(get_todos())
