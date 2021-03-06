import sys
print(sys.path)
try:
    sys.path.remove("/opt/ros/kinetic/lib/python2.7/dist-packages")
except Exception:
    pass
import cv2
import imutils.paths as paths
import face_recognition
import pickle
import os
import imutils
import numpy as np
import time
import shutil
import datetime
import pandas as pd
import time
import warnings    
import psycopg2
import requests
import re
conn = psycopg2.connect(host = 'localhost',database = 'FR-SMILE-DB',user = 'postgres',password = 'admin123',port = 5432)

    
warnings.filterwarnings("ignore")
 
#import sqlite3

def recent_time(a):
    rec_time = a 
    year = rec_time[0:4]
    mon = rec_time[5:7]
    day = rec_time[8:10]
    hour = rec_time[11:13]
    mins = rec_time[14:16]
    sec = rec_time[17:19]
    
    new_date = year+'-'+mon+'-'+day+' '+hour+':'+mins+':'+sec
    last_time = datetime.datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S') 
    #print('last_obj_time: ',last_time)
    now = datetime.datetime.now()
    #print('now_time: ', now)
    difference=float((now-last_time).seconds)
    return difference
def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)



def main(): 
    count=0
    global df_u
    df_u = pd.DataFrame(columns = ['Name','time']) 
    print(df_u)

    encoding = "E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/encoding_append.pickle"
    
    encoding = "E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/encoding_append.pickle"
    data = pickle.loads(open(encoding, "rb").read())

    #cap = cv2.VideoCapture("rtsp://192.168.43.1:8080/h264_ulaw.sdp")
    cap = cv2.VideoCapture(0)
    if cap.isOpened :
        ret, frame = cap.read()
        print(ret)
    else:
         ret = False
    while(ret):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(frame, width=400)
        r = frame.shape[1] / float(rgb.shape[1])

        boxes = face_recognition.face_locations(rgb, model= "hog")
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []
        
        #profile = getProfile(id)

   
        for encoding in encodings:
                matches = face_recognition.compare_faces(np.array(encoding),np.array(data["encodings"]),tolerance=0.45)
                name = "Unknown"
               
                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                   
                    
                    for i in matchedIdxs:
                                  name = data["names"][i]
                                  counts[name] = counts.get(name, 0) + 1
                                  name = max(counts, key=counts.get)
                names.append(name)
                
                print('Im printing names',names)
                
                if names[0]=='Unknown':
                    
                    df_u=df_u.append({'Name':'Unknown','time':time.time()},ignore_index=True)
                    print(len(df_u))
                    if len(df_u)>=20:
                        df_u=df_u.iloc[-10:,:]
                        t_diff=(df_u.iloc[9,1]-df_u.iloc[0,1])
                        if t_diff<=20:
                            currenttime1 = datetime.datetime.now() 
                            c_time = str(currenttime1)
                            
                            cursor = conn.cursor()
                            
                            stat = 'unknown'
                            d = datetime.datetime.now()
                            cursor.execute("ROLLBACK")
                            query = '''INSERT INTO "CameraApp_status"(status, created_at) VALUES (%s, %s)'''
                            cursor.execute((query), (stat,d))
                            
                            conn.commit()
                            print('DB Updated with unknown')
                            print(t_diff)
                            print('unkonwn patient detected please fill your data')     
                            print('please fill your data')
                            t_start=time.time()
                            while True:
                                t_end=time.time()
                                response=requests.get('http://127.0.0.1:8000/api/patients')
                                
                                x=response.json()
                                d = x['created_at']
                                q = recent_time(d)
                                id=x['first_name']+str(x['id'])
                                if q<=80:
                                    count =1
                                    shutil.rmtree('E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Images/user1')
                                    print('object found, user has been entered the data through app')
                                    break
                                if (t_end-t_start)>80:
                                    count=0
                                    print('I am unnecessarily being terminated')
                                    break
                                    
                if (count>=1):
                    count=0
                    mode = 0o666
                    r_t_diff=20
                    
                    
                    

                    user_folder=id
                    path = os.path.join('E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Images/','user1') 
                    os.mkdir(path, mode) 
                    count_i=0
                    cv2.imshow("Frame", frame)
                    while True:
                        print('training the model')
                        cv2.imwrite("E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Images/user1/frame%d.jpg" % count_i, frame)     # save frame as JPEG file      
                        success,frame = cap.read()
                        print('Read a new frame: ', success)
                        count_i += 1 
                        if count_i>=10:
                            dataset = "E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Images/user1"# path of the data set
                            module = "E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Images/encoding1.pickle" # were u want to store the pickle file
                            imagepaths = list(paths.list_images(dataset))
                            print(imagepaths)
                            knownEncodings = []
                            knownNames = []
                            print('executed')
                            print(len(knownEncodings))
                            for (i, imagePath) in enumerate(imagepaths):
                                
                                print("[INFO] processing image {}/{}".format(i + 1,len(imagepaths)))
                                name = user_folder
                                print('here is the error',name)
                                image = cv2.imread(imagePath)
                                rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                                boxes = face_recognition.face_locations(rgb, model= "hog")
                                encodings = face_recognition.face_encodings(rgb, boxes)
                                print('not executed')
                                for encoding in encodings:
                                    print('not executed twice')
                                    knownEncodings.append(encoding)
                                    knownNames.append(name)
                                    print("[INFO] serializing encodings...")
                                    data = {"encodings": knownEncodings, "names": knownNames}
                                    output = open(module, "wb")
                                    pickle.dump(data, output)
                                    output.close()
                            module = "E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/encoding_append.pickle" # were u want to store the pickle file
                            output = open(module, "wb")
                            module = pickle.loads(open(module, "rb").read())
                            
                            module1 = "E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Images/encoding1.pickle" # were u want to store the pickle file
                            module1 = pickle.loads(open(module1, "rb").read())
                            
                            
                            x=module1["names"]+module["names"]
                            
                            
                            y=module1["encodings"]+module["encodings"]
                            
                            
                            
                            print(len(module1["encodings"]),len(module["encodings"]))
                            
                            
                            module = "E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Images/encoding_append.pickle" # were u want to store the pickle file
                            
                            
                            data = {"encodings": y, "names": x}
                            
                            output = open(module, "wb")
                            pickle.dump(data, output)
                            output.close()
                            
                            data = pickle.loads(open(module, "rb").read())
                            break
                                    
                    
                    #os.mkdir(path, mode) 
                    cv2.imwrite("E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Images/user1" % count, frame)
                    
                    

        for ((top, right, bottom, left), name) in zip(boxes, names):
            top = int(top * r)
            right = int(right * r)
            bottom = int(bottom * r) 
            left = int(left * r)
            cv2.rectangle(frame, (left, top), (right, bottom),(255, 255, 255), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (255, 255, 0), 2)
            
            #cv2.putText(frame,'NAME :'+str(profile[1])+' '+(left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), lineType=cv2.LINE_AA)
            df=pd.read_csv("E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Id.csv")
            l=len(df)
                
                
            df=df.iloc[:,1:]

            df1 = pd.DataFrame() 

            
            df1['name']=[name]
            now =(datetime.datetime.now())
            
            dt = now.strftime("%d-%m-%Y %H:%M:%S")


            df1['date']=[dt]
            
            df1['dt']=[dt[:10]]

            
            if len(df)==0:
         
                df=df.append(df1, ignore_index = True) 
                                
                df.to_csv("E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Id.csv")

            else:
                
                last_name=df.iloc[l-1,0]
                if last_name != name:
                    
                    if name != "Unknown":
                    
                        df=df.append(df1, ignore_index = True) 
                                    
                        df.to_csv("E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Id.csv")

                        
                else:
                    l=len(df)
                    ld=df.iloc[l-1,1]
                    x =(datetime.datetime.now())
                    date_time_obj=datetime.datetime.strptime(ld, '%d-%m-%Y %H:%M:%S')
                    z=str(x-date_time_obj)
                    print(z)
                    #k=get_sec(z)
                    """if k>60:
                        df=df.append(df1, ignore_index = True) 
                                
                        df.to_csv("Id.csv")"""
                        
                    try:
                        k=get_sec(z)
                        if k>60:
                            df=df.append(df1, ignore_index = True)
                            currenttime1 = datetime.datetime.now() 
                            c_time = str(currenttime1)
                            c_time = str(currenttime1)
                            df.to_csv("E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Id.csv")
                            pushing=df.iloc[-1,0]
                            cursor = conn.cursor()
                            
                            stat = 'known'
                            d = datetime.datetime.now()
                            cursor.execute("ROLLBACK")
                            query = '''INSERT INTO "CameraApp_status"(status, created_at) VALUES (%s, %s)'''
                            cursor.execute((query), (stat,d))
                            
                            
                            print('DB updated with known')

                    except ValueError:
                        df=df.append(df1, ignore_index = True)
                        currenttime1 = datetime.datetime.now()
                        c_time = str(currenttime1)
                        df.to_csv("E:/WEB_PROJECTS/Smile_FR_Project/FR_ML_CODE/Id.csv")
                        pushing=df.iloc[-1,0]
                        cursor = conn.cursor()
                        
                        stat = 'known'
                        d = datetime.datetime.now()
                        cursor.execute("ROLLBACK")
                        query = '''INSERT INTO "CameraApp_status"(status, created_at) VALUES (%s, %s)'''
                        cursor.execute((query), (stat,d))
                        
                        print('DB updated with known')

            now =(datetime.datetime.now())
            
            dt8 = now.strftime("%d-%m-%Y %H:%M:%S")
            if (int(dt8[11:13]))>=10:
                print('yes')
                    
        cv2.imshow("Frame", frame)
        if(cv2.waitKey(1)==ord('q')):
            break                                                

    cv2.destroyAllWindows()
    cap.release()
    
    
if __name__ == "__main__":
    main()
  

    