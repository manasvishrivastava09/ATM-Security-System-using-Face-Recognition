from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from imutils.video import VideoStream
import cv2 
vs = VideoStream(src=0).start()
 frame = vs.read()
detections = faceNet.forward() # detection of faces
    	faces = []
    	locs = []
    	preds = []
    			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    			(startX, startY, endX, endY) = box.astype("int")
    
    			# ensure the bounding boxes fall within the dimensions of
    			# the frame
    			(startX, startY) = (max(0, startX), max(0, startY))
    			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

    			face = frame[startY:endY, startX:endX]
    			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    			face = cv2.resize(face, (224, 224))
    			face = img_to_array(face)
    			face = preprocess_input(face)

faces.append(face)
locs.append((startX, startY, endX, endY))

    		faces = np.array(faces, dtype="float32")
    		preds = cover_model.predict(faces, batch_size=32)# to predict face is covered or not covered
               
                (startX, startY, endX, endY) = box
                (covered, not_covered) = pred
                self.label = "Covered" if covered > not_covered else "Not Covered"
                self.color = (0, 0, 255) if self.label == "Covered" else (0, 255, 0)
                self.con = int(max(covered, not_covered) * 100)
                label1 = ''
                label1 = "{:.2f}%".format(max(covered, not_covered) * 100)

                cv2.putText(frame, label1, (startX, startY - 10), # used tp print confidence percentage on screen
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, self.color, 2)
                cv2.rectangle(frame, (startX, startY), (endX, endY), self.color, 2) # to show rectangle 

                cv2.destroyAllWindows()
                vs.stop()
