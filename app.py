from counterfit_connection import CounterFitConnection
import io
from counterfit_shims_picamera import PiCamera
print("Import done.")

CounterFitConnection.init('127.0.0.1', 5000)
print("CounterFit init done.")

camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 0
print("Camera init done.")

image = io.BytesIO()
camera.capture(image, 'jpeg')
image.seek(0)
print("Capture done.")

with open('image.jpg', 'wb') as image_file:
    image_file.write(image.read())

print("Write done. AKA DONE!")
