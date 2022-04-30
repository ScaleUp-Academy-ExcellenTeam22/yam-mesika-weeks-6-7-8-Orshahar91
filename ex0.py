from PIL import Image


def decipher(image):
    """
    Decipher the hidden message inside the image.
    :param image: The path for the image file.
    :return: The coded message as string.
    """
    coded_message = ""
    threshold = 127  # lower than this is black
    pixel_matrix = image.load()
    width, height = image.size
    black_pixels = [(col, row) for col in range(width) for row in range(height) if pixel_matrix[col, row] < threshold]
    coded_message = [coded_message + chr(index[1]) for index in black_pixels]
    coded_message = ''.join(coded_message)
    return coded_message


"""Driver code to test the function above."""
img_to_decipher = Image.open("code.png")
print(decipher(img_to_decipher))
