from django.shortcuts import render
from .forms import BlockForm
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext
import subprocess



def homepage(request):

    form = BlockForm(request.POST or None)

    #main information
    wifi_info = get_info('ls')
    stats_info = get_info('pihole', '-c')
    dev_info = get_info('ps')



    templ = {"form" : form, "wifi_info" : wifi_info,
            "stats_info" : stats_info, "dev_info" : dev_info}

    return render(request,"index.html", templ)

def block_addv(request):
    if request.POST:

        ip = request.POST['ip']
        mask = request.POST['mask']

        return HttpResponse(ip,mask)

    return render_to_response('menu', RequestContext(request))

def get_info(command,key=None):
    
    try:
        if key:
            command = [command, key]

        result = subprocess.run(command, stdout=subprocess.PIPE)
        result = result.stdout

    except (Exception) as err:

        print(err)
        result = ''

    return result

def wificonf(request):
    return render(request,"wificonf.html")

def stats(request):
    return render(request,"stats.html")

def wblist(request):
    return render(request,"wblist.html")

def dev(request):
    return render(request,"dev.html")