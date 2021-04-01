"""
IoU (Intersection over Union, 交并比)

IoU is a metric to measure the overlap between two bounding boxes or masks.
It's commonly used to evaluate Object Detection or Image Segmentation models.

The ideal situation will be totally overlapping, and the IoU value will be 1, 
and the worst case will be 0, meaning there is no overlapping between candidate 
bounding box and ground truth bounding box.

Reference: https://blog.csdn.net/guyuealian/article/details/86488008
"""

def calculate_iou(box1, box2):
    """
    :param box1: = [xmin1, ymin1, xmax1, ymax1]
    :param box2: = [xmin2, ymin2, xmax2, ymax2]
    """
    xmin1, ymin1, xmax1, ymax1 = box1
    xmin2, ymin2, xmax2, ymax2 = box2

    # Calculate the two rectangles's area.
    area_1 = (xmax1 - xmin1)*(ymax1 - ymin1)
    area_2 = (xmax2 - xmin2)*(ymax2 - ymin2)

    # Calculate the overlapping rectangle indices.
    xmin = max(xmin1, xmin2)
    ymin = max(ymin1, ymin2)
    xmax = min(xmax1, xmax2)
    ymax = min(ymax1, ymax2)

    # For boxes that are not overlapping, such as 
    # [1, 1, 3, 3] and [5, 5, 8, 8], we shall output 0.
    w = max(0, xmax - xmin)
    h = max(0, ymax - ymin)

    # Calculate the overlapping area and the IoU.
    area = w * h
    iou = area / (area_1 + area_2 - area)

    return "{:.2f}%".format(iou * 100)

if __name__ == "__main__":
    box1 = [1, 1, 10, 10]
    box2 = [5, 5, 12, 12]
    # (5*5) / (9*9 + 7*7 - 5*5) = 0.238
    print(calculate_iou(box1, box2))

    box1 = [3, 3, 10, 10]
    box2 = [1, 1, 5, 5]
    # (2*2) / (7*7 + 4*4 - 2*2) = 0.656
    print(calculate_iou(box1, box2))

    box1 = [1, 1, 3, 3]
    box2 = [5, 5, 8, 8]
    # Not overlapping, 0
    print(calculate_iou(box1, box2))