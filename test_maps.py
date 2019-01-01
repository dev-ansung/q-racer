import numpy as np

trackWidth = 10
rectangle = np.full([50, 100], 255, dtype=np.uint8)
startPos = rectangle.shape[0] // 2
rectangle[0:rectangle.shape[0]//2,startPos] = 200
rectangle[0] = 0; rectangle[rectangle.shape[0] - 1] = 0; rectangle[:,0] = 0; rectangle[:,rectangle.shape[1] - 1] = 0
rectangle[trackWidth:rectangle.shape[0]-trackWidth, trackWidth:rectangle.shape[1]-trackWidth] = np.full((rectangle.shape[0]-trackWidth*2, rectangle.shape[1]-trackWidth*2), 0)
rectangle = (rectangle, startPos)