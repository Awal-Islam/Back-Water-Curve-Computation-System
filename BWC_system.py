from bokeh.io import output_file, show
from bokeh.layouts import column, row, gridplot
from bokeh.models import Button, CustomJS, TextInput
from bokeh.plotting import figure

output_file("BWC.html")
button_title = Button(label="BACK WATER CURVE NUMERICAL SOLUTION", button_type="success")
button_input = Button(label="INPUT", button_type="success")
text_input_length = TextInput(value = '', title = "Length of Channel, L (m)")
text_input_width = TextInput(value = '', title = "Bed Width of Channel, B (m)")
text_input_discharge = TextInput(value = '', title = "Discharge, Q (m3/s)")
text_input_chezy = TextInput(value = '', title = "Chezy's Coefficient, C (m^(1/2)/s)")
text_input_slope = TextInput(value = '', title = "Channel Bed Slope, So")
text_input_idepth = TextInput(value = '', title = "Initial Depth, ho (m)")
text_input_delx = TextInput(value = '', title = "Delta X, (m)")
button_run = Button(label="RUN", button_type="success")
button_odata = Button(label="STORE OUTPUT DATA", button_type="success")
figure = figure(title = 'Backwater Curve', x_axis_label = 'Distance (m)', y_axis_label = 'Water Level (m)')
gui = row(column(button_title, button_input, text_input_length, text_input_width, text_input_discharge, text_input_chezy, text_input_slope, text_input_idepth, text_input_delx), column(button_run, figure, button_odata))
show(gui)
