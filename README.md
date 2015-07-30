# trackmerge

Collection of tools for tracking software releases with git.

# Installation

```
pip install trackmerge
```

# Usage

## ismerged
```
ismerged

Takes a github pull request (either url or number) and a list of branches.
Checks to see if the pull is present in the branches.

usage:
  ismerged [options] --pull=<pull> [<branches>...]
  ismerged [options] --rev=<rev>   [<branches>...]

Options:
  -h --help      Show this screen.
  --version      Show version.
  --depot=<path> Use this depot.
```

### Example
```
$ ismerged --pull https://github.com/Livefyre/mongo-mgr/pull/86 origin/master origin/stream
Merged  origin/master
Missing origin/stream
```
You can choose to use the pull request number rather than URL as well.
```
$ ismerged --pull 86 origin/master origin/stream
Merged  origin/master
Missing origin/stream
```

## isreleased
```
isreleased

Takes a github pull request (either url or number) or a rev.
Checks to see which releases contain the object.

usage:
  isreleased [options] --pull=<pull>
  isreleased [options] --rev=<pull>

Options:
  -h --help      Show this screen.
  --version      Show version.
  --depot=<path> Use this depot.
```

### Example
```
$ isreleased --depot ~/dev/streamhub-sdk/ --pull https://github.com/Livefyre/mongo-mgr/pull/86
v2.16.2
v2.16.1
v2.16.0
v2.15.4+build.515
v2.15.4
v2.15.3+build.513
v2.15.3+build.106
v2.15.3+build.105
v2.15.3
v2.15.2+build.512
...
```
