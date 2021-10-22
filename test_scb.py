import requests
import json
import numpy as np
import base64
import matplotlib.pyplot as plt
import cv2
from imageio import imread
import io

API_ENDPOINT = "https://kiosk-com-joo-earn.herokuapp.com/getQrcodePayment" 

url = "http://localhost:3000/test"
newHeaders = {'Content-type': 'application/json'}
data = {'cost':90}

r = requests.post(url = API_ENDPOINT, data =json.dumps(data) ,headers=newHeaders)
image  = json.loads(r.text)['qr']

# print(image)


# r = base64.decodebytes(image)
# im_bytes = base64.b64decode(image)
# im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
# img = cv2.imdecode(im_arr)
# print(img)
img = imread(io.BytesIO(base64.b64decode(image)))
# print(img)
# plt.figure()
# plt.imshow(img, cmap="gray")
while True:
    cv2.imshow("art",img)
    key = cv2.waitKey(1) 
    if key == ord('q'):
        break
# if & 0xFF == ord(‘q’)

# break
