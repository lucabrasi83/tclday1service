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
                               snmp
                                   |
                                   snmp-mib
                                           
Schema Representation:

/services/day1services/day1service/snmp/snmp-mib
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
from servicemodel.controller.devices.device import snmp
import service_customization


class SnmpMib(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'snmp_mib')

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
        inputdict['mib-persistence'] = config.get_field_value('mib_persistence')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['day1services_day1service_device_ip'] = sdata.getRcPath().split('/')[-3].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #snmp_object = devices.device.snmp.snmp()
        snmp_object = snmp.snmp()
        if util.isNotEmpty(inputdict.get('mib-persistence')):
          #snmp_snmp_mib_object = devices.device.snmp.snmp_mib.snmp_mib()
          snmp_snmp_mib_object = snmp.snmp_mib.snmp_mib()
          snmp_snmp_mib_object.mib_persistence = inputdict.get('mib-persistence')


        #End of Device binding
        devbindobjs['snmp_snmp_mib_object'] = snmp_snmp_mib_object

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)
        #Use the custom method to process/create payload

        snmp_snmp_mib_object_payload = snmp_snmp_mib_object.getxml(filter=True)
        log('snmp_snmp_traps_object_payload: %s' % (snmp_snmp_mib_object_payload))
        for dev_iterator in dev:
          yang.Sdk.createData(dev_iterator.url+'/basicDeviceConfigs:snmp',snmp_snmp_mib_object_payload, sdata.getSession(), True)

        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'snmp_mib')
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
        inputdict['mib_persistence'] = config.get_field_value('mib_persistence')
        # END OF FETCHING THE LEAF PARAMETERS

        pinputdict = {}

        # START OF FETCHING THE PREVIOUS LEAF PARAMETERS
        pinputdict['mib_persistence'] = pconfig.get_field_value('mib_persistence')
        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_update_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, pconfig=pconfig, hopaque=opaque_args, inputdict=inputdict, pinputdict=pinputdict)

    def delete(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.delete_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'snmp_mib')
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
        inputdict['mib_persistence'] = config.get_field_value('mib_persistence')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(SnmpMib._instance == None):
            SnmpMib._instance = SnmpMib()
        return SnmpMib._instance
