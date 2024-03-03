# README for the flex.pkg file format
Example file inluded

# Functions:
## pkg
Installs packages using the os package manager
## flatpak
Installs packages from flatpak (Linux only)
## git (1,2 or 3)
Clones a git repo
## cmd
Runs a command
## get (1,2 or 3)
Downloads a file using WGET
## sh
Runs a .sh file (Linux only)
## batch
Runs a .bat file (Windows only)

# Execution order:
pkg,git,get,flat,cmd and batch