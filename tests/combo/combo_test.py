"""
### Combo test
"""

import TkEasyGUI as eg

# set values
values = [f"value_{i}" for i in range(50)]
# create window
window = eg.Window(
    "Combo test",
    layout=[
        [eg.Text("Please select value or input:")],
        [
            eg.Combo(
                values,
                enable_events=True,
                key="-combo1-",
                expand_x=True,
            )
        ],
        [eg.Text("Please select value(readonly):")],
        [
            eg.Combo(
                values,
                default_value="value_0",
                enable_events=True,
                readonly=True,
                key="-combo2-",
                expand_x=True,
            )
        ],
        [eg.Button("OK")],
    ],
)
# event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == eg.WIN_CLOSED:
        break
    if event == "OK":
        eg.print(f"You selected: -combo1-={values["-combo1-"]}, -combo2-={values["-combo2-"]}")

window.close()
