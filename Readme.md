# Readme

Quickly hacked together code formatter for apex.
Feel free to adapt it to your needs.

This project is a work in progress solution and can change any time.

## Installation

1. move the `apex-formatter.py` file to some location you like. I have mine on `~/.apex-formatter.py`.

1. You may need to perform a `chmod +x apex-formatter.py` in order for it to be executable.

1. install https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters
and set the apex-formatter.py as formatter for apex in the settings.json:
(find the settings.json by Cmd+Shift+P -> settings -> Extensions -> Custom Local Formatter -> Emmet -> "Extension path" )

    ```json
    "customLocalFormatters.formatters": [
        {
        "command": "python c://Users/PathToFormatter/apex-formatter.py",
        "languages": ["apex"]
        }
    ],
    ```
