import cv2 as opencv


class ImageHandler:
    """
    A class for processing images using OpenCV.
    """

    #

    def __init__(self):
        """
        Initialize an ImageHandler instance.
        """
        pass

    #

    def __str__(self):
        """
        Return a human-readable string representation of the ImageHandler instance.
        """
        return f"{self}[]"

    # ---
    # Methods that show image-files and opencv-images as a window
    # ---
    def show_opencv(self, opencv_image, window_title: str = "image"):
        """
        Display an OpenCV image in a window.

        :param opencv_image: The OpenCV image to be displayed.
        :param window_title: Title of the display window (default is "image").
        """
        opencv.imshow(window_title, opencv_image)

    #

    def show_file(self, filepath: str, window_title: str = "image"):
        """
        Read an image file and display it in a window.

        :param filepath: Path to the image file.
        :param window_title: Title of the display window (default is "image").
        """
        opencv_image = opencv.imread(filepath, flags=opencv.IMREAD_COLOR_RGB)
        self.show_opencv(opencv_image, window_title)

    #

    # ---
    # Methods that encode files and opencv-images to bytes
    # ---
    def encode_bytes_opencv(self, opencv_image, extension: str):
        """
        Encode an OpenCV image into byte data.

        :param opencv_image: The OpenCV image to be encoded.
        :param extension: File extension (e.g., ".jpg", ".png").
        :return: The encoded byte data of the image.
        :raises Exception: If the image cannot be encoded.
        """
        success, image_encoded = opencv.imencode(extension, opencv_image)
        if success:
            image_bytes = image_encoded.tobytes()
            return image_bytes
        else:
            raise Exception("Image couln't be encoded!")

    #

    def encode_bytes_file(self, filepath: str, extension: str):
        """
        Read an image file and encode it into byte data.

        :param filepath: Path to the image file.
        :param extension: File extension (e.g., ".jpg", ".png").
        :return: The encoded byte data of the image.
        """
        opencv_image = opencv.imread(filepath, flags=opencv.IMREAD_COLOR_RGB)
        return self.encode_bytes_opencv(opencv_image, extension)

    # ---
    # Methods that decode bytes to files and opencv-images
    # ---
    def decode(self):
        pass
