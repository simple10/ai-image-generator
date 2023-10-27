import subprocess

prompt = input("Enter your image prompt: ")
print("Generating image with 10 steps 512x512...")


venv_python = './venv/bin/python'
args = [venv_python, 'main.py', prompt, '--steps=10', '--width=512', '--height=512']
subprocess.run(args)
