import json
import os

from django.http import FileResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from sx import settings


class CommonViewSet(viewsets.GenericViewSet):

    @action(methods=['get'],detail=False)
    def download(self,request):

        fileName = request.query_params.get('fileName')
        print(fileName)

        file = open(os.path.join(settings.MEDIA_FILE,fileName), 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=%s' % fileName.encode('utf8').decode('ISO-8859-1')
        return response


