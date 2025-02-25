from WORK.Image_Handler import ImageHandler


def main() -> None:
    """Main Process of the application used on app start."""
    imghandler: ImageHandler = ImageHandler()
    image_bytes = imghandler.encode_bytes_file(
        "src\FLASK\static\images\Comrade_Doge.png", ".png"
    )
    print(image_bytes)


if __name__ == "__main__":
    main()
