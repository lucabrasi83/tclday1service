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
                               named-access-lists
                                                 |
                                                 acl
                                                    |
                                                    match-condition
                                                                   
Schema Representation:

/services/day1services/day1service/named-access-lists/acl/match-condition
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
from servicemodel.controller.devices.device import access_lists
import service_customization


class MatchCondition(yang.AbstractYangServiceHandler):
    _instance = None

    def __init__(self):
        self.delete_pre_processor = service_customization.DeletePreProcessor()
        self.create_pre_processor = service_customization.CreatePreProcessor()
        self.opaque_args = {}

    def create(self, id, sdata):
        sdata.getSession().addYangSessionPreReserveProcessor(self.create_pre_processor)

        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'match_condition')

        #Fetch Service Model Context Object
        smodelctx = None

        #Fetch Parent Object
        parentobj = None

        dev = []
        inputkeydict = {}
        devbindobjs={}
        inputdict = {}
        opaque_args = self.opaque_args
 
        if config.get_field_value('cidr') == "true":
            prefix_in = config.get_field_value('cidr_value')
            prefix = util.IPPrefix(prefix_in)
            ip_address = prefix.address
            wildcard = prefix.wildcard
            source_ipv4_address = ip_address
            source_ipv4_mask = wildcard
        else:
            source_ipv4_address = config.get_field_value('source_ipv4_address')
            source_ipv4_mask = config.get_field_value('source_ipv4_address_mask')

        if config.get_field_value('cidr') == "true" and config.get_field_value('cidr_destination_value') !=None:
            prefix_in = config.get_field_value('cidr_destination_value')
            prefix = util.IPPrefix(prefix_in)
            ip_address = prefix.address
            wildcard = prefix.wildcard
            destination_ipv4_address = ip_address
            destination_ipv4_mask = wildcard
        else:
            destination_ipv4_address = config.get_field_value('destination_ipv4_address')
            destination_ipv4_mask = config.get_field_value('destination_ipv4_address_mask')

        # START OF FETCHING THE LEAF PARAMETERS
        inputdict['sequence_number'] = config.get_field_value('sequence_number')
        inputdict['match_condition_name'] = config.get_field_value('match_condition_name')
        inputdict['match_packets'] = config.get_field_value('match_packets')
        inputdict['source_condition_type'] = config.get_field_value('source_condition_type')
        inputdict['source_ipv4_address'] = source_ipv4_address
        inputdict['source_ipv4_address_mask'] = source_ipv4_mask
        '''
        if config.get_field_value('dest_condition_type') is None:
          if inputdict['source_condition_type'] == 'host':
            inputdict['dest_condition_type'] = 'host'
          if inputdict['source_condition_type'] == 'cidr':
            inputdict['dest_condition_type'] = 'cidr'
          if inputdict['source_condition_type'] == 'any':
            inputdict['dest_condition_type'] = None
        else:
          inputdict['dest_condition_type'] = config.get_field_value('dest_condition_type')
        inputdict['cidr_destination_value'] = config.get_field_value('cidr_destination_value')
        inputdict['destination_ipv4_address'] = destination_ipv4_address
        inputdict['destination_ipv4_address_mask'] = destination_ipv4_mask
        '''
        inputdict['action'] = config.get_field_value('action')


        acl_name = inputdict['action']

        if inputdict['source_condition_type'] == 'host':
          acl_name = acl_name + ' ' + 'host' + ' '+ inputdict['source_ipv4_address']
        
        if inputdict['source_condition_type'] == "cidr":
          acl_name = acl_name + ' ' + inputdict['source_ipv4_address'] + ' ' + inputdict['source_ipv4_address_mask']

        if inputdict['source_condition_type'] == "any":
	      acl_name = acl_name + ' ' + 'any'

        #if inputdict['dest_condition_type'] == "host" and inputdict['destination_ipv4_address'] != None:
          #acl_name = acl_name + ' ' + 'host' + ' ' + inputdict['destination_ipv4_address']

        #if inputdict['destination_ipv4_address'] != None and inputdict['destination_ipv4_address_mask'] !=None:
          #acl_name = acl_name + ' ' + inputdict['destination_ipv4_address'] + ' ' + inputdict['destination_ipv4_address_mask']

        if inputdict['match_packets']!= None:
	       acl_name = acl_name + ' ' + inputdict['match_packets']
    
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        # START OF FETCHING THE PARENT KEY LEAF PARAMETERS
        inputkeydict['day1services_day1service_named_access_lists_acl_acl_name'] = sdata.getRcPath().split('/')[-2].split('=')[1]
        inputkeydict['day1services_day1service_device_ip'] = sdata.getRcPath().split('/')[-4].split('=')[1]
        # END OF FETCHING THE PARENT KEY LEAF PARAMETERS

        #Use the custom methods to process the data
        service_customization.ServiceDataCustomization.process_service_create_data(smodelctx, sdata, dev, id=id, device=dev, parentobj=parentobj, inputdict=inputdict, inputkeydict=inputkeydict, config=config, hopaque=opaque_args)

        #Start of Device binding with python bindings
        #access_lists_object = devices.device.access_lists.access_lists()
        _Gen_obj = getLocalObject(sdata, 'acl')
        inputdict['day1services_day1service_named_access_lists_acl_acl_name'] = _Gen_obj.acl.acl_name
        if util.isNotEmpty(inputdict.get('day1services_day1service_named_access_lists_acl_acl_name')):
          #access_lists_access_list_object = devices.device.access_lists.access_list.access_list()
          #access_lists_access_list_acl_rules_object = devices.device.access_lists.access_list.acl_rules.acl_rules()
          if util.isNotEmpty(inputdict.get('match_condition_name')):
            #access_lists_access_list_acl_rules_acl_rule_object = devices.device.access_lists.access_list.acl_rules.acl_rule.acl_rule()
            access_lists_access_list_acl_rules_acl_rule_object = access_lists.access_list.acl_rules.acl_rule.acl_rule()
            #access_lists_access_list_acl_rules_acl_rule_object.name = inputdict.get('match_condition_name')

            access_lists_access_list_acl_rules_acl_rule_object.name = acl_name
            access_lists_access_list_acl_rules_acl_rule_object.linenumber = inputdict.get('sequence_number')
            access_lists_access_list_acl_rules_acl_rule_object.action = inputdict.get('action')
            access_lists_access_list_acl_rules_acl_rule_object.source_condition_type = inputdict.get('source_condition_type')
            access_lists_access_list_acl_rules_acl_rule_object.source_ip = inputdict.get('source_ipv4_address')
            access_lists_access_list_acl_rules_acl_rule_object.source_mask = inputdict.get('source_ipv4_address_mask')
            #access_lists_access_list_acl_rules_acl_rule_object.dest_condition_type = inputdict.get('dest_condition_type')
            #access_lists_access_list_acl_rules_acl_rule_object.dest_ip = inputdict.get('destination_ipv4_address')
            #access_lists_access_list_acl_rules_acl_rule_object.dest_mask = inputdict.get('destination_ipv4_address_mask')
            if inputdict.get('match_packets') != "log":
                access_lists_access_list_acl_rules_acl_rule_object.match_packets = inputdict.get('match_packets')
            else:
                access_lists_access_list_acl_rules_acl_rule_object.extra_options = "log"




        #End of Device binding
        devbindobjs['access_lists_access_list_acl_rules_acl_rule_object'] = access_lists_access_list_acl_rules_acl_rule_object
        #Use the custom method to process/create payload
        service_customization.ServiceDataCustomization.process_service_device_bindings(smodelctx, sdata, dev, id=id, device=dev, inputdict=inputdict, inputkeydict=inputkeydict, parentobj=parentobj, config=config, devbindobjs=devbindobjs, hopaque=opaque_args)
        #for dev_iterator in dev:
          #yang.Sdk.createData(dev_iterator.url+'/access-lists/access-list=%s'%(util.make_interfacename(inputdict.get('day1services_day1service_named_access_lists_acl_acl_name'))),'<acl-rules/>', sdata.getSession(), True)


        access_lists_access_list_acl_rules_acl_rule_object_payload = access_lists_access_list_acl_rules_acl_rule_object.getxml(filter=True)
        #log('access_lists_access_list_acl_rules_acl_rule_object_payload: %s' % (access_lists_access_list_acl_rules_acl_rule_object_payload))
        for dev_iterator in dev:
          yang.Sdk.createData(dev_iterator.url+'/acl:access-lists/access-list=%s/acl-rules'%(util.make_interfacename(inputdict.get('day1services_day1service_named_access_lists_acl_acl_name'))),access_lists_access_list_acl_rules_acl_rule_object_payload, sdata.getSession(), True)

    def update(self, id, sdata):
        #Fetch Local Config Object
        config = getCurrentObjectConfig(id, sdata, 'match_condition')
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
        inputdict['match_condition_name'] = config.get_field_value('match_condition_name')
        inputdict['source_condition_type'] = config.get_field_value('source_condition_type')
        inputdict['source_ipv4_address'] = config.get_field_value('source_ipv4_address')
        inputdict['source_ipv4_address_mask'] = config.get_field_value('source_ipv4_address_mask')
        inputdict['dest_condition_type'] = config.get_field_value('dest_condition_type')
        inputdict['destination_ipv4_address'] = config.get_field_value('destination_ipv4_address')
        inputdict['destination_ipv4_address_mask'] = config.get_field_value('destination_ipv4_address_mask')
        inputdict['action'] = config.get_field_value('action')
        inputdict['sequence_number'] = config.get_field_value('sequence_number')
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
        config = getCurrentObjectConfig(id, sdata, 'match_condition')
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
        inputdict['match_condition_name'] = config.get_field_value('match_condition_name')
        inputdict['source_condition_type'] = config.get_field_value('source_condition_type')
        inputdict['source_ipv4_address'] = config.get_field_value('source_ipv4_address')
        inputdict['source_ipv4_address_mask'] = config.get_field_value('source_ipv4_address_mask')
        inputdict['dest_condition_type'] = config.get_field_value('dest_condition_type')
        inputdict['destination_ipv4_address'] = config.get_field_value('destination_ipv4_address')
        inputdict['destination_ipv4_address_mask'] = config.get_field_value('destination_ipv4_address_mask')
        inputdict['action'] = config.get_field_value('action')
        inputdict['sequence_number'] = config.get_field_value('sequence_number')
        # END OF FETCHING THE LEAF PARAMETERS

        _Gen_obj = getLocalObject(sdata, 'day1service')
        device_mgmt_ip_address = _Gen_obj.day1service.device_ip

        #Fetch Device Object
        dev = getDeviceObject(device_mgmt_ip_address, sdata)

        #Use the custom method to process the data
        service_customization.ServiceDataCustomization.process_service_delete_data(smodelctx, sdata, id=id, dev=dev, parentobj=parentobj, config=config, hopaque=opaque_args, inputdict=inputdict)

    @staticmethod
    def getInstance():
        if(MatchCondition._instance == None):
            MatchCondition._instance = MatchCondition()
        return MatchCondition._instance

    def rollbackCreate(self, id, sdata):
        log('rollback: id = %s, sdata = %s' % (id, sdata))
        self.delete(id,sdata)

if __name__ == 'match_condition':
  from servicemodel.yang import YangServiceData
  sdata = YangServiceData()
  instance = MatchCondition().getInstance()
  instance.create(None, sdata)
  instance.delete(None, sdata)
  instance.update(None, sdata)
