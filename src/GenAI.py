import os
import pyautogui
import google.generativeai as genai
from dotenv import load_dotenv
import logging
from PIL import ImageGrab
import markdown
from bs4 import BeautifulSoup

class GeminiClient:
    """A client to interact with the Gemini generative AI API.

    This client can send a text-only prompt or a prompt accompanied by an image.
    """

    def __init__(self, api_key: str = None, model_name: str = "gemini-1.5-flash-8b", generation_config: dict = None):
        load_dotenv()
        # Retrieve API key from parameter or environment variable.
        if not api_key:
            try:
                api_key = os.environ["GEMINI_API_KEY"]
            except KeyError:
                raise ValueError("GEMINI_API_KEY not found in environment variables.")
        genai.configure(api_key=api_key)

        # Set up logging for the client.
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Use default generation config if none provided.
        if generation_config is None:
            generation_config = {
                "temperature": 0.3,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 1024,
                "response_mime_type": "text/plain",
            }
        self.generation_config = generation_config
        self.model_name = model_name

        try:
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=self.generation_config
            )
            self.logger.info(f"Initialized Gemini model: {self.model_name}")
        except Exception as e:
            self.logger.error(f"Error initializing Gemini model: {e}")
            raise
    
    def markdown_to_plain_text(self,markdown_text: str) -> str:
        """
        Convert Markdown-formatted text to plain text.

        Args:
            markdown_text: The Markdown-formatted input string.

        Returns:
            A plain text string with Markdown formatting removed.
        """
        # Convert Markdown to HTML
        html = markdown.markdown(markdown_text)
        # Use BeautifulSoup to remove HTML tags
        soup = BeautifulSoup(html, "html.parser")
        plain_text = soup.get_text()
        return plain_text

    def upload_file(self, file_path: str, mime_type: str = None):
        """Uploads the given file to Gemini and returns the file object."""
        try:
            file_obj = genai.upload_file(file_path, mime_type=mime_type)
            self.logger.info(f"Uploaded file '{file_obj.display_name}' as: {file_obj.uri}")
            return file_obj
        except Exception as e:
            self.logger.error(f"Error uploading file '{file_path}': {e}")
            raise

    def take_screenshot(self, filename: str = "screenshot.png") -> str:
        """Takes a screenshot and saves it as the specified filename using Pillow's ImageGrab."""
        try:
            screenshot = ImageGrab.grab()  # This uses Pillow's ImageGrab to take a screenshot
            screenshot.save(filename)  # Save the screenshot as a PNG file
            self.logger.info(f"Screenshot saved as {filename}")
            return filename
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")
            raise
    
    def delete_screenshot(self)->None:
        file_path = "screenshot.png"
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                self.logger.info(f"'{file_path}' deleted successfully.")
            except OSError as e:
                self.logger.error(f"Error deleting '{file_path}': {e}")


    def send_prompt_with_image(self, image_path: str, prompt: str) -> str:
        """Uploads an image and sends a prompt along with it to Gemini.
        
        Args:
            image_path: The path to the image file.
            prompt: The text prompt to accompany the image.
        
        Returns:
            The response text from Gemini.
        """
        try:
            uploaded_file = self.upload_file(image_path, mime_type="image/png")
            chat_session = self.model.start_chat(
                history=[
                    {
                        "role": "user",
                        "parts": [uploaded_file],
                    }
                ]
            )
            response = chat_session.send_message(prompt)
            self.logger.info("Received response from Gemini with image prompt.")
            self.delete_screenshot()
            return self.markdown_to_plain_text(response.text)
        except Exception as e:
            self.logger.error(f"Error in send_prompt_with_image: {e}")
            raise

    def send_prompt(self, prompt: str) -> str:
        """Sends a text-only prompt to Gemini.
        
        Args:
            prompt: The text prompt.
        
        Returns:
            The response text from Gemini.
        """
        try:
            chat_session = self.model.start_chat()
            response = chat_session.send_message(prompt)
            self.logger.info("Received response from Gemini for text prompt.")
            return self.markdown_to_plain_text(response.text)
        except Exception as e:
            self.logger.error(f"Error in send_prompt: {e}")
            raise


# Example usage (this block can be removed when integrating as a module):
if __name__ == "__main__":
    # Configure basic logging to console.
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    client = GeminiClient()
    
    # For a text-only prompt:
    try:
        text_response = client.send_prompt("Tell me about Gemini AI")
        print("Text response:")
        print(text_response)
    except Exception as e:
        print(f"Error during text prompt: {e}")
    
    # For a prompt with an image:
    try:
        # Optionally, take a screenshot (or provide an image path)
        screenshot_path = client.take_screenshot()
        image_response = client.send_prompt_with_image(screenshot_path, "Describe this screenshot")
        print("Image response:")
        print(image_response)
    except Exception as e:
        print(f"Error during image prompt: {e}")
