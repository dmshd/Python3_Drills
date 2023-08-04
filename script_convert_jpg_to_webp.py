``` Python
# convert_jpg_to_webp.py
# Description: Convert all jpg files in a directory to webp

import os
import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 convert_jpg_to_webp.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Directory does not exist")
        sys.exit(1)
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            subprocess.run(["cwebp", "-q", "75", os.path.join(directory, filename), "-o", os.path.join(directory, filename.replace(".png", ".webp"))])

if __name__ == "__main__":
    main()
```
As long as the cwebp package is installed and Python 3 is available, this script should work 
let's break down this line of code:
``` Python
subprocess.run(["cwebp", "-q", "75", os.path.join(directory, filename), "-o", os.path.join(directory, filename.replace(".png", ".webp"))])
```




> -   `"cwebp"`: This is the name of the command-line tool being called. The `cwebp` tool is used to convert images to the WebP format.
>     
> -   `"-q"`: This is an option that sets the quality of the output WebP image. The quality value can range from 0 (worst) to 100 (best).
>     
> -   `"75"`: This is the quality value being set. In this case, the quality of the output WebP images is set to 75.
>     
> -   `os.path.join(directory, filename)`: This is the path to the input image. The `os.path.join()` function is used to concatenate the directory path and the filename into a full path.
>     
> -   `"-o"`: This option specifies the output file.
>     
> -   `os.path.join(directory, filename.replace(".png", ".webp"))`: This is the path to the output WebP image. The `.replace(".png", ".webp")` part is used to change the file extension from `.png` to `.webp`.
