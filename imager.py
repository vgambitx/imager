from PIL import Image
import glob, os

def max_scaled_size(original_size, needed_size):
	original_width, original_height = original_size
	needed_width, needed_height = needed_size

	width_scale = original_width * 1.0 / needed_width
	height_scale = original_height * 1.0 / needed_height
	print original_size
	print width_scale, height_scale

	scale = max(width_scale, height_scale)

	return (original_width / scale, original_height / scale)


scales = (('', (105, 77)), ('@2x', (210, 144)), ('@3x', (354, 261)), ('~ipad', (227, 162)), ('@2x~ipad', (418, 324)))
# scales = (('_preview', (192, 192)), ('_preview@2x', (384, 384)), ('_preview@3x', (576, 576)))

all_files = glob.glob("*.[jJ][pP][gG]")
all_files += glob.glob("*.[pP][nN][gG]")
all_files += glob.glob("*.[jJ][eE][pP][gG]")
for filename in all_files:
    print filename
    file, ext = os.path.splitext(filename)
    
    original_image = Image.open(filename)
    filtered_file = file.replace(' ', '_')
    for postfix, thumbnail_size in scales:
        x1_image = original_image.copy()
        thumbnail_size = max_scaled_size(original_image.size, thumbnail_size)
        print thumbnail_size
        x1_image.thumbnail(thumbnail_size)
        x1_image.save("out/" + filtered_file + postfix + ".png", "png")