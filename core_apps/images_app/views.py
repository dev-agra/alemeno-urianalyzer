from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer
from django.http import JsonResponse
import cv2
import os


def HomepageRender(request):
    return render(request, 'images_app/example.html')


class ImageProcessSet(APIView):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES['file']
        media_root = settings.MEDIA_ROOT
        file_path = os.path.join(media_root, 'images', image_file.name)
        img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

        img = cv2.imread('strip_images/image1.jpg', cv2.IMREAD_UNCHANGED)

        height, width, channel = img.shape
        cx = int(width / 2 + 30)
        cy = int(height / 2 + 40)

        response = {}
        strip_para = ['leukocytes', 'nitrite', 'urobilinogen', 'protein',
                      'pH', 'Haemoglobin', 'specific_gravity',
                      'ketone', 'bilirubin', 'glucose']
        for i in range(10):
            pixel_center = img[cy, cx]
            r, g, b = int(pixel_center[0]), int(pixel_center[1]), int(pixel_center[2])
            response.update({f'{strip_para[i]}': [r, g, b]})
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), 3)
            cy -= 73

        cv2.destroyAllWindows()
        response_data = {
            'message': 'File processed successfully',
            'status': 'success',
            'response': response
        }
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
