# stablediff_pipeline
This pipeline expects the SD models to be downloaded into a local folder. Example to download sd-15 model:
```
git lfs install
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
```
This works accordingly for all other models on huggingface but may prompt a request for your username and password if you want to download a model where you have to share your details on the model card.

# Setup
1. create a conda environment
```
# to install conda env in 'env' subfolder of anaconda directory
conda create -n stablediff python=3.10 jupyter
# to install conda env in subfolder of current dir
conda create --prefix ./stablediff python=3.10 jupyter
```
2. activate conda env
3. run "setup_pipeline.ipynb" notebook to install diffusers package and training scripts
```
jupyter-notebook setup_pipeline.ipynb
```
OR
run 'setup_pipeline.sh'
```
sudo chmod 774 setup_pipeline.sh
./setup_pipeline.sh
```
4. change "MODELS_FOLDER" in sd.cfg to your local models folder (or create symlink named 'models' that links to your local models folder)
```
ln -s path/to/pretrained/models/root_dir/ models
```
5. test installation
```
python test_setup.py
```
