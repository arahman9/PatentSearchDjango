from django.shortcuts import render
from .models import Patenttable
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank


def index(request):
    q = request.GET.get('q')

    if q:
        vector = SearchVector('patent_text')
        query = SearchQuery(q)
        patents = Patenttable.objects.annotate(rank=SearchRank(vector,query)).filter(rank__gte=0.03).order_by("-rank")
    else:
        patents = None
    c = {'patents': patents}
    return render(request,'home/index.html', c)
