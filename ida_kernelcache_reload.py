#
# ida_kernelcache.py
# Brandon Azad
#
# A script to import the ida_kernelcache module into IDA, reloading all the necessary internal
# modules.
#

from __future__ import absolute_import

import sys

for mod in list(sys.modules.keys()):
    if 'ida_kernelcache' in mod:
        del sys.modules[mod]

