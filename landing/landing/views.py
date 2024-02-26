from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import *


def index(request):
    # try:
    setting_list = SeoHeader.objects.get(id=1)
    nav_list = MenuNavHeader.objects.all()
    consultation = HowToDoIt.objects.get(id=1)
    services = Services.objects.get(id=1)
    expert_list = Experts.objects.all()
    videos_block_parameters = ParametersVideosBlock.objects.get(id=3)
    list_videos = ListVideos.objects.all()

    # except:
    #     raise Http404('УПППППСССССС !!!!! Страница пропала !!! Иду на поиски... ')

    context = {
        'setting_list': setting_list,
        'nav_list': nav_list,
        'consultation': consultation,
        'services': services,
        'expert_list': expert_list,
        'videos_block_parameters': videos_block_parameters,
        'list_videos': list_videos,
    }
    return render(request, 'landing/index.html', context)
