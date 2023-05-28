from diffusers import DiffusionPipeline
import torch
from PIL import Image
import os
import configparser

# model_dict = {"midway-sd15":"stable-diffusion-v1-5",
#                 "deliberate":"Deliberate",
#                 #"deepfloyd-xl":"IF-I-XL-v1.0",
#                 "openjourney-v4":"openjourney-v4",
#                 "realistic-vision-14":"Realistic_Vision_V1.4",
#                 "realistic-vision-20":"Realistic_Vision_V2.0"}

# model_names = [v for k,v in model_dict.items()]
# model_root_dir = "/media/datasciencefhswf/data2/stable_diffusion/models/pretrained"

def read_config(file_path:str = "sd.cfg"):
    global MODELS_FOLDER
    
    config = configparser.ConfigParser()
    config.read(file_path)
    
    MODELS_FOLDER = os.path.join(config["DEFAULT"]["MODELS_FOLDER"])

def main():
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"created dir '{output_dir}'")
    
    model_names = [dir for dir in os.listdir(MODELS_FOLDER) if os.path.isdir(os.path.join(MODELS_FOLDER,dir))]
    # model_paths = [os.path.join(MODELS_FOLDER,model_name) for model_name in model_names]

    for model_name in model_names:
        model_path = os.path.join(MODELS_FOLDER,model_name)
        pipeline = DiffusionPipeline.from_pretrained(model_path, safety_checker=None, torch_dtype=torch.float16)
        pipeline.to("cuda")
        out = pipeline("An image of a squirrel in van Gogh style").images[0]
        out = out.save(os.path.join(f"{output_dir}",f"out_vangogh_{model_name}.jpg"))
    
if __name__ == '__main__':
    read_config()
    main()