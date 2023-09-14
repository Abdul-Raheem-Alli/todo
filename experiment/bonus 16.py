import PySimpleGUI as sg
label = sg.Text("File compressor")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("choose")

label2 = sg.Text("compress")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("choose")
compress_button = sg.Button("compress")
window = sg.Window("my compresser",
                    layout=[[label, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [compress_button]], font=('Helvetical', 20))
window.read()
window.close()