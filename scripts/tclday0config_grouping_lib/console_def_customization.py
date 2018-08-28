
from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller import devices

import copy

from tclday0config.tclday0config_lib import getLocalObject
from tclday0config.tclday0config_lib import getDeviceObject
from tclday0config.tclday0config_lib import getCurrentObjectConfig
from tclday0config.tclday0config_lib import ServiceModelContext
from tclday0config.tclday0config_lib import getParentObject
from tclday0config.tclday0config_lib import log

"""
Names of Leafs for this Yang Entity
        console-line            maps-to  /ac:devices/ac:device/bdc:console/console-line
        exec-timeout            maps-to  /ac:devices/ac:device/bdc:console/exec-timeout
     privilege-level            maps-to  /ac:devices/ac:device/bdc:console/privilege-level
 logging-synchronous            maps-to  /ac:devices/ac:device/bdc:console/logging-synchronous
         no-password            maps-to  /ac:devices/ac:device/bdc:console/no-password
           auth-type            maps-to  /ac:devices/ac:device/bdc:console/auth-type
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_console_def_(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_console_def_(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_console_def_(smodelctx, sdata, **kwargs):
    pass
