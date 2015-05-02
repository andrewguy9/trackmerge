# trackmerge

Collection of tools for tracking software releases with git.

## ismerged
```
ismerged

Takes a github pull request (either url or number) and a list of branches.
Checks to see if the pull is present in the branches.

usage:
  ismerged [--depot=<path>] <pull> [<branches>...]
```

### Example
```
$ ismerged --depot ~/dev/mongo_mgr/ https://github.com/Livefyre/mongo-mgr/pull/5 master feature
Merged  master
Missing feature
```
```
$ ismerged --depot ~/dev/mongo_mgr/ 5 master feature
Merged  master
Missing feature
```
