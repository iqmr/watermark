import os

from PIL import Image, ImageDraw, ImageFont
# Python Image Library PIL

def add_text_watermark_to_folder(
        input_dir, output_dir, watermark_text, position_from_right, position_from_bottom, font_size = 30):

        # Create output directory if it doesn't exist:
        if not os.path.isdir(output_dir):
            os.makedirs(output_directory)

        for filename in os.listdir(input_dir):
                if filename.lower().endswith((".png", ".jpeg", ".jpg", ".bmp")):
                        image_path = os.path.join(input_dir, filename)
                        original = Image.open(image_path)
                        (width, height) = original.size

                        print(f"Image size: {width}x{height}")



                        # Create ImageDraw object
                        draw = ImageDraw.Draw(original)
                
                        # Set up font
                        font = ImageFont.truetype("super_nought.ttf", font_size)
                
                        # Get the text dimensions
                        text_width = font.getmask(watermark_text).getbbox()[2]
                        text_height = font.getmask(watermark_text).getbbox()[3]
                        print(f"text-width: {text_width}, text-height: {text_height}")

                
                        # Get the coord to place watermark in bottom right corner
                        a = width - text_height - position_from_right
                        b = height - text_height - position_from_bottom
                
                        # Apply th watermark
                        draw.text((a,b),text=watermark_text,font=font,fill="white")
                
                        # Save the watermark image in the output directory
                        output_path = os.path.join(output_directory, f"watermarked {filename}")
                
                        original.save(output_path)
                        print(f"Watermarked image saved as {output_path}")
        

input_directory = "./input_directory"
output_directory = "./output_directory"
watermark = "~ Watermaked ~"
add_text_watermark_to_folder(
        input_dir = input_directory,
        output_dir = output_directory,
        watermark_text = watermark,
        position_from_right = 200,
        position_from_bottom = 20,
        font_size = 24
        
)
        
