from blog.models import Post

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def q_search(query):

    # Поиск по id
    if query.isdigit() and len(query) <= 5:
        return Post.objects.filter(id=int(query))
    
    vector = SearchVector("title", "content")
    query = SearchQuery(query)

    for x in Post.published.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank"):
        print(x, x.rank)

    return Post.published.annotate(rank=SearchRank(vector, query)).filter(rank__gt=1e-20).order_by("-rank")
