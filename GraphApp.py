import PySimpleGUI as sg
import matplotlib
import matplotlib.figure as mf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_figure(data):
    fig.axes[0].plot([i[0] for i in data], [i[1] for i in data], "g-")
    fig_canvas.draw()
    fig_canvas.get_tk_widget().pack()


sg.theme("DarkTeal6")
table_content = []
layout = [
    [sg.Table(headings=["Observation", "Result"], values=table_content, expand_x=True, hide_vertical_scroll=True, key="-TABLE-")],
    [sg.Input(key="-INPUT-", expand_x=True), sg.Button("Submit")],
    [sg.Canvas(key="-CANVAS-")]
]

window = sg.Window("Graph application", layout, finalize=True)

# matplotlib
fig = mf.Figure(figsize=(5, 4))
fig.add_subplot(111).plot([], [])
fig_canvas = FigureCanvasTkAgg(fig, window["-CANVAS-"].TKCanvas)
fig_canvas.draw()
fig_canvas.get_tk_widget().pack()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED: break

    if event == "Submit":
        new_value = values["-INPUT-"]
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1, float(new_value)])
            window["-TABLE-"].update(table_content)
            window["-INPUT-"].update("")
            update_figure(table_content)
        else:
            sg.popup_error("Input a numeric value!")


window.close()