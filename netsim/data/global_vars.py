#
# Implement global variables hidden within topology defaults
#
# Needed to support reentrant use of netsim modules (custom transformations or tests)
#

import typing
from box import Box
from ..common import fatal

_topology: typing.Optional[Box] = None
_globals:  typing.Optional[Box] = None

'''
init -- create 'globals' entry in 'topology.defaults' and save a pointer to it

It would be ideal to get a pointer to topology in every call to 'get', but
that's not realistic.
'''

def init(topology: Box) -> None:
  global _topology,_globals

  _topology = topology
  _globals  = topology.defaults._globals


'''
get -- get a pointer to a global Box (referenced by name) hidden in topology
'''

def get(varname: str) -> Box:
  if _globals is None:
    fatal(f'Trying to get global variable {varname} before the global_vars subsystem is initialized')
    return Box({})                  # pragma: no cover -- fatal aborts, but we need to return the right object to keep mypy happy

  return _globals[varname]
