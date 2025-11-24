import os
from PIL import Image
# 1. Create a folder named 'raw_images' and put your photos there
INPUT_FOLDER = 'raw_images'

# 2. Processed images will appear here
OUTPUT_FOLDER = 'resized_images'

# 3. Target width in pixels (height will adjust automatically to keep aspect ratio)
TARGET_WIDTH = 800

def process_images():
    # check if input folder exists
    if not os.path.exists(INPUT_FOLDER):
        print(f"Error: The folder '{INPUT_FOLDER}' does not exist.")
        print(f"Please create a folder named '{INPUT_FOLDER}' and add some images.")
        return

    # Create output folder if it doesn't exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created output folder: {OUTPUT_FOLDER}")

    # Get list of files
    files = os.listdir(INPUT_FOLDER)
    print(f"Found {len(files)} files. Starting processing...")

    count = 0

    for filename in files:
        # Check for valid image extensions
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # 1. Open the image
                input_path = os.path.join(INPUT_FOLDER, filename)
                img = Image.open(input_path)

                # 2. Calculate new height to maintain aspect ratio
                # (Original Height / Original Width) * New Width
                aspect_ratio = img.height / img.width
                new_height = int(TARGET_WIDTH * aspect_ratio)

                # 3. Resize the image (LANCZOS is a high-quality resampling filter)
                print(f"Resizing {filename} from {img.size} to ({TARGET_WIDTH}, {new_height})...")
                img = img.resize((TARGET_WIDTH, new_height), Image.Resampling.LANCZOS)

                # 4. Save to output folder
                output_path = os.path.join(OUTPUT_FOLDER, filename)
                img.save(output_path)
                
                count += 1
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

    print(f"\nSuccess! {count} images resized and saved to '{OUTPUT_FOLDER}/'.")

if __name__ == "__main__":
    process_images()