# remote-barcode-scanner
Software that emulates a barcode scanner activated over ethernet, using python

## Build .exe
To convert the script to a .exe, use the following command:

powershell```
pyinstaller --onefile --noconsole tu_script.py
```

Note: This requires the pyinstaller package:
powershell```
pip install pyinstaller
```

