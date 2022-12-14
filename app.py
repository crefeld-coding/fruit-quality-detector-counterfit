from counterfit_connection import CounterFitConnection
import io
from counterfit_shims_picamera import PiCamera
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
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

print("Write done.")

prediction_url = 'REPLACE_ME'
prediction_key = 'REPLACE_ME'

parts = prediction_url.split('/')
endpoint = 'https://' + parts[2]
project_id = parts[6]
iteration_name = parts[9]

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)
print("Predictor created.")

image.seek(0)
results = predictor.classify_image(project_id, iteration_name, image)
print("Image submitted, results received.")

for prediction in results.predictions:
    print(f'{prediction.tag_name}:\t{prediction.probability * 100:.2f}%')
print("Results done.")
