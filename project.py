# needed libraries
import cv2
import numpy as np
import re
import sys


# main
def main():
    # checks if the user provides all setup info when starting program
    input_data = shortcut_setup(sys.argv)

    # if the user didnt provide all input at the command line get required inputs from user
    if input_data == False:
        input_data = user_setup()

    # checks if the input file is a video
    if input_data[3] == "-v":
        # creates a pixelated video from the input video
        create_pixelated_video(input_data)

    else:
        # returns the name of the pixelated image and the image
        output_values = return_pixelated_image(
            input_data[0], input_data[1], input_data[2]
        )

        # exits on function failure
        if output_values == False:
            sys.exit(2)

        # saves/writes the pixelated image to output folder
        cv2.imwrite(f"Output/{output_values[0]}", output_values[1])


# loops a video pixelating its frames
def create_pixelated_video(data):

    # checks if input files are valid
    if valid_input_extension(data[0]) and valid_input_extension(data[1]):
        # stores the video file
        cap = cv2.VideoCapture(f"Input/{data[0]}")

        # get video cap frame sizes
        width = cap.get(3)
        height = cap.get(4)

        # uses width and height to create framesize
        # frame_size = [int(height), int(width)]

        # default frame size
        frame_size = [1920, 1080]
        # sets the framerate of the video
        framerate = data[4]

        # video writer
        video = cv2.VideoWriter(
            f"Output/{data[1]}",
            cv2.VideoWriter_fourcc(*"DIVX"),
            framerate,
            frame_size,
        )

        # keeps track of frame count
        frame_count = 0

        # checks if the video cant open
        if not cap.isOpened():
            # the input video was unreadable
            print("Invalid input file")
            sys.exit(2)
        # the video can be opened
        else:
            # for each frame in the video
            while cap.isOpened():

                # Capture frame-by-frame
                ret, frame = cap.read()

                # if frame is read correctly ret is True
                if not ret:
                    break

                # pixelates the frame
                frame = pixelate_image(frame, f"{frame_count}.jpeg", data[2])[1]
                # resizes frame to output size
                frame = cv2.resize(frame, frame_size)

                # writes the frame to the ouput video
                video.write(frame)

            # releases the video capture
            cap.release()
            # releases the video
            video.release
    else:
        # prints error message
        print("Invalid File extension")
        sys.exit(3)


# allows user to provide all inputs at the command line
def shortcut_setup(setup_data):
    # user has provided appropriate command line arg
    if len(setup_data) >= 4 and len(setup_data) <= 5:
        # checks if command line args are valid
        if (
            isinstance(setup_data[1], str)
            and setup_data[1].lower() in ["-v", "-i"]
            and valid_input_extension(setup_data[2])
        ):

            if len(setup_data) == 5 and valid_input_extension(setup_data[3]):
                if len(setup_data) >= 1 and len(setup_data) <= 100:

                    # input file, output file, pixelation value, file type, framerate
                    return [
                        setup_data[2],
                        setup_data[3],
                        int(setup_data[4]),
                        setup_data[1],
                        20.0,
                    ]
                else:
                    return False

            elif len(setup_data) == 4:
                if len(setup_data) >= 1 and len(setup_data) <= 100:

                    # input file, output file, pixelation value, file type, framerate
                    return [
                        setup_data[2],
                        setup_data[2],
                        int(setup_data[3]),
                        setup_data[1],
                        20.0,
                    ]
                else:
                    return False

            # args are invalid
            return False
        else:
            # invalid args user input required
            print("Invalid command line arguments\nManual input required")
            return False
    else:  # user did not provide command line shortcut
        return False


# sets up the program to users preference
def user_setup():

    # does the user want to use default settings or use custom settings
    while True:
        # gets input from user
        default_settings = input("Would you like to use the default settings? (y/n) ")

        # user wants default settings
        if default_settings.lower().strip() in ["y", "yes", "1"]:
            default_settings = True
            break
        # user wants custom settings
        elif default_settings.lower().strip() in ["n", "no", "0"]:
            default_settings = False
            break

    # is the input a video
    while True:
        # gets input from user
        file_type = input("Are you pixelating a video or an image? ")

        # input file is an image
        if file_type.lower().strip() in ["image", "i"]:
            file_type = "-i"
            break
        # input file is a video
        elif file_type.lower().strip() in ["video", "v"]:
            file_type = "-v"
            break

    # gets input file from user
    input_file = input("Input file: ")

    # default framerate
    framerate = 20.0

    # applies custom settings
    if default_settings == False:
        # output file
        output_file = input("Output file: ")
        # loop breaks on acceptable input
        while True:
            # lets user choose framerate
            if file_type == "v":
                framerate = float(input("Video framerate"))

            # makes sure values are non negative
            try:
                pixelation_value = int(pixelation_value)
                if (
                    pixelation_value >= 1
                    and pixelation_value <= 100
                    and framerate >= 1
                    and framerate <= 100
                ):
                    break
            except ValueError:
                pass
    else:
        # default settings
        output_file = input_file

    while True:
        pixelation_value = int(input("Pixelation Value: 1 - 100 recommended 15: "))

        if int(pixelation_value) > 1 and int(pixelation_value) < 100:
            break

    # returns values
    if file_type == "-i":
        # returns the values in a list
        return [input_file, output_file, int(pixelation_value), file_type]
    elif file_type == "-v":
        return [input_file, output_file, int(pixelation_value), file_type, framerate]


def return_pixelated_image(input_image, output_image, pixelation_value):
    # checks if the inputs have valid image extensions
    if valid_input_extension(input_image) and valid_input_extension(output_image):
        # tries to pixelate image
        try:
            # reads the input image
            input_img = cv2.imread(f"Input/{input_image}")
            # call pixelation function on image
            return pixelate_image(input_img, f"{output_image}", pixelation_value)
        except ValueError:
            # the input image was unreadable
            print("Invalid input file")
            return False
    else:
        # prints error message
        print("Invalid File extension")
        return False


# checks if the file has a valid extension
def valid_input_extension(image_name):
    return re.search(r"^\w*\.(jpeg|jpg|png|tiff|avi|mp4)", image_name.strip().lower())


# uses cv2 to resize an image down and up again to pixelate the image
def pixelate_image(input_img, output="output.png", size_value=10):
    # Error handling
    try:
        # the size of the pixel
        pixel_size = size_value

        # stores the height and width of the image
        original_height, original_width = input_img.shape[
            :2
        ]  # returns only width and height from shape tupple

        # the width and height of the return image
        new_width = (
            original_width // pixel_size
        )  # uses floor division so the pixels are ints not floats
        new_height = original_height // pixel_size

        # creates a temp image that is a resized version of the input image
        resized_image = cv2.resize(
            input_img, (new_width, new_height), interpolation=cv2.INTER_LINEAR
        )

        # resizes the new image to the original images size
        output_img = cv2.resize(
            resized_image,
            (original_width, original_height),
            interpolation=cv2.INTER_NEAREST,
        )

        # returns the image
        return [output, output_img]
    except AttributeError:
        # used to raise error for outer try blocks
        raise ValueError


# calls main
if __name__ == "__main__":
    main()
