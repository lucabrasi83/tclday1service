
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

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_scripts_def_eem_script(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_scripts_def_eem_script(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_scripts_def_eem_script(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_scripts_def_eem_script_eem_if_errors(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_scripts_def_eem_script_eem_if_errors(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_scripts_def_eem_script_eem_if_errors(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
              if-tag            maps-to  /ac:devices/ac:device/eem-script/eem-if-errors/interface/if-tag
      interface-name            maps-to  /ac:devices/ac:device/eem-script/eem-if-errors/interface/interface-name
           correlate            maps-to  /ac:devices/ac:device/eem-script/eem-if-errors/interface/correlate
           variable1            maps-to  /ac:devices/ac:device/eem-script/eem-if-errors/interface/variable1
           variable2            maps-to  /ac:devices/ac:device/eem-script/eem-if-errors/interface/variable2
           variable3            maps-to  /ac:devices/ac:device/eem-script/eem-if-errors/interface/variable3

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_scripts_def_eem_script_eem_if_errors_interface(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_scripts_def_eem_script_eem_if_errors_interface(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_scripts_def_eem_script_eem_if_errors_interface(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
  enable-bgp-adj-eem            maps-to  /ac:devices/ac:device/eem-script/eem-bgp-adj/enable-bgp-adj-eem
           variable1            maps-to  /ac:devices/ac:device/eem-script/eem-bgp-adj/variable1
           variable2            maps-to  /ac:devices/ac:device/eem-script/eem-bgp-adj/variable2
           variable3            maps-to  /ac:devices/ac:device/eem-script/eem-bgp-adj/variable3

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_scripts_def_eem_script_eem_bgp_adj(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_scripts_def_eem_script_eem_bgp_adj(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_scripts_def_eem_script_eem_bgp_adj(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
enable-eigrp-adj-eem            maps-to  /ac:devices/ac:device/eem-script/eem-eigrp-adj/enable-eigrp-adj-eem
           variable1            maps-to  /ac:devices/ac:device/eem-script/eem-eigrp-adj/variable1
           variable2            maps-to  /ac:devices/ac:device/eem-script/eem-eigrp-adj/variable2
           variable3            maps-to  /ac:devices/ac:device/eem-script/eem-eigrp-adj/variable3

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_scripts_def_eem_script_eem_eigrp_adj(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_scripts_def_eem_script_eem_eigrp_adj(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_scripts_def_eem_script_eem_eigrp_adj(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
 enable-ospf-adj-eem            maps-to  /ac:devices/ac:device/eem-script/eem-ospf-adj/enable-ospf-adj-eem
           variable1            maps-to  /ac:devices/ac:device/eem-script/eem-ospf-adj/variable1
           variable2            maps-to  /ac:devices/ac:device/eem-script/eem-ospf-adj/variable2
           variable3            maps-to  /ac:devices/ac:device/eem-script/eem-ospf-adj/variable3

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_scripts_def_eem_script_eem_ospf_adj(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_scripts_def_eem_script_eem_ospf_adj(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_scripts_def_eem_script_eem_ospf_adj(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
    rising-threshold            maps-to  /ac:devices/ac:device/eem-script/eem-cpu-threshold/rising-threshold
rising-threshold-interval            maps-to  /ac:devices/ac:device/eem-script/eem-cpu-threshold/rising-threshold-interval
   falling-threshold            maps-to  /ac:devices/ac:device/eem-script/eem-cpu-threshold/falling-threshold
falling-threshold-interval            maps-to  /ac:devices/ac:device/eem-script/eem-cpu-threshold/falling-threshold-interval
           variable1            maps-to  /ac:devices/ac:device/eem-script/eem-cpu-threshold/variable1
           variable2            maps-to  /ac:devices/ac:device/eem-script/eem-cpu-threshold/variable2
           variable3            maps-to  /ac:devices/ac:device/eem-script/eem-cpu-threshold/variable3

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_scripts_def_eem_script_eem_cpu_threshold(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_scripts_def_eem_script_eem_cpu_threshold(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_scripts_def_eem_script_eem_cpu_threshold(smodelctx, sdata, **kwargs):
    pass

"""
Names of Leafs for this Yang Entity
enable-mem-threshold-eem            maps-to  /ac:devices/ac:device/eem-script/eem-mem-threshold/enable-mem-threshold-eem
           variable1            maps-to  /ac:devices/ac:device/eem-script/eem-mem-threshold/variable1
           variable2            maps-to  /ac:devices/ac:device/eem-script/eem-mem-threshold/variable2

"""

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_create_eem_scripts_def_eem_script_eem_mem_threshold(smodelctx, sdata, dev, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_update_eem_scripts_def_eem_script_eem_mem_threshold(smodelctx, sdata, **kwargs):
    pass

"""
Contents of kwargs
config = kwargs['config']
inputdict = kwargs['inputdict']
devbindobjs = kwargs['devbindobjs']

devices is list

Fetch the parent object using getParentObject() API 
"""
def grouping_delete_eem_scripts_def_eem_script_eem_mem_threshold(smodelctx, sdata, **kwargs):
    pass
