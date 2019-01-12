import numpy as np
import soundfile as sf
new_data = np.empty([25000,])
y1 = np.empty([25000,])
for j in range(1,2001):
	b= "back"+str(j)+".wav"
	data, samplerate = sf.read(b)
	print len(data)

			

