import csv
import sys
from PIL import Image, ImageOps


def main():
    # checks for valid command line arguments
    valid_args = check_command_line_arguments()
    if check_command_line_arguments() != "Valid":
        # prints error message then exits
        print(valid_args)
        sys.exit(1)

    # adds the shirt to the image if it exists
    program_sucess = add_shirt_to_image(sys.argv[1], sys.argv[2])

    # if the program didnt run correctly print error
    if program_sucess != 0:
        # error
        print(program_sucess)
        sys.exit(2)

    # all code executed correctly exit with 0
    sys.exit(0)


def add_shirt_to_image(input_image, output_image):
    try:
        # opens the input image and the shirt image
        with Image.open(input_image) as input, Image.open("shirt.png") as shirt:
            # gets the shirts size
            shirt_size = shirt.size
            # creates an image the same as the input image but fit to the shirt image size
            output = ImageOps.fit(input, shirt_size)
            # pastes the shirt onto the image
            output.paste(shirt, shirt)
            # saves this image as the output image
            output.save(output_image)

        return 0
    # error handling
    except FileNotFoundError:
        return "Input does not exist"


def check_command_line_arguments():
    # list of valid extensions
    valid_extension = [".jpeg", ".png", ".jpg"]
    # used to check what extension is invalid
    input_valid = False

    # checks if correct amount of cmd args
    if len(sys.argv) < 2:
        return "Too few command-line arguments"
    elif len(sys.argv) > 3:
        return "Too many command-line arguments"

    # checks if input extension is in valid list and matches output
    for i in range(len(valid_extension)):
        if sys.argv[1].endswith(valid_extension[i]):
            input_valid = True
            # checks fro a valid matching input and output
            if sys.argv[2].endswith(valid_extension[i]):
                return "Valid"
            else:
                return "Input and output have different extensions"

    # if input is valid output must not be
    if input_valid:
        return "Invalid output"
    else:  # input was not valid
        return "Invalid input"


# calls main if this file is main
if __name__ == "__main__":
    main()
