import requests
from load.models import Loadinfo
from datetime import  date,datetime
from  django.http import HttpResponse


def load_page(request):
    #TODO
    # 2.nick 传过来的数据有重复的，因为插入时做了判重。不影响功能使用。


    #重新设定url参数
    today = str(date.today())
    print(type(today))

    # res = requests.get("http://cmdb.server.com/loadAPI/load_info/?load_date=2019-05-17")
    res = requests.get("http://cmdb.server.com/loadAPI/load_info/?load_date=" + today +"&load_info=-1&page_size=500000" )

    # print(help(res))

    if res.status_code == 200:
        load_info = res.json()

    load_list = load_info['data']
    print(len(load_list))
    i = 0
    for load_data in load_list:
        #返回数据中有一级目录为空的场景，增加一个判断。
        if load_list[i]['tree_info']:
            aa = load_list[i]['tree_info'][0]['tree_id'].split("-")[0]
            bb = load_list[i]['tree_info'][0]['tree_name'].split("-")[0]
        else:
            aa = '0'
            bb = '其他'

        if Loadinfo.objects.filter( ip = load_list[i]['ip'] ).filter(load_date=today):
            i = i + 1
            continue

        b = Loadinfo(
            ip = load_list[i]['ip'],
            business_id = aa,
            business_name = bb,
            load = load_list[i]['load_info_text'],
            load_date = today,
            create_time = datetime.now(),
            )

        i = i + 1
        b.save()
    return HttpResponse("refresh success! \n  refresh time is"  + str(datetime.now()))
    # print(load_info)
    # print(load_list)