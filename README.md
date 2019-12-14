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