# VCS: A Git Clone
A basic clone of Git

## Current
- [ ] Init
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
/nodes/  
  {hash}/
    node.vcs
    changes.vcs
dag.vcs  
stage.vcs

#### Node structure (1 commit)
children:  
branchName:  
commitMessage:  
commitUser:  
hash:  
parents:  
timestamp:  
type: (Full/Cumulative)  

#### Patch format (changes.vcs - binary file)
Dict  
key = fileName  
(if binary, direct copy; else)  
list of changes [lineNo -> (+ or -) change]
