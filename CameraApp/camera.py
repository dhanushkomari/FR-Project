import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings



class VideoCamera(object):
	def __init__(self):
		# self.video = cv2.VideoCapture('rtsp://192.168.137.137:8080/h264_ulaw.sdp')
		self.video = cv2.VideoCapture(1)
			

	def __del__(self):
		self.video.release()
		

	def get_frame(self):        
		success, image = self.video.read()

		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)


		return jpeg.tobytes()
	
	def dhanush(self):
		self.name = 'dhanush'
		self.college = 'prik'
		print(self.name, self.college)

		return [self.name, self.college]

	def FrCode(self):
		sucess, image = self.video.read() 
	