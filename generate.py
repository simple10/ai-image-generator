import subprocess

prompt = input("Enter your image prompt: ")
print("Generating image with 4 steps 512x512...")


venv_python = './venv/bin/python'
args = [venv_python, 'main.py', prompt, '--steps=4', '--width=512', '--height=512']
subprocess.run(args)
