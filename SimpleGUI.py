
### Tutorial from Webpage https://realpython.com/pysimplegui-python/

import PySimpleGUI as sgui
import os.path
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

fileListColumn = [
    [
        sgui.Text('Image Viewer'),
        sgui.In(size=(25,1),enable_events=True,key='-FOLDER-'),
        sgui.FolderBrowse()
    ],
    [
        sgui.Listbox(values=[],enable_events=True, size=(40,20), key='-FILE LIST-')
    ]
]

imageViewerColumn = [
    [sgui.Text('Choose an image from list on the left')],
    [sgui.Text(size=(40,1), key='-TOUT-')],
    [sgui.Image(key='-IMAGE-')]
]

plotColumn = [
    [sgui.Text('Plot Test',size=(40,1))],
    [sgui.Canvas( key='-CANVAS-')],
    [sgui.Button('OK', key='-OK2PLOT-')]
]
#create the full layout
layout = [
    [
        sgui.Column(fileListColumn),
        sgui.VSeparator(),
        sgui.Column(imageViewerColumn),
        sgui.VSeparator(),
        sgui.Column(plotColumn)
    ]
]

# Create the window
window = sgui.Window("Image&Plot Viewer", layout, font='Helvetica 18')


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side = 'top', fill = 'both', expand = 1)
    return figure_canvas_agg

fig = matplotlib.figure.Figure(figsize=(5,4), dpi = 100)
t = np.arange(0,3,0.01)
fig.add_subplot(111).plot(t, 2* np.sin(2 * np.pi * t))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button

    if event == "OK" or event == sgui.WIN_CLOSED:
        break
    #Folder name was filled in, make a list of files in the folder
    if event == '-FOLDER-':
        folder = values['-FOLDER-']
        try:
            #get list of files in the folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith(('.png','.gif'))
        ]
        window['-FILE LIST-'].update(fnames)
    elif event == '-FILE LIST-':
        try:
            file_name = os.path.join(values['-FOLDER-'],values['-FILE LIST-'][0])
            window['-TOUT-'].update(file_name)
            window['-IMAGE-'].update(filename = file_name)
        except:
            pass
    elif event == '-OK2PLOT-':
        draw_figure(window['-CANVAS-'].TKCanvas,fig)
window.close()

matplotlib.use('TkAgg')
