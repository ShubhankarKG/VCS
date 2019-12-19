# VCS
A Version Control System

## Current
- [ ] Init
- [ ] Config
- [ ] Add
- [ ] Status
- [ ] Commit
- [ ] Log
- [ ] .vcsignore
- [ ] diff
- [ ] Rollbacks (Reset, Checkout, Rebase)
- [ ] Branches (Merge, Create)

## Later On

- [ ] Remote Things
- [ ] Stash

---
---

### Init
Folder structure: .vcs

#### Folder structure
```
/nodes/  
  {hash}/
    node.vc
    changes.vc
dag.vc  
stage.vc
```

#### Node structure (1 commit)
```
children:
branchName:
commitMessage:
commitUser:
hash:
parents:
timestamp:
type: (Full/Cumulative)
```

#### Patch format (changes.vc - binary file)
```
Dict
key = fileName
type = binary/text
data =
  if binary:
    fileName (hash)
  else:
    list of changes
    (list of changes [lineNo -> (+ or -) change])
```

#### File Structure - init.py
This file is used as a starting point for our Version Control. 
The file contains two functions for handling the init request.
```
check_init.py
init.py
```
Specifically, `init.py` creates a new folder in the current working directory named `vcs` within
which there are the following contents:
*  `nodes` folder for storing hashes
*   `dag, stage, config` files for processing purposes. 

`check_init.py` is a helper function that checks whether the above listed files are present in current working directory.
