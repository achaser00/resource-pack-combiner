import PySimpleGUI as sg
import os
import shutil

file_list_column = [
    [
        sg.Text("Main Pack Folder"),
        sg.In(size=(25,1), enable_events=True, key="MAINFOLDER"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Secondary Pack Folder"),
        sg.In(size=(25,1), enable_events=True, key="SECONDFOLDER"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Output Folder"),
        sg.In(size=(25,1), enable_events=True, key="OUTPUTFOLDER"),
        sg.FolderBrowse(),
    ],
    [
        sg.Button("Combine Packs", key="COMBINE")
    ],
]

#full layout
layout = [
    [
        sg.Column(file_list_column),
    ]
]

window = sg.Window("Resource Pack Combiner", layout)


#event loop to actually run program
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "COMBINE":
        new_pack = values["OUTPUTFOLDER"]
        main_folder = values["MAINFOLDER"]
        second_folder = values["SECONDFOLDER"]
        #Gets the directories of all packs, and adds them to a list.
        pack_dir_list = [main_folder, second_folder]
        '''counter = 0
        while counter < 2:
            pack_dir_list.append(input("Directory of pack :"))
            counter += 1
        '''
        #In order of their index, adds each pack to the new_pack directory, orverriding files of the same name.
        for pack in pack_dir_list:
            shutil.copytree(str(pack), str(new_pack), dirs_exist_ok=True)
    '''
    #folder name was filled, so make list of files
    if event == "COMBINE":
        folder = values["-FOLDER-"]
        try:
            #get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-": #a file was chosen from list
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
    '''


window.close()