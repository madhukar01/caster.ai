import cv2

# Open video
video = cv2.VideoCapture('dota_video.flv')

# Read video frame by frame
success, image = video.read()
count = 0

# cv2.imshow('cropped', cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

while success:
    # Crop the map area
    cropped = image[535:720, 0:185]
    cv2.imwrite('frames/frame_%s.png' % count, cropped)
    success, image = video.read()

    print('Saving frame %d' % count)
    count += 1
