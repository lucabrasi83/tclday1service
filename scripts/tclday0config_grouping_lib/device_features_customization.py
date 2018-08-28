
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
                 cdp            maps-to  /ac:devices/ac:device/bdc:features/cdp
       domain-lookup            maps-to  /ac:devices/ac:device/bdc:features/domain-lookup
   tcp-small-servers            maps-to  /ac:devices/ac:device/bdc:features/tcp-small-servers
   udp-small-servers            maps-to  /ac:devices/ac:device/bdc:features/udp-small-servers
              finger            maps-to  /ac:devices/ac:device/bdc:features/finger
        source-route            maps-to  /ac:devices/ac:device/bdc:features/source-route
        bootp-server            maps-to  /ac:devices/ac:device/bdc:features/bootp-server
         http-server            maps-to  /ac:devices/ac:device/bdc:features/http-server
  http-secure-server            maps-to  /ac:devices/ac:device/bdc:features/http-secure-server
         banner-exec            maps-to  /ac:devices/ac:device/bdc:features/banner-exec
        banner-login            maps-to  /ac:devices/ac:device/bdc:features/banner-login
         banner-motd            maps-to  /ac:devices/ac:device/bdc:features/banner-motd
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_device_features_(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_device_features_(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_device_features_(smodelctx, sdata, **kwargs):
    pass
