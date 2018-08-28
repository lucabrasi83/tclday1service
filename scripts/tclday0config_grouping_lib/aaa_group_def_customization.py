
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
 tacacs-server-group            maps-to  /ac:devices/ac:device/bdc:aaa-group/tacacs-server-group
    source-interface            maps-to  /ac:devices/ac:device/bdc:aaa-group/source-interface
       aaa-new-model            maps-to  /ac:devices/ac:device/bdc:aaa-group/aaa-new-model
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_aaa_group_def_(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_aaa_group_def_(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_aaa_group_def_(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
       aaa-server-ip            maps-to  /ac:devices/ac:device/bdc:aaa-group/bdc:aaa-servers-private/aaa-server-private
     privilege-level            maps-to  /ac:devices/ac:device/bdc:aaa-group/bdc:aaa-servers-private/privilege-level
       privilege-key            maps-to  /ac:devices/ac:device/bdc:aaa-group/bdc:aaa-servers-private/privilege-key
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_aaa_group_def_aaa_servers_private(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_aaa_group_def_aaa_servers_private(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_aaa_group_def_aaa_servers_private(smodelctx, sdata, **kwargs):
    pass
