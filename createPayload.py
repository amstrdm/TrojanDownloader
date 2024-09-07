from PIL import Image
import os 
import shutils 

def create_directory_structure():

    #define the directory structure
    

    default_dir = f"{os.getcwd()}/dist"
    build_dir = input(f"Enter the directory to which the payload will be built or press Enter for default(default: {default_dir}): ")

    #create default folder if user input is empty
    if build_dir == '':
        build_dir = default_dir
        #if default folder exists create default folder n+1
        if os.path.exists(default_dir) and os.listdir(default_dir): 
            num_count = 1
            path_exists = True
            while path_exists:
                build_dir = default_dir+str(num_count)
                if not os.path.exists(build_dir):
                    path_exists = False
                else:
                    num_count += 1
            print(f"No Path selected, {default_dir} exists and is not empty. Files will be created at {build_dir}")
        elif os.path.exists(default_dir) and os.listdir(default_dir):
            build_dir = default_dir
            print(f"No Path selected. Files will be created at {build_dir}")     
                    

    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
        print(f"created build directory {build_dir}")

    elif os.path.exists(build_dir) and os.listdir(build_dir):
        print("Chosen Directory is not empty please choose an empty directory ")
        
    
def hide_payload(image_path, script):
    # Convert script to binary
    binary_script = ''.join(format(ord(i), '08b') for i in script)
    img = Image.open(image_path)
    pixels = img.load()

    binary_script += '00000000'  # Null terminator to indicate the end of the script
    binary_index = 0

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if binary_index < len(binary_script):
                r, g, b = pixels[i, j]
                r = (r & ~1) | int(binary_script[binary_index])
                binary_index += 1
                pixels[i, j] = (r, g, b)
            else:
                break

    img.save('14113.png')

create_directory_structure()