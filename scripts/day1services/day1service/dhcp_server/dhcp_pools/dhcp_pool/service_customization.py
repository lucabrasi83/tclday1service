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
                               dhcp-server
                                          |
                                          excluded-address
                                                          
Schema Representation:

/services/day1services/day1service/dhcp-server/excluded-address
"""
"""
Names of Leafs for this Yang Entity
       low-ipaddress            maps-to  /ac:devices/ac:device/l3:dhcp-server/excluded-address/low-ipaddress
      high-ipaddress            maps-to  /ac:devices/ac:device/l3:dhcp-server/excluded-address/high-ipaddress
            vrf-name            maps-to  /ac:devices/ac:device/l3:dhcp-server/excluded-address/vrf-name

"""

from servicemodel import util
from servicemodel import yang
from servicemodel import devicemgr
from servicemodel.controller import devices

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
      modify = False
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']

    @staticmethod
    def process_service_device_bindings(smodelctx, sdata, dev, **kwargs):
      """ Custom API to modify the device bindings or Call the Business Login Handlers"""
      modify = False
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']
        devbindobjs = kwargs['devbindobjs']
        import tclday0config.tclday0config_grouping_lib.dhcp_server_def_customization
        tclday0config.tclday0config_grouping_lib.dhcp_server_def_customization.grouping_create_dhcp_server_def_excluded_address(smodelctx, sdata, dev, **kwargs)


    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      #raise Exception('Update forbidden  for node excluded-address at path day1services/day1service/dhcp-server/excluded-address')
      modify = False
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        import tclday0config.tclday0config_grouping_lib.dhcp_server_def_customization
        tclday0config.tclday0config_grouping_lib.dhcp_server_def_customization.grouping_update_dhcp_server_def_excluded_address(smodelctx, sdata, **kwargs)

    @staticmethod
    def process_service_delete_data(smodelctx, sdata, **kwargs):
      """callback called for delete operation"""
      modify = False
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        import tclday0config.tclday0config_grouping_lib.dhcp_server_def_customization
        tclday0config.tclday0config_grouping_lib.dhcp_server_def_customization.grouping_delete_dhcp_server_def_excluded_address(smodelctx, sdata, **kwargs)

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
