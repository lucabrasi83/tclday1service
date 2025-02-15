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
                               local-credentials
                                                |
                                                local-credential
                                                                
Schema Representation:

/services/day1services/day1service/local-credentials/local-credential
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
from servicemodel.controller.devices.device import local_credentials
import service_customization


class LocalCredential(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'local_credential')

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
        inputdict['name'] = config.get_field_value('name')
        inputdict['password'] = config.get_field_value('password')
        inputdict['password_level'] = config.get_field_value('password_level')
        inputdict['enable_privilege'] = config.get_field_value('enable_privilege')
        inputdict['privilege_level'] = config.get_field_value('privilege_level')
        inputdict['privilege_secret'] = config.get_field_value('privilege_secret')
        inputdict['secret_level'] = config.get_field_value('secret_level')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['day1services_day1service_device_ip'] = sdata.getRcPath().split('/')[-3].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)

        #Start of Device binding with python bindings
        #local_credentials_object = devices.device.local_credentials.local_credentials()
        local_credentials_object = local_credentials.local_credentials()
        if util.isNotEmpty(inputdict.get('name')):
          #local_credentials_local_credential_object = devices.device.local_credentials.local_credential.local_credential()
          local_credentials_local_credential_object = local_credentials.local_credential.local_credential()
          local_credentials_local_credential_object.name = inputdict.get('name')
          local_credentials_local_credential_object.password = inputdict.get('password')
          local_credentials_local_credential_object.enable_privilege = inputdict.get('enable_privilege')
          local_credentials_local_credential_object.privilege_level = inputdict.get('privilege_level')
          if util.isNotEmpty(local_credentials_local_credential_object.password):
            if util.isNotEmpty(inputdict.get('password_level')):
                local_credentials_local_credential_object.password_level = inputdict.get('password_level')
          local_credentials_local_credential_object.secret_password = inputdict.get('privilege_secret')
          if util.isNotEmpty(local_credentials_local_credential_object.secret_password):
            local_credentials_local_credential_object.enable_secret = True
            if util.isNotEmpty(inputdict.get('secret_level')):
                local_credentials_local_credential_object.secret_level = inputdict.get('secret_level')

        #End of Device binding
        devbindobjs['local_credentials_local_credential_object'] = local_credentials_local_credential_object
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)
        #for dev_iterator in dev:
          #yang.Sdk.createData(dev_iterator.url,'<local-credentials/>', sdata.getSession(), True)


        local_credentials_local_credential_object_payload = local_credentials_local_credential_object.getxml(filter=True)
        #log('local_credentials_local_credential_object_payload: %s' % (local_credentials_local_credential_object_payload))
        for dev_iterator in dev:
          yang.Sdk.createData(dev_iterator.url+'/basicDeviceConfigs:local-credentials',local_credentials_local_credential_object_payload, sdata.getSession(), True)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'local_credential')
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
        inputdict['name'] = config.get_field_value('name')
        inputdict['password'] = config.get_field_value('password')
        inputdict['password_level'] = config.get_field_value('password_level')
        inputdict['enable_privilege'] = config.get_field_value('enable_privilege')
        inputdict['privilege_level'] = config.get_field_value('privilege_level')
        inputdict['privilege_secret'] = config.get_field_value('privilege_secret')
        inputdict['secret_level'] = config.get_field_value('secret_level')
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
        config = getCurrentObjectConfig(id, sdata, 'local_credential')
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
        inputdict['name'] = config.get_field_value('name')
        inputdict['password'] = config.get_field_value('password')
        inputdict['password_level'] = config.get_field_value('password_level')
        inputdict['enable_privilege'] = config.get_field_value('enable_privilege')
        inputdict['privilege_level'] = config.get_field_value('privilege_level')
        inputdict['privilege_secret'] = config.get_field_value('privilege_secret')
        inputdict['secret_level'] = config.get_field_value('secret_level')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(LocalCredential._instance == None):
            LocalCredential._instance = LocalCredential()
        return LocalCredential._instance

    def rollbackCreate(self, id, sdata):
        log('rollback: id = %s, sdata = %s' % (id, sdata))
        self.delete(id,sdata)

if __name__ == 'local_credential':
  from servicemodel.yang import YangServiceData
  sdata = YangServiceData()
  instance = LocalCredential().getInstance()
  instance.create(None, sdata)
  instance.delete(None, sdata)
  instance.update(None, sdata)
