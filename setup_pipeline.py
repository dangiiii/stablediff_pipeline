import subprocess
# res = subprocess.check_output(["sudo", "apt", "update"])
# for line in res.splitlines():

# install diffusers package from source
print("installing diffusers package from source")
print(subprocess.check_output(['bash','-c', "pip install -qq git+https://github.com/huggingface/diffusers"]))

bashCommands = []
# download dreambooth training scripts
bashCommands.append("wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py")
bashCommands.append("wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/train_dreambooth.py")
bashCommands.append("wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/train_dreambooth_flax.py")
bashCommands.append("wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/train_dreambooth_lora.py")
bashCommands.append("wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/requirements.txt")
bashCommands.append("wget -nc -q -P train_scripts/dreambooth https://github.com/huggingface/diffusers/raw/main/examples/dreambooth/requirements_flax.txt")

# # download custom diffusion training scripts
bashCommands.append("wget -nc -q -P train_scripts/custom_diffusion https://github.com/huggingface/diffusers/raw/main/examples/custom_diffusion/requirements.txt")
bashCommands.append("wget -nc -q -P train_scripts/custom_diffusion https://github.com/huggingface/diffusers/raw/main/examples/custom_diffusion/retrieve.py")
bashCommands.append("wget -nc -q -P train_scripts/custom_diffusion https://github.com/huggingface/diffusers/raw/main/examples/custom_diffusion/train_custom_diffusion.py")

for bashCommand in bashCommands:
    subprocess.call(['bash','-c', bashCommand])

print("downloaded training scripts")

# install reqs for dreambooth training
print(subprocess.check_output(['bash','-c', "pip install -r train_scripts/dreambooth/requirements.txt"]))

# install reqs for custom diffusion training
print(subprocess.check_output(['bash','-c', "pip install -r train_scripts/custom_diffusion/requirements.txt"]))
print(subprocess.check_output(['bash','-c', "pip install clip-retrieval"]))

