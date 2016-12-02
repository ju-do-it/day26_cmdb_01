#!/usr/bin/env python
#coding:utf-8

from assets import views
from django.conf.urls import url,include
urlpatterns = [

    # url(r'report/$', views.asset_report, name='asset_report'),
    url(r'report/asset_with_no_asset_id/$', views.asset_with_no_asset_id, name='acquire_asset_id'),
    # url(r'new_assets/approval/$', views.new_assets_approval, name="new_assets_approval"),

]