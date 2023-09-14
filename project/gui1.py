import text
import PySimpleGUI as sg

label = sg.Text("Type in a to do ")
input_box = sg.InputText(tooltip="enter a todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('my todo app',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetical', 10))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = text.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            text.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()