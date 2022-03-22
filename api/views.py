# dependencies
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
import cv2
import numpy as np


def compare(name1, name2):
    # images to compare
    image1 = cv2.imread(name1)
    image2 = cv2.imread(name2)

    # differences
    difference = cv2.subtract(image1, image2)
    result = not np.any(difference)

    # comment out to check the differences in result.png
    # cv2.imwrite("result.png", difference)

    # if difference is all zeros it will return False
    return result


@api_view(['POST'])  # POST request receives images
def images(request):

    # receiving images with key "image1" & "image2"
    image1 = request.FILES['image1']
    image2 = request.FILES['image2']

    # saving to local to work with opencv
    default_storage.save(image1.name, image1)
    default_storage.save(image2.name, image2)

    result = compare(image1.name, image2.name)
    text = "Images are same" if result is True else "Images are different"

    # json data to send
    data = {'imageAreSame': result, 'message': text}

    # delete images from local
    default_storage.delete(image1.name)
    default_storage.delete(image2.name)

    return Response(data)
