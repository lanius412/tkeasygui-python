# TkEasyGUI

`TkEasyGUI` is a Python library that allows for the easy and simple creation of GUI applications.

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/logo-button.jpg" width="180" alt="TkEasyGUI Logo">

- Python's standard UI library `Tkinter`, is often considered to have a high barrier to entry and to be difficult to use. By using this library, you can create GUI applications easily and intuitively.
- In the event model, it is compatible with the well-known GUI library `PySimpleGUI`.
- This project adopts the lenient MIT license. This license will not change in the future. Let's enjoy creating GUI programs.

- [👉日本語](https://github.com/kujirahand/tkeasygui-python/blob/main/README-ja.md) / [👉中文](https://github.com/kujirahand/tkeasygui-python/blob/main/README-zh.md)


## Platform

- Windows / macOS / Linux (Tkinter required)

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/tkeasygui-shot640.jpg" width="300" alt="TkEasyGUI">

## Install

Install package from [PyPI](https://pypi.org/project/TkEasyGUI/).

```sh
python -m pip install TkEasyGUI
```

Install package from [GitHub Repository](https://github.com/kujirahand/tkeasygui-python).

```sh
python -m pip install git+https://github.com/kujirahand/tkeasygui-python
```

- (memo) Updating from older versions (less than 0.2.24) will fail. ([See the solution](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/installation_trouble.md))

## How to use - popup dialogs

Using TkEasyGUI is simple. If you only want to display a dialog, it requires just two lines of code.

```py
import TkEasyGUI as eg
# Displays the message in a popup dialog.
eg.print("A joyful heart is good medicine.")
```

Ask the user for their name and display that name in the window.

```py
import TkEasyGUI as eg
name = eg.input("What is your name?")
eg.print(f"Hello, {name}.")
```

### How to use - widgets

To create a simple window with only labels and buttons, you would write as follows:

```py
import TkEasyGUI as eg
# define layout
layout = [
    [eg.Text("Hello, World!")],
    [eg.Button("OK")]
]
# create a window
window = eg.Window("Hello App", layout)
# event loop
for event, values in window.event_iter():
    if event == "OK":
        eg.print("Thank you.")
        break
```

You can describe it using an event model similar to the famous GUI library, PySimpleGUI.

```py
import TkEasyGUI as eg

# define layout
layout = [[eg.Text("Hello, World!")], [eg.Button("OK")]]
# create a window
window = eg.Window("Hello App", layout)
# event loop
while True:
    event, values = window.read()
    if event in ["OK", eg.WINDOW_CLOSED]:
        eg.popup("Thank you.")
        break
# close window
window.close()
```

## Samples

We have prepared a selection of samples to demonstrate simple usage. Please check them out.

- [samples](https://github.com/kujirahand/tkeasygui-python/tree/main/tests).

Running `tests/file_viewer.py` allows all samples to be easily launched.

## Documents

Below is a detailed list of classes and methods.

- [docs](https://github.com/kujirahand/tkeasygui-python/tree/main/docs)

## About the relationship with PySimpleGUI

- When utilizing basic features, it is compatible with PySimpleGUI. You can write programs using the same event model as PySimpleGUI.
- The names of basic GUI components are also kept the same. However, while some property names differ, many unique features have been implemented.
- This project was developed with PySimpleGUI in mind, but has been implemented entirely from scratch. There are no licensing issues.
- We are not considering full compatibility with PySimpleGUI.

### TkEasyGUI features:

- Using a `for` loop and `window.event_iter()` enables straightforward event processing.
- Custom popup dialogs, such as a color selection dialog (`eg.popup_color`), are available.
- The `Image` class supports not only PNG but also JPEG formats.
- Convenient event hooks and features for bulk event registration are provided - [docs/custom_events](docs/custom_events.md).
- Methods such as Copy, Paste, and Cut are added to text boxes (Multiline/Input).
- The system's default color scheme is utilized.

## Link

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)
