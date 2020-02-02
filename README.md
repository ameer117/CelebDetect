# CelebDetect

CelebDetect allows users to upload video files and find all instances of given celebrities. Users are prompted to upload a video file and then search for one or many names of celebrities using just their voice with help from the Google Cloud Speech-to-Text API. CelebDetect then utilizes uses Amazon Rekognition to scan all faces in the video and returns all the points in which those celebrities are in the video. Users can jump around between points in the video in which their given celebrity or celebrities are in the frame!

The front end was built using Python Flask, JavaScript, HTML/CSS.

The back end utilizes the machine learning based Amazon Rekognition API, tuned to detect as many celebrities as possible in different settings, cosmetic makeup, and other conditions. The video file that is uploaded is stored using Amazon Web Services and LeanCloud.

Users search for the name of a celebrity or celebrities using the machine learning and neural net powered Google Speech-to-Text API.
