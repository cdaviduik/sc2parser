# sc2parser

Starcraft 2 replay parser written in python using sc2reader and mpyq which creates a copy of the replay file containing player names and their mmr.

### Prerequisites

Download [Python 2.7](https://www.python.org/download/releases/2.7/) (probably [this one](https://www.python.org/ftp/python/2.7/python-2.7.amd64.msi)). This won't work with any Python 3 versions.

Download this project somewhere on your computer. You can do this by clicking the green "Code" button, then "Download ZIP" and extracting it to a folder on your computer.

Specify your `replay_path` in `config.json`. You will (unfortunately) need to ensure all backslashes are escaped by adding a second `\` next to them, it will look something like `C:\\Users\\MyUser\\Documents\\StarCraft II\\Accounts\\12345678\\1-S2-1-1110011\\Replays\\Multiplayer`. 

Execute (i.e. double click on) the `main.py` script. If you install Python 2.7 windows should automatically execute it with the appropriate interpreter.

The script will look for all the SC2Replay files in the specified directory (but not nested directories), parse them, and copy a renamed version into a nested `parsed` directory inside your `replay_path`.

### Skip Existing
By default, the script will skip any parsed files that already exist. This behaviour can be changed by setting `skip_existing` to `false` in `config.json`.

The parsed filename is deterministic, so executing it multiple times for the same replay(s) should always result in the same parsed filename.

### Own Accounts
By specifying account names in `own_accounts` of `config.json` the mmr will not be included for those players in the parsed filename. If you're not sure what to specify for the account name, look at how it is written in a parsed file and use that.


#### TODO
- gitignore config.json
- support mac vs win slashes
