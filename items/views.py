from django.shortcuts import render
from rest_framework.generics import ListAPIView,UpdateAPIView
from items.serializers import ItemSerializer,ItemUpdateSerializer
from items.models import Item

class ItemListAPIView(ListAPIView):
    '''
        Method: GET
        URL: http://127.0.0.1:8000/items
        Response:   HTTP 200 OK
                    Allow: GET, HEAD, OPTIONS
                    Content-Type: application/json
                    Vary: Accept

                    [
                        {
                            "name": "Orange",
                            "category": "Food",
                            "subcategory": "Fruit",
                            "amount": 130
                        },
                        {
                            "name": "Limca",
                            "category": "Food",
                            "subcategory": "Beverage",
                            "amount": 95
                        },
                        {
                            "name": "Potato",
                            "category": "Food",
                            "subcategory": "Vegetable",
                            "amount": 80
                        }
                    ]
    '''
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        """
        This view should return a list of all objects by
        the filter(name,category,subcategory) passed in the URL
        """
        queryset = Item.objects.all()
        print('self.request.query_params',self.request.query_params)
        if 'name' in self.request.query_params:
            name = self.request.query_params.get('name', None)
            if name is not None:
                queryset = queryset.filter(name=name)
        if 'category' in self.request.query_params:
            category = self.request.query_params.get('category', None)
            if category is not None:
                queryset = queryset.filter(category__name=category)
        if 'subcategory' in self.request.query_params:
            subcategory = self.request.query_params.get('subcategory', None)
            if subcategory is not None:
                queryset = queryset.filter(subcategory__name=subcategory)
        return queryset


class ItemUpdateAPIView(UpdateAPIView):
    '''
        Method: GET
        URL: http://127.0.0.1:8000/items/update/1/
        Request Parameter: {
                                "name": "Orange",
                                "category": 1,
                                "subcategory": 1,
                                "amount": 130
                            }
        Response:               HTTP 200 OK
                                Allow: PUT, PATCH, OPTIONS
                                Content-Type: application/json
                                Vary: Accept
                                {
                                    "name": "Orange",
                                    "category": 1,
                                    "subcategory": 1,
                                    "amount": 130
                                }
    '''
    queryset = Item.objects.all()
    serializer_class = ItemUpdateSerializer





def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})

