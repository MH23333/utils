#!/usr/bin/env python
# coding: utf-8

# In[2]:


from aip import AipOcr
from PIL import ImageGrab
from PIL import Image
import io

APP_ID = '00000'
API_KEY = '00000000000000'
SECRET_KEY = '0000000000000000'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def ocr():
    img = ImageGrab.grabclipboard()
    img_bytes = io.BytesIO()
    if isinstance(img, Image.Image):
        #  img.save('test.png', 'png')
        img.save(img_bytes, 'png')
        image = img_bytes.getvalue()
        
        dic_result = client.basicGeneral(image)
        res = dic_result['words_result']
        result = ''
        for m in res:
            print m['words']
            
while True:
    ocr()
    print()
    raw_input()





