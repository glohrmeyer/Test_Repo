#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      glohrmeyer
#
# Created:     12/02/2014
# Copyright:   (c) glohrmeyer 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

for dirname, dirnames, filenames in os.walk(r'\\red\projects\0\0497120\CAD'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print os.path.join(dirname, subdirname)

    # print path to all filenames.
    for filename in filenames:
        print os.path.join(dirname, filename)

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if 'County' not in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')