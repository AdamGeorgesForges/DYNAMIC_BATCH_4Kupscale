# Real-ESRGAN 4K Upscaler with Batch Processing

This repository extends the [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) project by adding a new Python script, `batch_upscaler.py`, designed for upscaling images in batches on systems with limited computing resources, like laptops. This tool is ideal for users needing to process multiple images efficiently without overloading their hardware.

## About `batch_upscaler.py`

`batch_upscaler.py` is a user-friendly Python script that automates the upscaling of images using the Real-ESRGAN model. It prompts users for the input and output directory paths, then processes each image using the Vulkan-based `realesrgan-ncnn-vulkan.exe` executable. This script is particularly beneficial for systems with limited GPU resources as it handles image processing sequentially to minimize system strain.

### Features

- **Batch Processing:** Upscale multiple images in a sequence to avoid high memory usage.
- **Tile Mode:** Process images in tiles, reducing the overall memory footprint and making it possible to upscale even on low-end hardware.
- **User-Friendly:** Simple CLI prompts guide the user through specifying input and output directories.
- **Flexible Output:** Users can specify a custom output directory or use a default folder.

### How It Works

When you run `batch_upscaler.py`, the script performs the following steps:
1. Prompts the user to enter the directory containing the images to be upscaled.
2. Asks for an output directory where the upscaled images will be saved.
3. Processes each image one by one, using tile-based upscaling to manage memory usage effectively.

This method is particularly advantageous for users with limited system resources, as it minimizes memory and GPU usage per operation, allowing for the upscaling of large image files without requiring powerful hardware.

### System Requirements

- Windows OS
- Python 3.x
- Real-ESRGAN dependencies installed

### Setup and Usage

Clone this repository and navigate to the directory containing `batch_upscaler.py`. Ensure you have Python installed and run the script via command line:

```bash
python batch_upscaler.py
```

Follow the on-screen prompts to input the paths for your image directories.

## Acknowledgements

This project utilizes the powerful [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) by [Xintao](https://github.com/xinntao), built on the [Tencent/ncnn](https://github.com/Tencent/ncnn) framework. For detailed information on the original models and their capabilities, refer to the official [Real-ESRGAN GitHub repository](https://github.com/xinntao/Real-ESRGAN/) and the research paper available [here](https://arxiv.org/abs/2107.10833).

## License

This project is open-sourced under the MIT license. See the [LICENSE](LICENSE) file for more details.