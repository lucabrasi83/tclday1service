
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
         banner-motd            maps-to  /ac:devices/ac:device[ac:id=current()/../../device-ip]/bdc:banner/motd-message
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_banner_def_(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_banner_def_(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_banner_def_(smodelctx, sdata, **kwargs):
    pass
