import boto3
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import request, response
from django.http import HttpResponseRedirect
from .models import Resource
from .serializers import ResourceSerializer


class ResourceViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


@api_view(['GET'])
def download_from_s3(request, id):
    document = Resource.objects.get(id=id)
    key = document.get_file_location()
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    object_name = key.split('/')[0]
    file_name = key.split('/')[1]
    s3_file_path = f"media/{key}"

    response_headers = {
        'response-content-type': 'application/force-download',
        'response-content-disposition': 'attachment;filename="%s"' % s3_file_path
    }

    s3_client = boto3.client('s3', region_name="us-west-2")
    url = s3_client.generate_presigned_url('get_object',
                                           Params={'Bucket': bucket_name, 'Key': s3_file_path, 'ResponseContentDisposition': 'attachment'}, ExpiresIn=3600)

    return HttpResponseRedirect(url)
