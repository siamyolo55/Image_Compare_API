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
    difference1 = cv2.subtract(image1, image2)
    difference2 = cv2.subtract(image2, image1)
    result1 = not np.any(difference1)
    result2 = not np.any(difference2)

    # --- take the absolute difference of the images ---
    abs_diff = cv2.absdiff(image1, image2)

    # --- find percentage difference based on number of pixels that are not zero ---
    percentage = (np.count_nonzero(abs_diff) * 100) / abs_diff.size

    # images are same only when both results return True
    if result1 is True & result2 is True:
        return True, 0
    elif result1 is True and result2 is False:
        cv2.imwrite('result2.jpg', difference2)
        print("The difference is: ", percentage, "%")
        return False, percentage
    elif result1 is False and result2 is True:
        cv2.imwrite('result1.jpg', difference1)
        print("The difference is: ", percentage, "%")
        return False, percentage
    else:
        print(cv2.imwrite("result.jpg", difference1))
        print("images are different from both sides")
        print("The difference in First 'Pixel Track' is: ", percentage, "%")
        return False, percentage


@api_view(['POST'])  # POST request receives images
def images(request):

    # receiving images with key "image1" & "image2"
    image1 = request.FILES['image1']
    image2 = request.FILES['image2']

    # saving to local to work with opencv
    default_storage.save(image1.name, image1)
    default_storage.save(image2.name, image2)

    result, percentage = compare(image1.name, image2.name)
    text = "Images are same" if result is True else "Images are different"

    # json data to send
    data = {'imageAreSame': result, 'difference_percentage': percentage}

    # delete images from local
    default_storage.delete(image1.name)
    default_storage.delete(image2.name)

    return Response(data)
