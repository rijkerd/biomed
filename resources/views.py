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
def view_from_s3(id):
    document = Resource.objects.get(id=id)
    key = document.get_file_location()
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    s3_file_path = f"media/public/{key}"

    s3_client = boto3.client('s3', region_name=settings.AWS_REGION)

    url = s3_client.generate_presigned_url('get_object',
                                           Params={'Bucket': bucket_name, 'Key': s3_file_path}, ExpiresIn=3600)

    return HttpResponseRedirect(url)


@api_view(['GET'])
def download_from_s3(id):
    document = Resource.objects.get(id=id)
    key = document.get_file_location()
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    s3_file_path = f"media/public/{key}"

    s3_client = boto3.client('s3', region_name="us-west-2")
    url = s3_client.generate_presigned_url('get_object',
                                           Params={'Bucket': bucket_name, 'Key': s3_file_path, 'ResponseContentDisposition': 'attachment'}, ExpiresIn=3600)

    return HttpResponseRedirect(url)
