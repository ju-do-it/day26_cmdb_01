#!/usr/bin/env python
#coding:utf-8

from assets import models
import json
class Asset(object):
    def __init__(self,request):
        self.request = request
        self.mandatory_fields = ['sn','asset_id','asset_type'] #must contains 'sn' , 'asset_id' and 'asset_type'
        self.field_sets = {
            'asset':['manufactory'],
            'server':['model','cpu_count','cpu_core_count','cpu_model','raid_type','os_type','os_distribution','os_release'],
            'networkdevice':[]
        }
        self.response = {
            'error':[],
            'info':[],
            'warning':[]
        }

    def response_msg(self,msg_type,key,msg):
        if msg_type in self.response:
            self.response[msg_type].append({key:msg})
        else:
            raise ValueError

    # def data_is_valid(self):
    #     data = self.request.POST.get("asset_data")
    #     if data:
    #         try:
    #             data = json.loads(data)
    #             self.mandatory_check(data)
    #             self.clean_data = data
    #             if not self.response['error']:
    #                 return True
    #         except ValueError as e:
    #             self.response_msg('error','AssetDataInvalid', str(e))
    #     else:
    #         self.response_msg('error','AssetDataInvalid', "The reported asset data is not valid or provided")
