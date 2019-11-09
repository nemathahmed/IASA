# IASA
Immersive Acoustic Spatial Awareness

This project has three modules:
># Obstacle Detection for the blind using a 3-D Sound
  >>The sensor array gives the distance from the sensor to the object and a the chip is programmed to give us an array where the first element is the mode and remaining are the angles where the obstacles have been found by the array. Array is of form [ mode, angle1, angle2......] where mode is 0 if the object is closer than 80 cm and 1 if greater than 100 cm. If any one of the sensor is in the mode 0, the overall base signal is used similiar to that of mode 0.
