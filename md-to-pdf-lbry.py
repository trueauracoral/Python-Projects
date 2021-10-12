########################
# THIS IS GPL V3 STUFF.#
########################

# This is a plugin that converts .md to .pdf The program used for the
# convertion is a wonderfule program called pandoc.

# Import sys this is what allows us to make make arguments.
import sys
# Import subprocess to run system commands
import subprocess

# This variable stores are sys command. This is where the user can give a file.
md = sys.argv[1]

subprocess.run(["pandoc", "-f", "markdown", "-t", "latex", "-o", "vim-to-neovim.tex", md])
