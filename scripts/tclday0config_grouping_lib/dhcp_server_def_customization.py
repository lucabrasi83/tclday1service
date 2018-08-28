
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
           pool-name            maps-to  /ac:devices/ac:device/l3:dhcp-server/pool-name
            pool-vrf            maps-to  /ac:devices/ac:device/l3:dhcp-server/pool-vrf
             network            maps-to  /ac:devices/ac:device/l3:dhcp-server/network
                mask            maps-to  /ac:devices/ac:device/l3:dhcp-server/mask
         domain-name            maps-to  /ac:devices/ac:device/l3:dhcp-server/domain-name
      dhcp-server-ip            maps-to  /ac:devices/ac:device/l3:dhcp-server/dhcp-server-ip
       dns-server-ip            maps-to  /ac:devices/ac:device/l3:dhcp-server/dns-server-ip
      default-router            maps-to  /ac:devices/ac:device/l3:dhcp-server/default-router
      interface-name            maps-to  /ac:devices/ac:device/l3:dhcp-server/interface-name
            start-ip            maps-to  /ac:devices/ac:device/l3:dhcp-server/start-ip
              end-ip            maps-to  /ac:devices/ac:device/l3:dhcp-server/end-ip
               lease            maps-to  /ac:devices/ac:device/l3:dhcp-server/lease

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_dhcp_server_def_(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_dhcp_server_def_(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_dhcp_server_def_(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
       low-ipaddress            maps-to  /ac:devices/ac:device/l3:dhcp-server/excluded-address/low-ipaddress
      high-ipaddress            maps-to  /ac:devices/ac:device/l3:dhcp-server/excluded-address/high-ipaddress
            vrf-name            maps-to  /ac:devices/ac:device/l3:dhcp-server/excluded-address/vrf-name

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_dhcp_server_def_excluded_address(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_dhcp_server_def_excluded_address(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_dhcp_server_def_excluded_address(smodelctx, sdata, **kwargs):
    pass
