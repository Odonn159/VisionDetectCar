# VisionDetectCar
This program was a commission work designed to use OpenCV on a Raspberry Pi to be able to detect the Self-Driving status of the vehicle. The program reads from a camera detected by opencv and determines the state of the screen. It only plays noise when the gray steering wheel is up, which implies that the car cannot detect the lanes of the highway, and therefore manual steering is required. All other states including Green (Steering wheel), SpeedLimit, and Halfcovered are detected but do not need to play a sound and signal.  
![Alt text](/Green#1.jpg?raw=true "Title")
