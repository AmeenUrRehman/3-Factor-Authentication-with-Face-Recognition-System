# Imports the required Packages
from flask import Flask , render_template ,  request , Response
import cv2
import numpy as np
import face_recognition as fr
import os
from datetime import datetime

app = Flask(__name__ , template_folder='templates')

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def about():
    return render_template('/register.html')

@app.route('/home')
def home():
    return render_template(('/home.html'))

@app.route('/login_validation' , methods = ["POST"])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    if email == "thomaseinstein@example.com" and password == "12345":
        return render_template("second.html")
    else:
        return render_template("login.html")

@app.route('/second' , methods = ["POST"])
def second_login():
    password = request.form.get('password')
    if password == "password":
        return render_template('/third.html')
    else:
        return render_template("login.html")

@app.route('/third' , methods = ["POST"])
def third_login():
    password = request.form.get("password")
    if password == "EINSTEIN":
        return render_template("/home.html")
    else:
        return render_template("login.html")

path = 'UserImages'
Images = []
ClassNames = []
Mylist = os.listdir(path)
for cl in Mylist:
    CurrentImage = cv2.imread(f'{path}/{cl}')
    Images.append(CurrentImage)
    ClassNames.append(os.path.splitext(cl)[0]) # As we want only the name of the image not type
# Print the names of the images in the List.
print(ClassNames)


def findEcnoding(images):
    EncodeList = []
    for img in images:
        img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)  # convert Images BGR TO RGB
        encode = fr.face_encodings(img)[0]  # finding encoding of the store images
        EncodeList.append(encode)
    return EncodeList

EncodeListKnown = findEcnoding(Images)

# Print When Encoding is Complete (Hint)
print("Encoding Complete")


def login_time(name):
    with open('Users_login_time.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime("%H:%M:%S")
            f.writelines(f'\n{name},{dtstring}')

cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # Read the image
        success, img = cap.read()

        # Resize the image to 1/4th of size so it takes less time by Machine to compare the image.
        imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)

        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

        # Finding the location of the faces in the current Frame  , returns the coordinates of the faces.
        CurrentFaceLoc = fr.face_locations(imgs)

        # Find the encoding of each face in the frame with locations.
        CurrentFaceEncoding = fr.face_encodings(imgs, CurrentFaceLoc)

        # Creating a funtion to compare the Current Face and the store image of the Person
        for EncodeFace, FaceLoc in zip(CurrentFaceEncoding, CurrentFaceLoc):
            match = fr.compare_faces(EncodeListKnown, EncodeFace)
            FaceDist = fr.face_distance(EncodeListKnown, EncodeFace)

            # Return the value of each image after comparing with current face lower the value more chances of the face of same person.
            print(FaceDist)

            # Return the index having minimum value in the list
            matchInd = np.argmin(FaceDist)
            if match[matchInd]:
                name = ClassNames[matchInd].upper()
                print(name)

                y1,x2,y2,x1 = FaceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4 # Resize the image to original
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                height, width, _ = img.shape


                # Call login_time to save the id and time in Users_login_time.csv.
                login_time(name)

                ret, buffer = cv2.imencode('.jpg', img)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

@app.route("/video")
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == "__main__":
    app.run(port=8080)
