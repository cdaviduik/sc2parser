# sc2parser

Starcraft 2 replay parser written in python using sc2reader and mpyq which creates a copy of the replay file containing player names and their mmr.

### Prerequisites

Note, all instructions assume you are running this on windows, but it does work on mac as well.

Download [Python 2.7](https://www.python.org/download/releases/2.7/) (probably [this one](https://www.python.org/ftp/python/2.7/python-2.7.amd64.msi)). This won't work with any Python 3 versions.

Download this project somewhere on your computer. You can do this by clicking the green "Code" button, then "Download ZIP" and extracting it to a folder on your computer.

### Config
The project comes with a `default_config.json` file that you will need to make a copy of named `config.json`. See below for a description about each config field.

#### Replays Path
The path to the directory to search for replays. You will (unfortunately) need to ensure all backslashes are escaped by adding a second `\` next to them, it will look something like:

```
C:\\Users\\MyUser\\Documents\\StarCraft II\\Accounts\\12345678\\1-S2-1-1110011\\Replays\\Multiplayer
```

Execute (i.e. double click on) the `main.py` script. If you installed Python 2.7, windows should automatically execute it with the appropriate interpreter.

#### Parsed Replays Path
The path to copy the parsed replays to. As with the `replays_path`, backslashes need to be escaped. This might looks something like:

```
C:\\Users\\MyUser\\Documents\\StarCraft II\\Accounts\\12345678\\1-S2-1-1110011\\Replays\\Multiplayer\\My Parsed Replays
```

Although note, the `parsed_replays_path` does not have to be inside the `replays_path`, and can be anywhere on your computer.

**WARNING: do not include a trailing slash in the path name, otherwise the script will be unable to match it, and try parsing the replays inside if its under the `replays_path`**

### Skip Existing
By default, the script will skip any parsed files that already exist. This behaviour can be changed by setting `skip_existing` to `false` in `config.json`.

The parsed filename is deterministic, so executing it multiple times for the same replay(s) should always result in the same parsed filename.

### Own Accounts
By specifying account names in `own_accounts` of `config.json` the mmr will not be included for those players in the parsed filename. If you're not sure what to specify for the account name, look at how it is written in a parsed file and use that.

### Poll Interval
The time in seconds between each execution of the script. Currently set to 900s (15min) by default.

### Path Separator
On windows (default) ``\\`, on mac `/`.
