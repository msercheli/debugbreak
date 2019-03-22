# -*- coding: utf-8 -*-

name = 'debugbreak'

# since the author don't specify version semantics, I am using date and commit
version = '2019.03.22.5d62081'

description = \
    """
    Break into the debugger programmatically
    """
authors = ['Scott Tsai']

def commands():
    #env.PYTHONPATH.append("{root}/python")
    #env.PATH.append("{root}/bin/{system.platform}")
    env.REZ_DEBUGBREAK_INCLUDE_PATH = "{root}/include"

uuid = 'repository.debugbreak'

