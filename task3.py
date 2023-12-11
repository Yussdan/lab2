import webbrowser
import os
import time

for file in os.listdir('lab2/html'):
    webbrowser.open(f'file://{os.path.realpath(f"lab2/html/{file}")}')
    time.sleep(2)
