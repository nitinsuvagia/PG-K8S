import subprocess
import os

def build_and_push_image(dockerfile_path, image_tag, context_dir):
    try:
        print(f"Building Docker image {image_tag}...")
        subprocess.run([
            'docker', 'build', '-f', dockerfile_path,'-t', f"{image_tag}", context_dir
        ], check=True)

        print(f"Pushing Docker image {image_tag}...")
        subprocess.run([
            'docker', 'push', f"{image_tag}"
        ], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        raise

def main():

    # Replace below line of code to fetch Widget uploaded and it's Code Path
    # Also fetch other required fields from Pakckage.json file
    
    dockerhub_path = "nitinsuvagia" # we will create "quantumdatalytica"
    package_name = "passwordlocker" # This name will be from Pakcage.json
    version = "1.0.0" # This image version will be from Pakcage.json

    folders = ['folder1', 'folder2']  # Replace with your folders using Parameters
    
    for folder in folders:
        dockerfile_path = os.path.join(folder, 'Dockerfile')
        context_dir = folder    # It's current Directory of Dockerfile
        image_tag = f"{dockerhub_path}/{package_name}:{version}"

        build_and_push_image(dockerfile_path, image_tag, context_dir, )

    if __name__ == "__main__":
        main()