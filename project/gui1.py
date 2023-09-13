from project.text import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text("Type in a to do ")
input_box = sg.InputText(tooltip="enter a todo")
add_button = sg.Button("Add")

window = sg.Window('my todo app', layout=[[label], [input_box, add_button]])
window.read()
window.close()