# Get the last photo, and show it in the console
import photos
import foto_functions as ff

albums = photos.get_albums()

print(ff.find_album_index_by_name(album_list = albums, album_name = "afrika"))
