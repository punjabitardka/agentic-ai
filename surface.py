from serpapi import GoogleSearch as gs
from config import serp_key, search_key, IMGBB_KEY
import requests
import base64
import os


class surfaceagent:
    def __init__(self):
        self.api_key2 = search_key
        self.api_key = serp_key
        self.api_key3 = os.getenv("IMGBB_KEY")

  # we will have to do the try: search_image except: search image vr2 with the bollean vales of req_code function in the main module
    def req_code(self):
        response = requests.get("https://serpapi.com/manage-api-key")
        if response.status_code not in [400, 401, 403, 429]:
            self.reqcode= True
            return self.reqcode
        else:
            self.reqcode= False
            return self.reqcode

    def search_image(self,image_url):

        params = {
            "engine":"google_lens",
            "url": image_url,
            "api_key": self.api_key
        }
        print(f"DEBUG: Searching for URL -> {image_url}")
        search = gs(params)
        results = search.get_dict()
        visual_matches_thingy = results.get("visual_matches", [])
        return visual_matches_thingy

    def search_image_VR2(self,image_url):
        params_2={
            "engine":"google_lens",
            "url": image_url,
            "api_key":self.api_key2
        }
        search_12 = gs(params_2)
        results = search_12.get_dict()
        visual_matches = results.get("visual_matches",[])
        return visual_matches
    
    #to upload jpeg/...files to the cloud and get a public url 
    def upload_cloud(self,file_byte):
        api_key=self.api_key3
        url = "https://api.imgbb.com/1/upload"

        image = base64.b64encode(file_bytes)

        to_deliver = {
            "key": api_key,
            "image": encoded_image

        }

        try:
            response = requests.post(url,to_deliver)
            
            if response.status_code == 200:
                return response.json()['data']['url']
            else:
                return None
        except Exception as e:
            print(f"Cloud Upload Error: {e}")
            return None
         

