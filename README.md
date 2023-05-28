# stablediff_pipeline
This pipeline expects the SD models to be downloaded into a local folder. Example to download sd-15 model:
```
git lfs install
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
```
This works accordingly for all other models on huggingface but may prompt a request for your username and password if you want to download a model where you have to share your details on the model card.

1. create a conda environment
2. switch to conda env
3. run "setup_pipeline.ipynb" notebook to install diffusers package and training scripts
4. change "MODELS_FOLDER" in sd.cfg to your local models folder (or create symlink named 'models' that links to your local models folder)
5. test installation
```
python test_setup.py
```
