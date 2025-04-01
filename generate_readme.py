readme_file = "README.md"

#recursively search for all png files in sub directories
import os
png_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".png"):
            #print the path to the file
            print(os.path.join(root, file))
            #store pngs in a list 2d list with the first element being the directory and the second being the file name
            png_files.append([root.lstrip(".\\"), file])
print(png_files)

with open(readme_file, "w") as f:
    f.write("# NOOBSpec canopy repository\n")
    f.write("Collection of files for the noobspec whoop frame\n")
    f.write("\n\n")
    f.write("## Images\n\n")
    last_dir = ""
    for dir_file in png_files:
        #if the directory is not the same as the last directory, write the directory name as header
        if dir_file[0] != last_dir:
            last_dir = dir_file[0]
            f.write(f"### {dir_file[0]}\n")
        #add image to the readme file
        url_dir = dir_file[0].replace(" ", "%20")
        url_file = dir_file[1].replace(" ", "%20")
        url_encoded_file = f"https://github.com/dargust/NOOBSpec/blob/main/{url_dir}/{url_file}?raw=true"
        #write the image to the readme file with a link to the file in github
        f.write(f"![{dir_file[1]}]({url_encoded_file})\n")