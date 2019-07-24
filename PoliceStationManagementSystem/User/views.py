from msilib.schema import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q
from django.shortcuts import render

# Create your views here.nment
from User.models import CrimeRecord


@login_required()
def crimes(request):
    if request.GET.get('q'):
        query = request.GET.get('q')
        se_result = CrimeRecord.objects.filter(Q(CriminalID__icontains=query))
        current_site = get_current_site(request)
        context = dict()
        context['s_result'] = se_result

        travel_obj = CrimeRecord.objects.get(id=query)

        travel_obj.EyeColor = query
        travel_obj.save()

        context['domain'] = current_site
        return render(request, 'ViewRecords.html', context)

    else:
        qs = CrimeRecord.objects.all()

        current_site = get_current_site(request)
        context = dict()
        context['s_result'] = qs
        context['domain'] = current_site
        return render(request, 'ViewRecords.html', context)








