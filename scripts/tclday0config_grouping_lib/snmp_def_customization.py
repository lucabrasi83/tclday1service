
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
write-community-string            maps-to  /ac:devices/ac:device/bdc:snmp/rw-community
            acl-name            maps-to  /ac:devices/ac:device/bdc:snmp/acl-name
snmp-ifmib-ifindex-persist            maps-to  /ac:devices/ac:device/bdc:snmp/snmp-ifmib-ifindex-persist
         trap-source            maps-to  /ac:devices/ac:device/bdc:snmp/trap-source
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_snmp_def_(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_snmp_def_(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_snmp_def_(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
    community-string            maps-to  /ac:devices/ac:device/bdc:snmp/snmp-community-list/snmp-string
      permision-type            maps-to  /ac:devices/ac:device/bdc:snmp/snmp-community-list/permission-type
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_snmp_def_snmp_community(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_snmp_def_snmp_community(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_snmp_def_snmp_community(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
                host            maps-to  /ac:devices/ac:device/bdc:snmp/snmp-server/snmp-server-ip
             version            maps-to  /ac:devices/ac:device/bdc:snmp/snmp-server/snmp-version
      snmp-community            maps-to  /ac:devices/ac:device/bdc:snmp/snmp-server/community
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_snmp_def_snmp_host(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_snmp_def_snmp_host(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_snmp_def_snmp_host(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
                trap            maps-to  /ac:devices/ac:device/bdc:snmp/snmp-traps/snmp-trap
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_snmp_def_snmp_traps(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_snmp_def_snmp_traps(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_snmp_def_snmp_traps(smodelctx, sdata, **kwargs):
    pass
