from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET']) #api operator
def getData_view(request):
    person = {'name':'mingzi','age':28}
    return Response(person)

    #dic input, output as JSON