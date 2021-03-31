# sc2parser

Add replay path to `config.json` and execute script.

It will find all the SC2Replay files in the specified directory, parse them, and copy a renamed version into a nested `parsed` directory.

### Skip Existing
By default, the script will skip any parsed files that already exist. This behaviour can be changed by setting `skip_existing` to `false` in `config.json`.

Having said that, the parsed filename is deterministic, so executing it multiple times for the same replay(s) should always result in the same parsed filename.

### Own Accounts
By specifying account names in `own_accounts` of `config.json` the mmr will not be included for those players in the parsed filename.
