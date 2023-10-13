#!/usr/bin/python3

from jetson_inference import poseNet
from jetson_utils import videoSource, videoOutput, cudaFont

net = poseNet("resnet18-hand")

input = videoSource("/dev/video0")
output = videoOutput("webrtc://@:8554/output")
font = cudaFont()

fingers = ["index_finger", "middle_finger", "ring_finger", "baby_finger"]
superHero = ""

while True:
    # capture the next image
    img = input.Capture()

    if img is None: # timeout
        continue  

    superHero = "Human"
    
    # perform pose estimation (with overlay)
    poses = net.Process(img, overlay="links,keypoints")

    # print the pose results
    #print("detected {:d} objects in image".format(len(poses)))

    for pose in poses:
        for f in fingers:
          i=pose.FindKeypoint(f+'_1')
          j=pose.FindKeypoint(f+'_4')
          if i < 0 or j < 0:
           continue
          start=pose.Keypoints[i]
          end=pose.Keypoints[j]
          x1=start.x
          x2=end.x
          y1=start.y
          y2=end.y
          dist=((x2-x1)**2+(y2-y1)**2)**0.5
          if dist > 220:
            superHero = 'Wolverine'
          elif dist > 150:
            superHero = "Iron-Man"
          elif dist > 50:
            superHero = "Jedi"
          elif dist > 20:
            superHero = "Bat-Man"
          else: 
            superHero = ""
          #print(f, dist)
        #print(pose)
        #print(pose.Keypoints)
        #print('Links', pose.Links)
 
    font.OverlayText(img, text=superHero, 
    x=5, y=5 + (font.GetSize() + 5),
    color=font.White, background=font.Gray40)

    # render the image
    output.Render(img)

    # print out performance info
    #net.PrintProfilerTimes()

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break


