"""Set up a new MSMBuilder project

"""
# Author: Matthew Harrigan <matthew.harrigan@outlook.com>
# Contributors:
# Copyright (c) 2016, Stanford University
# All rights reserved.

from __future__ import print_function, division, absolute_import

import os
import stat
import textwrap

from ..cmdline import NumpydocClassCommand
from ..io import ProjectTemplate


def chmod_plus_x(fn):
    st = os.stat(fn)
    os.chmod(fn, st.st_mode | stat.S_IEXEC)


class ProjectTemplateCommand(NumpydocClassCommand):
    _group = '0-Support'
    _concrete = True
    description = __doc__
    klass = ProjectTemplate

    def start(self):
        self.instance.write_all()

        print('\n'.join(textwrap.wrap(
            "Ok, I wrote out a bunch of Python files that can guide you "
            "through analyzing a system with MSMBuilder. I implore you to "
            "look at the scripts before you start blindly running them. "
            "You will likely have to change some (hyper-)parameters or "
            "filenames to match your particular project."
        )))
        print()
        print('\n'.join(textwrap.wrap(
            "More than that, however, it is important that you understand "
            "exactly what the scripts are doing. Each protein system is "
            "different, and it is up to you (the researcher) to hone in on "
            "interesting aspects. This very generic pipeline may not give "
            "you any new insight for anything but the simplest systems."
        )))
