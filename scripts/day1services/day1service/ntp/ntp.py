#
# This computer program is the confidential information and proprietary trade
# secret of Anuta Networks, Inc. Possessions and use of this program must
# conform strictly to the license agreement between the user and
# Anuta Networks, Inc., and receipt or possession does not convey any rights
# to divulge, reproduce, or allow others to use this program without specific
# written authorization of Anuta Networks, Inc.
#
# Copyright (c) 2015-2016 Anuta Networks, Inc. All Rights Reserved.
#

#
#DO NOT EDIT THIS FILE ITS AUTOGENERATED ONE
#ALL THE CUSTOMIZATIONS REGARDING DATAPROCESSING SHOULD BE WRITTEN INTO service_customization.py FILE
#
"""
Tree Structure of Handled XPATH:

services
        |
        day1services
                    |
                    day1service
                               |
                               ntp
                                  
Schema Representation:

/services/day1services/day1service/ntp
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

#from servicemodel.controller import devices
from servicemodel.controller.devices.device import ntp
import service_customization


class Ntp(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'ntp')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['access_group_name'] = config.get_field_value('access_group_name')
        inputdict['ntp_source_interface'] = config.get_field_value('ntp_source_interface')
        inputdict['update_calendar'] = config.get_field_value('update_calendar')
        if inputdict.get('update_calendar') is None:
          inputdict['update_calendar'] = 'False'
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['day1services_day1service_device_ip'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)

        #Start of Device binding with python bindings
        #ntp_object = devices.device.ntp.ntp()
        ntp_object = ntp.ntp()
        ntp_object.ntp = inputdict.get('access_group_name')
        ntp_object.ntp_source_interface = inputdict.get('ntp_source_interface')
        ntp_object.update_calendar = inputdict.get('update_calendar')


        #End of Device binding
        devbindobjs['ntp_object'] = ntp_object
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

        ntp_object_payload = ntp_object.getxml(filter=True)
        #log('ntp_object_payload: %s' % (ntp_object_payload))
        for dev_iterator in dev:
          yang.Sdk.createData(dev_iterator.url+'',ntp_object_payload, sdata.getSession(), True)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'ntp')
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['access_group_name'] = config.get_field_value('access_group_name')
        inputdict['ntp_source_interface'] = config.get_field_value('ntp_source_interface')
        inputdict['update_calendar'] = config.get_field_value('update_calendar')
        if inputdict.get('update_calendar') is None:
          inputdict['update_calendar'] = 'False'
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'ntp')
        opaque_args = self.opaque_args

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['access_group_name'] = config.get_field_value('access_group_name')
        inputdict['ntp_source_interface'] = config.get_field_value('ntp_source_interface')
        inputdict['update_calendar'] = config.get_field_value('update_calendar')
        if inputdict.get('update_calendar') is None:
          inputdict['update_calendar'] = 'False'
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(Ntp._instance == None):
            Ntp._instance = Ntp()
        return Ntp._instance

    def rollbackCreate(self, id, sdata):
        log('rollback: id = %s, sdata = %s' % (id, sdata))
        self.delete(id,sdata)

if __name__ == 'ntp':
  from servicemodel.yang import YangServiceData
  sdata = YangServiceData()
  instance = Ntp().getInstance()
  instance.create(None, sdata)
  instance.delete(None, sdata)
  instance.update(None, sdata)
