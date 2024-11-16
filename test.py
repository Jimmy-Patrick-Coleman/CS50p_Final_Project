from project import shortcut_setup, valid_input_extension, return_pixelated_image
import sys
import os.path


# python3 project.py -v test.avi test.avi 15


# tests that shortcut setup works
def test_shortcut_setup():

    # user has provided inappropriate command line arg
    assert shortcut_setup([]) == False
    assert shortcut_setup([1, 1, 1, 1, 1, 1, 1, 1]) == False

    # non input format
    assert (
        shortcut_setup(
            ["python3", "project.py", "-nonInputFormat", "test.avi", "test.avi", "15"]
        )
        == False
    )
    # input format is number
    assert (
        shortcut_setup(["python3", "project.py", 12, "test.avi", "test.avi", "15"])
        == False
    )

    # tests if function can run successfully
    if os.path.exists("/Input/test.avi"):
        if valid_input_extension("test.avi"):
            assert shortcut_setup(
                ["project.py", "-v", "test.avi", "test.avi", "15"]
            ) == ["test.avi", "test.avi", 15, "-v", 20.0]


# tests to see if file extensions work as intended
def test_valid_input_extension():
    # invalid extensions donet  return match
    assert valid_input_extension("invalid.txt") == None
    assert valid_input_extension("invalid.html") == None

    # valid extensions return match
    assert valid_input_extension("test.mp4") != None
    assert valid_input_extension("test.avi") != None
    assert valid_input_extension("test.png") != None
    assert valid_input_extension("test.jpeg") != None


def test_return_pixelated_image():
    # tests if function can run successfully
    if os.path.exists("/Input/test.png"):
        if valid_input_extension("test.png"):
            assert return_pixelated_image("test.png", "test.png", 10) != False

    # invalid inputs are caught
    assert return_pixelated_image("bob.bob", "bob.bob", 10) == False

    # non existant file is caught
    if not os.path.exists("/Input/idontexist.png"):
        if valid_input_extension("idontexist.png"):
            assert (
                return_pixelated_image("idontexist.png", "idontexist.png", 10) == False
            )
