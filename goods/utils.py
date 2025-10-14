from goods.models import Products
from django.db.models import Q

    
def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))