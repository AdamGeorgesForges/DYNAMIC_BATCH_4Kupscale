import os
import subprocess
import shutil

# Supported image formats for processing
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp')

def get_folder_path(prompt_text):
    """Prompt the user for a folder path and validate it."""
    while True:
        folder_path = input(prompt_text).strip().strip('"')  # Remove accidental quotes
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            return folder_path
        print("Invalid folder path. Please enter a valid directory.")

def get_output_folder():
    """Prompt the user for an output folder, creating it if necessary."""
    while True:
        output_folder = input("Enter the output folder path (or press Enter to use 'output' folder in the same directory): ").strip().strip('"')
        if not output_folder:
            output_folder = os.path.join(os.getcwd(), "output")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        return output_folder

def list_images(folder):
    """Return a list of image files (name and extension) in the given folder."""
    return [f for f in os.listdir(folder) if f.lower().endswith(VALID_EXTENSIONS)]

def process_images(input_folder, output_folder):
    """Run Real-ESRGAN on all images in the folder and display live progress."""
    images = list_images(input_folder)
    total_images = len(images)

    if total_images == 0:
        print("No valid images found in the selected folder.")
        return

    # Ask for confirmation before proceeding
    print(f"\n{total_images} images found in '{input_folder}'.")
    confirm = input("Do you want to proceed with upscaling? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Operation canceled.")
        return

    print(f"\nProcessing images... Saving outputs to: {output_folder}\n")

    # Process each image one by one
    for index, image_name in enumerate(images, start=1):
        input_image_path = os.path.join(input_folder, image_name)
        output_image_path = os.path.join(output_folder, f"upscaled_{image_name}")

        print(f"\nProcessing {index}/{total_images}: {image_name}")

        # Run Real-ESRGAN and capture progress
        command = [
            "realesrgan-ncnn-vulkan.exe",
            "-i", input_image_path,
            "-o", output_image_path,
            "-n", "realesrgan-x4plus"
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Display real-time progress updates
        for line in process.stdout:
            line = line.strip()
            if line:  # Only display meaningful lines
                print(f"{index}/{total_images} {line}")

        process.wait()

        if process.returncode == 0:
            print(f"✅ Successfully processed: {image_name}")
        else:
            print(f"⚠️ Error processing: {image_name}")

    print("\n🎉 Batch processing complete! All upscaled images saved in:", output_folder)

# Main program execution
if __name__ == "__main__":
    print("\n🔥 Batch Image Upscaling with Real-ESRGAN 🔥")
    
    input_folder = get_folder_path("Enter the folder containing images: ")
    output_folder = get_output_folder()
    
    process_images(input_folder, output_folder)