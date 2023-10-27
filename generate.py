import subprocess

prompt = input("Enter your image prompt: ")

steps = 10
width = 512
height = 512

print(f"Generating {width}x{height} image with {steps} steps...")

venv_python = './venv/bin/python'
args = [venv_python, 'main.py', prompt, f'--steps={steps}', f'--width={width}', f'--height={height}', '--interactive']
subprocess.run(args)
