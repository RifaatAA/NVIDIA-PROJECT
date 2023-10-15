# Superhero Charades

Have you ever wanted to play Charades with someone but nobody has had the time for you? Well with this revolutionary code utilising the Jetson Nano, you can play a simple game of charades with your local computer. I guarantee that you will keep playing this exciting game until your computer stops functioning properly. 

I personally came up with this idea to help people with a lack of social skills, improve their confidence by using hand gestures to express themselves.

<img alt="Wolverine" src="https://github.com/RifaatAA/NVIDIA-PROJECT/assets/142425815/d8c0b971-6c19-4595-88bf-789f754b3d54">

## The Algorithm

This is a game of charades using a logitech camera to detect your gestures and process each frame utilisng posenet to return a guess of the Superhero you are trying to impersonate. 

The way this works is by loading the network using the resnet-18-hand mdoel. Then we would need to access the webcam to grab the pose information from the model. We then get the key points that we need from the fingers to find the distance between the 2 points using the distance formula. Once the distance is found, we can depict which superhero you are posing as from the following choises: Wolverine, Iron-Man, Jedi or Bat-Man. Based on the dataset, the finger sizes are decreasing as you go from left to right. The results will be displayed on the video-stream where the user can see which superhero they are destined to be. If no fingers are present, the program will return "Human" indicating that you have no powers. So if you want to become a superhero, just use the code.

## Running this project

1. Install Jetson-Inference. This can be installed from the following link: https://github.com/dusty-nv/jetson-inference/tree/master
2. Download the code from this repository.
3. Plugin your logitech webcam to your Jetson Nano.
4. Use the following terminal command to access the project folder: cd NVIDIA-PROJECT
5. Use the following terminal command to make the file executable: chmod +x Charades.py
6. Use the following terminal command to run the file: ./Charades.py
7. Type in the following URL in your web browser with your Jetson Nano IP address: http://<JETSON-IP>:8554
8. Have Fun!

[View a video explanation here](video link)
