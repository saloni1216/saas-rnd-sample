
import pathlib

from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


this_dir = pathlib.Path(__file__).parent
def home_page_view(request, *args, **kwargs):
    page_title = "HomePage-Saas"
    total_visits = PageVisit.objects.all()
    page_visits = PageVisit.objects.filter(path=request.path)
    context_page ={
        "page_title": page_title,
        "total_page_visits": total_visits.count(),
        "percentage": (page_visits.count() *100.0) / total_visits.count(),
        "page_visits_count" : page_visits.count()

    }

    html_ = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_, context_page)




def old_home_page_view(request, *args, **kwargs):
    page_title = "Home Page Title"
    context_page ={
        "page_title": page_title,
        
    }
    html_ = f"""
    <!DOCTYPE html>
<html>
    <body>
        <h1>Hey, Welcome to the {page_title}</h1>   
    </body>
</html>
""".format(**context_page)
    # html_ = ""
    # html_file_path = this_dir / "home.html"
    # html_= html_file_path.read_text()
    return HttpResponse(html_)