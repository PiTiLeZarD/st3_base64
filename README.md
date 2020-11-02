# st3_base64

SublimeText3 plugin to encode and decode base64

In order to use this plugin, copy that base64plugin.py in your Package/User folder (on osx it's /Users/{YourUser}/Library/Application Support/Sublime Text 3/Packages/User) and then either update your Default.sublime-commands or create it with this:

    [
        {
            "caption": "Base64 - Encode",
            "command": "b64enc"
        },
        {
            "caption": "Base64 - Decode",
            "command": "b64dec"
        }
    ]
