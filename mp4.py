import os
import moviepy.video.io.ImageSequenceClip
import natsort

image_folder='preprocces'
fps=5

image_files = [os.path.join(image_folder,img)
               for img in natsort.natsorted(os.listdir(image_folder))
               if img.endswith(".png")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('my_video.mp4')