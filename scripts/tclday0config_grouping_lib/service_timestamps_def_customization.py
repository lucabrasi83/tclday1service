
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
service-timestamps-debug            maps-to  /ac:devices/ac:device/bdc:service-time-stamps/service-timestamps-debug
service-timestamps-log            maps-to  /ac:devices/ac:device/bdc:service-time-stamps/service-timestamps-log
service-password-encryption            maps-to  /ac:devices/ac:device/bdc:service-time-stamps/service-password-encryption
       enable-secret            maps-to  /ac:devices/ac:device/bdc:service-time-stamps/enable-secret
enable-secret-password            maps-to  /ac:devices/ac:device/bdc:service-time-stamps/enable-secret-password
   tcp-keepalives-in            maps-to  /ac:devices/ac:device/bdc:service-time-stamps/tcp-keepalives-in
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_service_timestamps_def_(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_service_timestamps_def_(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_service_timestamps_def_(smodelctx, sdata, **kwargs):
    pass
