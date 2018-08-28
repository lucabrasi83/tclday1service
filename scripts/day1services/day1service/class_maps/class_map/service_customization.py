#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2016-2017 Anuta Networks, Inc. All Rights Reserved.
#

#
#ALL THE CUSTOMIZATIONS REGARDING DATAPROCESSING SHOULD BE WRITTEN INTO THIS FILE
#
"""
Tree Structure of Handled XPATH:

services
        |
        day1services
                    |
                    day1service
                               |
                               class-maps
                                         |
                                         class-map
                                                  
Schema Representation:

/services/day1services/day1service/class-maps/class-map
"""
"""
Names of Leafs for this Yang Entity
                name
         description
          match-type

"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr

from tclday0config.tclday0config_lib import getLocalObject
from tclday0config.tclday0config_lib import getDeviceObject
from tclday0config.tclday0config_lib import getCurrentObjectConfig
from tclday0config.tclday0config_lib import ServiceModelContext
from tclday0config.tclday0config_lib import getParentObject 
from tclday0config.tclday0config_lib import log

class ServiceDataCustomization:

    @staticmethod
    def process_service_create_data(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the inputs"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']

    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the device bindings or Call the Business Login Handlers"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']
        devbindobjs = kwargs['devbindobjs']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']
#        import tclday0config.tclday0config_grouping_lib.common_config_def_customization
#        tclday0config.tclday0config_grouping_lib.common_config_def_customization.grouping_create_common_config_def_class_maps_class_map(smodelctx, sdata, dev, xpath='day1services/day1service/class-maps/class-map', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return


    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']

        #Previous config and previous inputdict
        pconfig = kwargs['pconfig']
        pinputdict = kwargs['pinputdict']

        dev = kwargs['dev']
 #       import tclday0config.tclday0config_grouping_lib.common_config_def_customization
 #       tclday0config.tclday0config_grouping_lib.common_config_def_customization.grouping_update_common_config_def_class_maps_class_map(smodelctx, sdata, xpath='day1services/day1service/class-maps/class-map', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.items():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        dev = kwargs['dev']
        id = kwargs['id']
        opaque_args = kwargs['hopaque']

  #      import tclday0config.tclday0config_grouping_lib.common_config_def_customization
  #      tclday0config.tclday0config_grouping_lib.common_config_def_customization.grouping_delete_common_config_def_class_maps_class_map(smodelctx, sdata, xpath='day1services/day1service/class-maps/class-map', **kwargs)

        if dev is None or (isinstance(dev, list) and len(dev) == 0):
          return

class DeletePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for Deletion"""
        log('operations: %s' % (operations))

class CreatePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for creation"""
        log('operations: %s' % (operations))
