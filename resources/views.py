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


# @api_view(['GET'])
# def download_file(request, id):

#     document = Resource.objects.get(id=id)
#     resource = document.get_file_location()
#     # print(str(resource.split('/'))
#     f1_path = resource
#     filename = resource.split('/')[1]

#     f1 = open(f1_path, 'r')
#     mimetypes, _ = mimetypes.guess_type(f1_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     return response
#     # print(resource.split('/'))
#     # return print('done')
@api_view(['GET'])
def download_from_s3(request, id):
    document = Resource.objects.get(id=id)
    resource = document.get_file_location()
    s3 = boto3.client('s3')
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    s3_file_path = resource
    print(s3_file_path)
    # s3.download_file(bucket_name, resource)
    response_headers = {
        'response-content-type': 'application/force-download',
        'response-content-disposition': 'attachment;filename="%s"' % s3_file_path
    }

    url = s3.generate_url(60, 'GET',
                          bucket=settings.AWS_STORAGE_BUCKET_NAME,
                          key=s3_file_path,
                          response_headers=response_headers,
                          force_http=True)

    return HttpResponseRedirect(url)
