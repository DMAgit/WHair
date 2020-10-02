import easyocr
from ingredient_import import ingredient_import
from PIL import Image, ImageDraw
from pandas.core.common import flatten

"""
test = [30, 60, 450, 750]
with Image.open("conditioner.jpg") as img:
    draw = ImageDraw.Draw(img)
    for coord in test:
        draw.rectangle(test, outline="Crimson", fill=None, width=4)  # draw a rectangle

img.show()
"""


def downscale(image, scale=4):
    """
    downscaler
    made it myself, probably not optimal
    :param image: name of file(string), numpy array, byte
    :param scale: multiple to downscale the image from
    :return: resized image
    """

    size_small = []
    for i in image.size:
        size_small.append(int(i / scale))
    return image.resize(size_small)


def give_corners(text_result):
    """
    give the corners of all of the bounding boxes
    :param text_result: output of reader.readtext as list
    :return: coordinates of 4 outer most coordinates of each of the reader.readtext bounding boxes in the output
    """

    for i in text_result:  # find corners of bounding boxes
        coord_list = [i[0]]
        coord_list = list(flatten(coord_list))

    return list(dict.fromkeys(coord_list))


def draw_boxes(image, outer_points, color):
    """

    :param image: image onto which to draw bounding boxes
    :param outer_points: output of give_corners, nested list of 4 outer most coordinates of every bounding box
    :param color: color with which to outline boxes
    :return: image with bounding boxes

    """

    draw = ImageDraw.Draw(image)
    for coord in outer_points:
        draw.rectangle(outer_points, outline=color, fill=None, width=4)

    return image


# ingredients = ingredient_import("C:/Users/DMA/PycharmProjects/pythonProject1", "ingredients.csv")
# print(ingredients.to_string())

photo = Image.open(image)
print("original size:" + str(photo.size))
photo = downscale(photo)
print("rescaled size:" + str(photo.size))

# print(cuda.is_available())
# cuda.empty_cache()

reader = easyocr.Reader(["en"])  # need to run only once to load model into memory
result = reader.readtext(photo, detail=1)

corners = give_corners(result)
bounding_boxes_img = draw_boxes(photo, give_corners(result), "CrimsonRed")
bounding_boxes_img.show()
