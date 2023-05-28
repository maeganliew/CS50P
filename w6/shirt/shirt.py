import sys, shutil
from PIL import Image, ImageOps

format = ["jpg", "jpeg", "png"]

def main():
    check_arg()
    add_image()


def check_arg():
    count = 0
    #to get extensions of both files
    title2, f1 = sys.argv[1].split(".")
    title2, f2 = sys.argv[2].split(".")

    if len(sys.argv) != 3:
        sys.exit("Invalid number of arguments")
    if f1 not in format or f2 not in format:
        sys.exit("Invalid file extension")
    for f in format:
        if sys.argv[1].endswith(f):
            if not sys.argv[2].endswith(f):
                sys.exit("Two files have different extensions")
        else:
            continue


def add_image():
    #try opening the background image
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")

    shirt = Image.open("shirt.png")
    size = shirt.size
    #to make a cropped duplicate of image  (image to be cropped, size to be cropped into)
    cropped = ImageOps.fit(image, size)

    #paste, and save to a file name
    cropped.paste(shirt, shirt)
    cropped.save(sys.argv[2])


if __name__ == "__main__":
    main()