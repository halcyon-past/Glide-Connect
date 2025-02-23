import logging
import os
import sys
import time
import webbrowser
from datetime import datetime, date
from os import listdir
from os.path import isfile, join
from threading import Thread

import pyttsx3
import pyautogui
import speech_recognition as sr
from pynput.keyboard import Key, Controller

import Gesture_Controller
import app

# Configure logging
logger = logging.getLogger("KrishnaAssistant")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# File handler
file_handler = logging.FileHandler('krishna_assistant.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(console_formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.propagate = False

class KrishnaAssistant:
    """A virtual assistant that uses speech recognition, text-to-speech, and gesture control."""

    def __init__(self):
        self.today = date.today()
        self.recognizer = sr.Recognizer()
        self.keyboard = Controller()
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

        self.file_exp_status = False
        self.files = []
        self.current_path = ''
        self.is_awake = True

        with sr.Microphone() as source:
            self.recognizer.energy_threshold = 500
            self.recognizer.dynamic_energy_threshold = False

    def reply(self, message: str) -> None:
        app.ChatBot.addAppMsg(message)
        logger.info(message)
        self.engine.say(message)
        self.engine.runAndWait()

    def wish(self) -> None:
        current_hour = datetime.now().hour
        if 0 <= current_hour < 12:
            self.reply("Good Morning!")
        elif 12 <= current_hour < 18:
            self.reply("Good Afternoon!")
        else:
            self.reply("Good Evening!")
        self.reply("I am Krishna, I have the answers to all your questions.")

    def record_audio(self) -> str:
        with sr.Microphone() as source:
            self.recognizer.pause_threshold = 0.8
            try:
                audio = self.recognizer.listen(source, phrase_time_limit=5)
                voice_data = self.recognizer.recognize_google(audio)
                return voice_data.lower()
            except sr.RequestError:
                self.reply("Sorry, my service is down. Please check your internet connection.")
            except sr.UnknownValueError:
                logger.warning("Unable to recognize audio.")
            return ""

    def respond(self, voice_data: str) -> None:
        logger.info(f"Voice Input: {voice_data}")
        voice_data = voice_data.replace('krishna', '').strip()
        app.eel.addUserMsg(voice_data)

        if not self.is_awake:
            if 'wake up' in voice_data:
                self.is_awake = True
                self.wish()
            return

        if 'hello' in voice_data:
            self.wish()
        elif 'what is your name' in voice_data:
            self.reply("My name is Krishna!")
        elif 'date' in voice_data:
            self.reply(self.today.strftime("%B %d, %Y"))
        elif 'time' in voice_data:
            current_time = datetime.now().strftime("%H:%M:%S")
            self.reply(current_time)
        elif 'location' in voice_data:
            self.reply('Which place are you looking for ?')
            temp_audio = self.record_audio()
            app.eel.addUserMsg(temp_audio)
            self.reply('Locating...')
            url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
            try:
                webbrowser.get().open(url)
                self.reply('This is what I found Sir')
            except:
                self.reply('Please check your Internet')
        elif 'search' in voice_data:
            query = voice_data.split('search', 1)[1].strip()
            self.reply(f"Searching for {query}")
            url = f"https://google.com/search?q={query}"
            try:
                webbrowser.open(url)
                self.reply("This is what I found, Sir.")
            except Exception as e:
                logger.error(f"Error opening web browser: {e}")
                self.reply("Please check your internet connection.")
        elif 'bye' in voice_data or 'by' in voice_data:
            self.reply("Goodbye Sir! Have a nice day.")
            self.is_awake = False
        elif 'exit' in voice_data:
            app.ChatBot.close()
            raise SystemExit
        
        # Dynamic Commands
        elif 'launch gesture recognition' in voice_data:
            if Gesture_Controller.GestureController.gc_mode:
                self.reply("Gesture recognition is already active.")
            else:
                gc = Gesture_Controller.GestureController()
                thread = Thread(target=gc.start)
                thread.start()
                self.reply("Launched successfully.")
        elif 'stop gesture recognition' in voice_data or 'top gesture recognition' in voice_data:
            if Gesture_Controller.GestureController.gc_mode:
                Gesture_Controller.GestureController.gc_mode = 0
                self.reply("Gesture recognition stopped.")
            else:
                self.reply("Gesture recognition is already inactive.")
        elif 'copy' in voice_data:
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.press('c')
                self.keyboard.release('c')
            self.reply("Copied.")
        elif 'paste' in voice_data or 'page' in voice_data or 'pest' in voice_data:
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.press('v')
                self.keyboard.release('v')
            self.reply("Pasted.")
        # File Navigation (Default Folder set to C://)
        elif 'list' in voice_data:
            self.current_path = 'C://'
            try:
                self.files = listdir(self.current_path)
                files_str = ""
                for idx, file in enumerate(self.files, start=1):
                    files_str += f"{idx}: {file}<br>"
                    logging.info(f"{idx}: {file}")
                self.file_exp_status = True
                self.reply("These are the files in your root directory.")
                app.ChatBot.addAppMsg(files_str)
            except Exception as e:
                logging.error(f"Error listing files in {self.current_path}: {e}")
                self.reply("Unable to list files.")
        elif self.file_exp_status:
            if 'open' in voice_data:
                try:
                    index = int(voice_data.split()[-1]) - 1
                    selected_file = self.files[index]
                    file_path = os.path.join(self.current_path, selected_file)
                    if isfile(file_path):
                        os.startfile(file_path)
                        self.file_exp_status = False
                    else:
                        # Update directory navigation if the selection is a folder
                        self.current_path = os.path.join(self.current_path, selected_file, '')
                        self.files = listdir(self.current_path)
                        files_str = ""
                        for idx, file in enumerate(self.files, start=1):
                            files_str += f"{idx}: {file}<br>"
                            logging.info(f"{idx}: {file}")
                        self.reply("Opened successfully.")
                        app.ChatBot.addAppMsg(files_str)
                except Exception as e:
                    logging.error(f"Error opening file or directory: {e}")
                    self.reply("You do not have permission to access this folder or the selection is invalid.")
            elif 'back' in voice_data:
                if self.current_path == 'C://':
                    self.reply("Sorry, this is the root directory.")
                else:
                    try:
                        # Remove the last directory from the current path
                        path_parts = self.current_path.rstrip(os.sep).split(os.sep)
                        new_path = os.sep.join(path_parts[:-1]) + os.sep
                        self.current_path = new_path
                        self.files = listdir(self.current_path)
                        files_str = ""
                        for idx, file in enumerate(self.files, start=1):
                            files_str += f"{idx}: {file}<br>"
                            logging.info(f"{idx}: {file}")
                        self.reply("Going back.")
                        app.ChatBot.addAppMsg(files_str)
                    except Exception as e:
                        logging.error(f"Error navigating back: {e}")
                        self.reply("Unable to go back in the directory structure.")
        else:
            self.reply("I am not programmed to do this.")

    def run(self) -> None:
        chatbot_thread = Thread(target=app.ChatBot.start)
        chatbot_thread.start()

        while not app.ChatBot.started:
            time.sleep(0.5)

        self.wish()
        while True:
            logger.info("Waiting for voice input...")
            if app.ChatBot.isUserInput():
                logger.info("Received input from GUI")
                voice_data = app.ChatBot.popUserInput()
            else:
                logger.info("Recording voice...")
                voice_data = self.record_audio()
            logger.info(f"Voice data: {voice_data}")

            if "krishna" in voice_data:
                try:
                    logger.info("Responding to voice input...")
                    self.respond(voice_data)
                except SystemExit:
                    self.reply("Exit successful.")
                    break
                except Exception as e:
                    logger.error(f"Exception occurred: {e}")
                    break

def main():
    try:
        assistant = KrishnaAssistant()
        assistant.run()
    except Exception as e:
        logger.critical(f"Critical error encountered: {e}")

if __name__ == "__main__":
    main()
