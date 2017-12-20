import logging
from api import BetaFaceAPI
from xml.etree import ElementTree
import xmltodict
import json

logging.basicConfig(level = logging.INFO)
client = BetaFaceAPI()

face_info = client.upload_face('/home/yash/Desktop/mhcli/pybetaface/image.jpeg', 'yash@ami-lab.ro')

print json.dumps(face_info, indent = 4)
