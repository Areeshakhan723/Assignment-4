import os

def main():
    i = 0
    path = "C:/test_folder"
    for filename in os.listdir(path):
        ext = os.path.splitext(filename)[1]  # gets the file extension
        new_filename = "file" + str(i) + ext # Just the new name
        my_src = os.path.join(path, filename)              # Full original path
        my_dest = os.path.join(path, new_filename)   # Full new path

         # Rename the file
        os.rename(my_src, my_dest)

        # Increment the counter for the next file
        i += 1

if __name__ == "__main__":
    main()
