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
#ALL THE CUSTOMIZATIONS REGARDING DATAPROCESSING SHOULD BE WRITTEN INTO THIS FILE
#
"""
Tree Structure of Handled XPATH:

services
        |
        day1services
                    |
                    day1service
                               
Schema Representation:

/services/day1services/day1service
"""
"""
Names of Leafs for this Yang Entity
                name
           device-ip
                 vrf
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
      modify = True
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']
        inputkeydict = kwargs['inputkeydict']

        import time
        now = time.strftime("%Y-%b-%d %I:%M %p %Z", time.localtime())

        payload_time = '<created-on>' + now + '</created-on>'
        yang.Sdk.createData(sdata.getRcPath(), payload_time, sdata.getSession(), False)

        taskid = sdata.getTaskId()

        output = yang.Sdk.invokeRpc('tasks:get-basic-task-detail', '<taskId>' + str(taskid) + '</taskId>')
        basic_task_details_out = util.parseXmlString(output)
        if hasattr(basic_task_details_out, 'taskDetail'):
            if hasattr(basic_task_details_out.taskDetail, 'userName'):
              taskuser = basic_task_details_out.taskDetail.userName

              payload_user = '<created-by>' + str(taskuser) + '</created-by>'
              yang.Sdk.createData(sdata.getRcPath(), payload_user, sdata.getSession(), False)

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


    @staticmethod
    def process_service_update_data(smodelctx, sdata, **kwargs):
      """callback called for update operation"""
      #raise Exception('Update forbidden  for node day1service at path day1services/day1service')
      modify = False
      if modify and kwargs is not None:
        for key, value in kwargs.iteritems():
          log("%s == %s" %(key,value))

      if modify:
        config = kwargs['config']
        inputdict = kwargs['inputdict']

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


class DeletePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for Deletion"""
        log('operations: %s' % (operations))
        yang.moveOperations(operations, ['DELETEVTYConfig'], ['DeleteAclRule'], False)
        print 'pass01: operations: %s' % (operations)
        #yang.moveOperations(operations, ['DeleteNETFLOWFlowMonitorInterface', 'DeleteNETFLOWFlowMonitor'], ['DeleteRecordIpv4options', 'DeleteRecordTimeStampsoptions', 'DeleteRecordCounteroptions'], False)
        #print 'pass03: operations: %s' % (operations)
        #yang.moveOperations(operations, ['DeleteNETFLOWFlowMonitorExporter', 'DeleteNETFLOWOption', 'DeleteRecordCounteroptions', 'DeleteNETFLOWFlowMonitorCachetimeout'], ['DeleteNETFLOWFlowExport', 'DeleteNETFLOWFlowRecord', 'DeleteNETFLOWFlowMonitor'], False)
        #print 'pass04: operations: %s' % (operations)
        #yang.moveOperations(operations, ['DeleteNETFLOWFlowExport', 'DeleteNETFLOWFlowRecord'], ['DeleteNETFLOWFlowMonitorInterface', 'DeleteNETFLOWFlowMonitor'], True)
        #print 'pass05: operations: %s' % (operations)
        

class CreatePreProcessor(yang.SessionPreProcessor):
    def processBeforeReserve(self, session):
        operations = session.getOperations()
        """Add any move operations for creation"""
        log('operations: %s' % (operations))
        #yang.moveOperations(operations, ['CreateNETFLOWFlowMonitor'], ['CreateNETFLOWFlowExport','CreateNETFLOWFlowRecord', 'CreateRecordIpv4options', 'CreateRecordTimeStampoptions', 'CreateRecordCounteroptions'], True)
        #print 'pass01: operations: %s' % (operations)
        #yang.moveOperations(operations, ['CreateNETFLOWFlowMonitorExporter','CreateNETFLOWFlowMonitorInterface'], ['CreateNETFLOWFlowMonitor'], True)
        #print 'pass02: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateAccessList', 'CreateAclRule'], ['CreateSnmpCommunity', 'UpdateVTYConfig', 'CreateVTYConfig'], False)
        print 'pass03: operations: %s' % (operations)
        yang.moveOperations(operations, ['CreateAAA'], ['DeleteRoute'], False)
        print 'pass04: operations: %s' % (operations)
