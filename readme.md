# Mango Diseases

This project identifies the disease of an infected mango leaf using image classification.

## The Algorithm

The algorithm uses a resnet-18 model that was retrained to identify different diseases in mango leaves through transfer learning. When run, the program will print the class of the disease and the confidence.

## Running this project

1. Make sure to have [jetson-inference](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md) already installed on your nano.
2. Download the 'models' folder and 'mangoLeafDisease.py' files into your nano. (Make sure to place them in the same directory)
3. cd into the directory where the program is located using ```cd <PATH HERE>```
4. Run the program by using the following command on the terminal.

   ```python3 mangoLeafDisease.py <PATH TO SAMPLE IMAGE>```

Once the program has finished running, the resulting class and confidence will be printed in the terminal.

## Demo

[![PROGRAM DEMO](https://img.youtube.com/vi/l0BZjBVIxRk/0.jpg)](https://youtu.be/l0BZjBVIxRk)
