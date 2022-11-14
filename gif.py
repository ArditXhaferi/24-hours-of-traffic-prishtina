import imageio
import glob
import natsort

with imageio.get_writer('./movie.gif', mode='I', duration=0.2) as writer:
    for filename in natsort.natsorted(glob.glob('./preprocces/*.png')):
        image = imageio.imread(filename)
        writer.append_data(image)