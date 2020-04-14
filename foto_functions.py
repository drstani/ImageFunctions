import photos

def get_image_location(album, asset_id, show_image=False):
	""" Takes album and image_id as index number and returns the location
	coordinates of image. If show_image ist set to True the image will be
	shown in the console """
	asset = album.assets[asset_id]
	if show_image is True:
		img = asset.get_image()
		img.show()
	ret = asset.location
	return ret


def get_locations_of_all_albumimages(album):
	""" Returns a list of all image locations (coordinates)
	in a given album ikcluding empty locations. Returns second list
	with indices of images with no location. """  
	# number of images in selected album
	number_of_images = len(album.assets)
	# coordinates of all images in selected album including empty locations
	coordinates = list()
	# index of images ith empty location
	none_index = list()

	for i in range(number_of_images):
		print(i)
		coord = get_image_location(album=albums[3], asset_id=i, show_image=False)
			
		if coord is None:
			none_index.append(i)
		coordinates.append(coord)
	return coordinates, none_index
	

def find_album_index_by_name(album_list, album_name):
	""" Returns album index by full 
	or partial album name given as string """
	album_indices = list()

	for i in range(len(album_list)):
		if album_list[i].__str__().find(album_name) != -1:
			album_indices.append(i)
	
	return album_indices
