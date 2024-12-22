# CS50p_Final_Project 

CS50p Final Project 

#### Video Demo Url https://youtu.be/Lg_6NeaPxo0

## Description 

This is my cs50p Final Project. It is a python program that pixelates images and videos input by the user.  

### Why I chose this as my project 

I chose to make this as my final project as I had been experimenting with pixelating images when creating my gd50 project sprites. Having a retro low-quality pixelated design meant I could hide my terrible art skills.  

I was using blender composites to render pixelated images that I was painting on a flat plane with texture paint. Creating a program that would pixelate the images or even videos would save me a lot of time. Additionally, I wanted to learn more about the process so this project seemed perfect 

## What each of the files do 

### project.py 

This is the main Project file. It contains all the code relating to pixelating the user's image/video. The notable functions in this file are: 

#### shortcut_setup: 
This function allows the user to execute the program entirely in 1 line at the command line.  This can be done with the command: $ python3 project.py -(format specifier i or v) (file name eg file.png) (pixelation value). 

#### create_pixelated_video: 
This function is what creates a pixelated video. It uses opencv cv2 to open up the input video file. Reads each line of the file and writes a pixelated copy of each frame into an output file. The output videos are encoded with DIVX. The pixelation of frames is achieved via the pixelate_image function. 

#### user_setup:
This function is called when the user doesn't provide the shortcut setup command line arguments. It gets the needed inputs from the user such as the file type, name, pixelation value.  

#### return_pixelated_image: 
This function takes in an image as input and returns a pixelated copy of the image. This function does not pixelate the image itself instead it calls the pixelate_image function. 

#### pixelate_image: 
This function is the bread and butter of the program. It takes an input image and output image name. It then creates a temporary resized image that is created by dividing the images height and width by the pixelation value. This temporary image is then used to create the output image which is the resized image with the original image's dimensions. This process pixelates the image. 

#### valid_input_extension: 
This function checks whether the input image name is a valid image name. It uses regex to check if the name has a valid image extension. 

### test_project.py 

This File is the accompanying unit test file required for the cs50p project. The file contains 3 functions that can be used with pytest to check if the functions work. The 3 functions test a project.py file function.  

#### test_shortcut_setup: 
This function test that the shortcut_setup function works correctly and dosent take invalid inputs. 

#### test_valid_input_extension: 
This function checks that no invalid file extensions pass the extension checker. 

#### test_return_pixelated_image: 
This function checks whether the function in project.py really does return a pixelated image if a valid one is passed in during its function call. 

## Design choices 

I had to make a few design choices that I'm not too happy about with this project. These choices were made because of my current skill level and due to my time limit as I was going back to college soon and had to get the project mostly finished beforehand. 

### Pixelation filters 

First when researching ways to create pixelation filters in python I found some methods that work out better than the one implemented here however I did not understand how gaussian blur works and wanted all the code to be my own.  

### Encoding and framerate 

I tried for days to get the video function to work with other codecs and video formats. However, the numerous methods I tried would just not work similarly originally intended for the user to be able to customise their frame rate however this too proved too much of a hassle to implement. 

 

## Final Thoughts 

I am quite happy with the outcome of this project. Although the filer is not as great as i would have hoped I successfully created a program that pixelates images and videos. I did what I set out to do and have had fun learning about some of the processes involved. 
