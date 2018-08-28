
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
            acl-name            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/name
            acl-type            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/acl-type
              remark            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/start-remark
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_access_lists_def_acl(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_access_lists_def_acl(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_access_lists_def_acl(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
match-condition-name            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/acl-rules/acl-rule/name
source-condition-type            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/acl-rules/acl-rule/source-condition-type
 source-ipv4-address            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/acl-rules/acl-rule/source-ip
source-ipv4-address-mask            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/acl-rules/acl-rule/source-mask
 dest-condition-type            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/acl-rules/acl-rule/dest-condition-type
destination-ipv4-address            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/acl-rules/acl-rule/dest-ip
destination-ipv4-address-mask            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/acl-rules/acl-rule/dest-mask
              action            maps-to  /ac:devices/ac:device/acl:access-lists/access-list/acl-rules/acl-rule/action
"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_access_lists_def_acl_match_condition(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_access_lists_def_acl_match_condition(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_access_lists_def_acl_match_condition(smodelctx, sdata, **kwargs):
    pass
