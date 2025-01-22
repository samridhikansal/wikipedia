from .models import Topics
from .form import SearchForm

def search_logic(request):
   
    if request.method == "POST":
        search_query = request.POST.get('search_query')
        heading = Topics.objects.filter(heading__icontains=search_query).values()
        desc = Topics.objects.filter(desc__icontains=search_query).values()
        final_list = (heading | desc).distinct()
        return(final_list)
    else:
        return()
