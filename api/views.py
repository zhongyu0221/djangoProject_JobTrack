from rest_framework.response import Response
from rest_framework.decorators import api_view

# from .serializers import Itemserializer
# from learnDRF.models import Item
#
# @api_view(['GET'])
#  #api operator
#
# def getData_view(request):
#     item = Item.objects.all()
#     serializer = Itemserializer(items,many=True)
#
#
#     return Response(serializer.data)
#
#     #dic input, output as JSON