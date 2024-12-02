# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%Y. %b %d - %H:%M:%S")
print('Current time: ', now)

user_prompt = "Type add, show, edit, complete or exit:"

# print(help(get_todos))

while True:
    # Get user input and strip space chars from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f'{index + 1}-{item}')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo {todo_to_remove} was removed from the list")
        except IndexError:
            print('There is no item with that number!')
    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid!')

print("Bye!")
