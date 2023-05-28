# https://stackoverflow.com/questions/4944295/skip-download-if-files-already-exist-in-wget
# other option: -N (only download newer files)

# install diffusers package from source
pip install -qq git+https://github.com/huggingface/diffusers

# download dreambooth training scripts
wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py
wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/train_dreambooth.py
wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/train_dreambooth_flax.py
wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/train_dreambooth_lora.py
wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/requirements.txt
wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/requirements_flax.txt

# download custom diffusion training scripts
wget -nc -q -P train_scripts/custom_diffusion https://github.com/huggingface/diffusers/raw/main/examples/custom_diffusion/requirements.txt
wget -nc -q -P train_scripts/custom_diffusion https://github.com/huggingface/diffusers/raw/main/examples/custom_diffusion/retrieve.py
wget -nc -q -P train_scripts/custom_diffusion https://github.com/huggingface/diffusers/raw/main/examples/custom_diffusion/train_custom_diffusion.py

# install reqs for dreambooth training
pip install -r train_scripts/dreambooth/requirements.txt

# install reqs for custom diffusion training
pip install -r train_scripts/custom_diffusion/requirements.txt
pip install clip-retrieval
