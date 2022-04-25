from PIL import Image


def decipher(image_path):
    #  decipher the hidden message inside the image
    black_pixels = []
    coded_message = ""
    threshold = 127  # lower than this is black
    image = Image.open(image_path)
    pixel_matrix = image.load()
    width, height = image.size
    for col in range(width):
        for row in range(height):
            if pixel_matrix[col, row] < threshold:
                black_pixels.append(row)

    for index_row in black_pixels:
        coded_message += chr(index_row)
    return coded_message
