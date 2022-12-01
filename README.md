
# 24 hours of traffic in prishtina

A brief description of what this project does and how you can use it!

 
## Documations

### Index.html

In the index.html file we have our own self-hosted version of google maps acceseed by their API (you need your own token) with my custom style you can change it to your liking.

Disclamer: You have to host this file as a live server.

### Main.py

This file calls our self hosted map with Selenium and creates clean headless screenshots with the appropriate file name.

Disclamer: You should call this file via a CronJob so you don't have to do it yoursel every 10 minutes.

### Preproccess.py

This file cleansup the screenshots and adds a nice overlay on top of it to showcase data as: "Time", "Date, "Technologies", "Credits", etc.

### MP4.py and GIF.py

Finally these two file will get all the processed images and order them based of the time of the screenshot (the file name) and then generate and output their adequate file type, use GIF.py to generate it as a GIF or MP4.py if you want a MP4 video instead.