# VisionDetectCar
This program was a commission work designed to use OpenCV on a Raspberry Pi to be able to detect the Self-Driving status of the vehicle. The program reads from a camera detected by opencv and determines the state of the screen. It only plays noise when the gray steering wheel is up, which implies that the car cannot detect the lanes of the highway, and therefore manual steering is required. All other states including Green (Steering wheel), SpeedLimit, and Halfcovered are detected but do not need to play a sound and signal.  
![Alt text](/Green#1.jpg "Title")

![Gray Steering Wheel](https://github.com/Odonn159/VisionDetectCar/blob/main/Gray%231.png) "Gray Steering Wheel"
![Green Steering Wheel](https://github.com/Odonn159/VisionDetectCar/blob/main/Green%231.png) "Green Steering Wheel"
![Half-Covered Steering Wheel](https://github.com/Odonn159/VisionDetectCar/blob/main/HalfCovered%231.png) "Half-Covered Steering Wheel"
![Speedlimit](https://github.com/Odonn159/VisionDetectCar/blob/main/Speedlimit.png) "Speedlimit"
