from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.

def personal_of_day(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'all-personal/recent-personal.html', {"date": date, "images":images})

#view Function to recent personal pictures old past days
def past_days_personal(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(personal_of_day)
        return render(request, 'all-personal/old-personal.html', {"date": date,})
    
    # search function
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Image.search_by_description(search_term)
        message = f"{search_term}"

        return render(request, 'all-personal/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any image"
        return render(request, 'all-personal/search.html',{"message":message})
