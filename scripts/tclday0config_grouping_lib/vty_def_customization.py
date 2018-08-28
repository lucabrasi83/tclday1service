
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
                name            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/name
      timeout-in-sec
      timeout-in-min            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/timeout
             min-vty            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/min-vty
             max-vty            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/max-vty
      transport-type            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/transport-types-in
                 acl            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/acl-rule-number
 logging-synchronous            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/logging-synchronous
        history-size            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/history-size
  no-privilege-level            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/no-privilege-level
         no-password            maps-to  /ac:devices/ac:device/bdc:vty-configs/vty-config/no-password
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_vty_def_(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_vty_def_(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_vty_def_(smodelctx, sdata, **kwargs):
    pass
