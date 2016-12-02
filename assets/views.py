#

from django.shortcuts import render
from django.http import HttpResponse
from assets import  core
import json
from django.views.decorators.csrf import csrf_exempt
from assets import models

# 这里创造视图
#csrf_exempt

def asset_with_no_asset_id(request):
    #pass
    if request.method == 'POST':
        print(request.POST.get("asset_data"))
        # ass_handler = core.Asset(request)
        # res = ass_handler.get_asset_id_by_sn()

        # return render(request,'assets/acquire_asset_id_test.html',{'response':res})
        print('------------:ok---------')
        #return HttpResponse(json.dumps(res))
        return HttpResponse('dddddd')

# def asset_report(request):
#     print(request.GET)
#     if request.method == 'POST':
#         ass_handler = core.Asset(request)
#         if ass_handler.data_is_valid():
#             print("----asset data valid:")
#             ass_handler.data_inject()
#             # return HttpResponse(json.dumps(ass_handler.response))
#
#         return HttpResponse(json.dumps(ass_handler.response))
#         # return render(request,'assets/asset_report_test.html',{'response':ass_handler.response})
#         # else:
#         # return HttpResponse(json.dumps(ass_handler.response))
#
#     return HttpResponse('--test--')