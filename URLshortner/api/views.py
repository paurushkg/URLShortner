import random
from rest_framework.views import APIView
from rest_framework.response import Response
from shortner.models import Url
from api.serializers import PostUrlSerializer, UrlSerializer

CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


class UrlShortner(APIView):

    def post(self, request):
        serializer = PostUrlSerializer(data=request.data)

        if serializer.is_valid():
            link = serializer.data['link']
            short_link = ""

            urls = Url.objects.all()

            for url in urls:
                if url.link == link:
                    short_link = url.short_link
                    break

            else:
                for i in range(1, 7):
                    letters = random.randint(1, len(CHARACTERS) - 1)
                    let = CHARACTERS[letters]
                    short_link += let

                url = Url(link=link, short_link=short_link)
                url.save()

            link_data = Url.objects.get(link=link)
            link_data_serializer = UrlSerializer(link_data)
            return Response(link_data_serializer.data)




