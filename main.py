import os

path = "/Users/irinatantsura/Documents/workspace/photos_for_task"
dirs = os.listdir(path)

def count_photo(path_to_photos):
    mass_of_ways_to_photo = []
    for file in path_to_photos:
        path_to_file, file_extension = os.path.splitext(file)
        if file_extension == '.jpg':
            path_to_photo = os.path.join(os.getcwd(), file)
#           print(path_to_photo)
            mass_of_ways_to_photo.append(path_to_photo)
    print(mass_of_ways_to_photo)
    return mass_of_ways_to_photo



count_photo(dirs)
