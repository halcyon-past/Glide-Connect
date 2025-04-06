# Virtual Mouse Control With Gesture Recognition and Voice Assistant [![](https://img.shields.io/badge/python-3.9.21-blue.svg)](https://www.python.org/downloads/) [![platform](https://img.shields.io/badge/platform-windows-green.svg)](https://www.microsoft.com/en-in/windows?r=1)

A Final Year Project for VIT, this project demonstrates a novel way to control a computer interface using hand gestures and voice commands. It leverages MediaPipe for real-time gesture recognition, integrates a custom voice assistant named **Krishna**, and incorporates generative AI (using Google Gemini) for enhanced query responses. The system offers an alternative and accessible method of interaction by combining gesture recognition and voice control in a unified platform.

---

## Table of Contents

- [Virtual Mouse Control With Gesture Recognition and Voice Assistant  ](#virtual-mouse-control-with-gesture-recognition-and-voice-assistant--)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
    - [Gesture Recognition](#gesture-recognition)
    - [Voice Assistant (Krishna)](#voice-assistant-krishna)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Clone the Repository](#clone-the-repository)
    - [Environment Setup](#environment-setup)
    - [Configuration](#configuration)
  - [Usage](#usage)
    - [Running the Voice Assistant](#running-the-voice-assistant)
    - [Running Only Gesture Recognition](#running-only-gesture-recognition)
  - [Voice Commands](#voice-commands)
  - [Project Structure](#project-structure)
  - [Future Enhancements](#future-enhancements)
  - [Contributors](#contributors)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
- [Team](#team)

---

## Introduction

The Virtual Mouse project reimagines human-computer interaction by providing a gesture- and voice-controlled interface. With this project, users can perform various mouse operations like cursor movement, clicks, scrolling, and system adjustments (volume and brightness) using hand gestures captured via a webcam. Additionally, the integrated voice assistant, **Krishna**, extends functionality by enabling voice commands for tasks such as file navigation, web searches, and leveraging generative AI for contextual responses (Divine Mode). This project was designed and developed as part of the final year curriculum at VIT.

---

## Features

### Gesture Recognition
- **Neutral Gesture**: Default state.
- **Move Cursor**: Real-time hand tracking to move the mouse pointer.
- **Click Operations**: Left click, right click, and double click.
- **Scrolling**: Vertical and horizontal scrolling.
- **Drag and Drop**: Using hand gestures to initiate and complete drag actions.
- **Multiple Item Selection**: Select multiple items using specific gestures.
- **Volume and Brightness Control**: Adjust system settings via pinch gestures.

### Voice Assistant (Krishna)
- **Launch/Stop Gesture Recognition**: Voice commands to control the gesture recognition module.
- **Google Search & Navigation**: Initiate web searches or locate places using Google Maps.
- **File Navigation**: List and open files or directories.
- **Date and Time Inquiry**: Respond with current date and time.
- **Copy & Paste Operations**: Keyboard shortcuts triggered by voice.
- **Sleep/Wake Up Commands**: Control the assistant's active listening state.
- **Divine Mode (GenAI Integration)**: Leverage Google Gemini Flash for generative AI responses including screenshot analysis and description.

---

## Prerequisites

- **Python Version:** 3.9.21
- **Operating System:** Windows (with required modules like `pywin32`)
- **Tools:** Anaconda Distribution (recommended for environment management)
- **Hardware:**
  - Webcam for gesture recognition
  - Microphone for voice input

---

## Installation

### Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/halcyon-past/Glide-Connect.git
```
For detailed instructions on cloning, visit [GitHub's documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Environment Setup

1. **Create a Conda Environment:**
   ```bash
   conda create --name gesture python=3.9.21
   ```
2. **Activate the Environment:**
   ```bash
   conda activate gesture
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Install pywin32:**
   ```bash
   conda install pywin32
   ```

### Configuration

1. **Set up Gemini API Key:**
   - Navigate to the `src` directory.
   - Create a `.env` file with the following content:
     ```bash
     GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>
     ```
   - To generate a Gemini API Key, visit [Google AI Studio](https://aistudio.google.com/apikey).

2. **Navigate to the `src` Folder:**
   - Open your terminal and change the directory to the `src` folder:
     ```bash
     cd path/to/your/repo/src
     ```

---

## Usage

### Running the Voice Assistant
To launch the integrated voice assistant (which also allows controlling gesture recognition):
```bash
python Voice_Assistant.py
```
The assistant will greet you and display a chat interface. You can interact via voice or by typing in the chat window.

### Running Only Gesture Recognition
To run gesture recognition independently without the voice assistant:
```bash
python Gesture_Controller.py
```
The system will start the webcam feed for gesture recognition. Ensure your microphone is set up correctly if using voice commands with the main assistant.

---

## Voice Commands

Interact with the Krishna assistant using the following voice commands. You can also type these commands into the chat interface. *(Note: While the wake word "Krishna" isn't strictly necessary for every command due to current logic, using it is good practice).*

* **`hello`**
    * **Action:** Greets the user based on the current time (Good Morning, Afternoon, or Evening).
    * **Example:** "Krishna, hello"

* **`what is your name`**
    * **Action:** The assistant states its name.
    * **Example:** "Krishna, what is your name?"

* **`date`**
    * **Action:** Replies with the current date.
    * **Example:** "Krishna, what is the date today?"

* **`time`**
    * **Action:** Replies with the current time.
    * **Example:** "Krishna, what time is it?"

* **`location`**
    * **Action:** Asks the user for a place name, then opens Google Maps to that location in a web browser.
    * **Example:** "Krishna, find a location" (Assistant will ask: "Which place are you looking for?") -> User replies: "Eiffel Tower"

* **`search [query]`**
    * **Action:** Performs a Google search for the text following the word "search".
    * **Example:** "Krishna, search for the latest Python news"

* **`copy`**
    * **Action:** Simulates pressing Ctrl+C (copy command).
    * **Example:** "Krishna, copy this"

* **`paste` / `page` / `pest`**
    * **Action:** Simulates pressing Ctrl+V (paste command). Recognizes common misinterpretations.
    * **Example:** "Krishna, paste here"

* **`launch gesture recognition`**
    * **Action:** Starts the gesture controller module in a separate thread if it's not already running.
    * **Example:** "Krishna, launch gesture recognition"

* **`stop gesture recognition` / `top gesture recognition`**
    * **Action:** Stops the currently running gesture controller module. Recognizes common misinterpretations.
    * **Example:** "Krishna, stop gesture recognition"

* **`list`**
    * **Action:** Enters "File Explorer Mode". Lists the files and folders in the `C://` drive, numbering them. Subsequent `open` and `back` commands work within this mode.
    * **Example:** "Krishna, list files"

* **`open [number]`** (Only in File Explorer Mode)
    * **Action:** Opens the file or navigates into the folder corresponding to the number provided after the `list` command. Updates the listed files if a folder is opened. Exits File Explorer Mode if a file is opened.
    * **Example:** (After `list` shows "3: Documents") "Krishna, open 3"

* **`back`** (Only in File Explorer Mode)
    * **Action:** Navigates to the parent directory of the current path shown in File Explorer Mode and lists its contents. Does nothing if already at `C://`.
    * **Example:** "Krishna, go back"

* **`enter divine mode`**
    * **Action:** Enters a special mode where subsequent queries (until "exit divine mode") are sent to the Google Gemini AI for a generative response.
    * **Example:** "Krishna, enter divine mode"

* **`exit divine mode`** (Only in Divine Mode)
    * **Action:** Exits Divine Mode and returns to normal command processing.
    * **Example:** "Exit divine mode"

* **`look at my screen`** (Only in Divine Mode)
    * **Action:** Takes a screenshot of the current screen, asks the user what they want to know about it, and sends both the image and the user's follow-up question to the Google Gemini AI for analysis and response.
    * **Example:** "Look at my screen" (Assistant will ask: "What do you want to know about it?") -> User replies: "Summarize the text in this article"

* **`bye` / `by`**
    * **Action:** The assistant says goodbye and enters a "sleep" state (`is_awake = False`). It will only respond to the "wake up" command.
    * **Example:** "Krishna, bye bye"

* **`wake up`** (Only when in sleep state)
    * **Action:** Wakes the assistant from its sleep state, allowing it to process commands normally again.
    * **Example:** "Krishna, wake up"

* **`exit`**
    * **Action:** The assistant says goodbye and shuts down the application, including the GUI.
    * **Example:** "Krishna, exit now"

* **(Any other unrecognized command)**
    * **Action:** The assistant replies with "I am not programmed to do this."
    * **Example:** "Krishna, make me coffee" -> Assistant: "I am not programmed to do this."

---

## Project Structure

```
├── README.md
├── requirements.txt
├── .env                  # Contains GEMINI_API_KEY
├── src
│   ├── Voice_Assistant.py   # Main entry for voice assistant and integration with gesture control.
│   ├── Gesture_Controller.py # Code for capturing and processing hand gestures using MediaPipe.
│   ├── GenAI.py             # Integration with Google Gemini generative AI.
│   ├── app.py               # Eel-based GUI for the chat interface.
│   ├── web/                 # Contains the files for the UI of the chatbot
│   └── logs/                # Contains logs of the chatbot
```

- **Voice_Assistant.py:** Combines voice recognition with gesture commands and handles system commands.
- **Gesture_Controller.py:** Implements hand gesture detection and corresponding mouse controls.
- **GenAI.py:** Manages API interactions with Google Gemini for text and image-based generative responses.
- **app.py:** Provides the graphical user interface for user interaction via Eel.

---

## Future Enhancements

- **Multi-Language Support:** Extend voice commands to support additional languages.
- **Improved Gesture Set:** Introduce more complex gestures for additional functionalities.
- **Performance Optimization:** Fine-tune gesture detection algorithms for lower latency.
- **User Personalization:** Adapt the interface and commands based on individual user preferences.
- **Mobile Integration:** Develop companion mobile applications for broader accessibility.

---

## Contributors
<a href="https://github.com/halcyon-past/Glide-Connect/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=halcyon-past/Glide-Connect" />
</a>

---

## Contributing

Contributions are welcome! If you would like to contribute to this project:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add Your Feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Please adhere to the project’s coding conventions and document your changes thoroughly.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **MediaPipe:** For providing a robust framework for gesture detection.
- **Google Gemini:** For the generative AI capabilities.
- **Open Source Community:** For the many libraries and tools that made this project possible.

# Team
  | Name | Github  | Email | Linkedin | Instagram | Youtube |
  | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
  | Aritro Saha | [GitHub](https://github.com/halcyon-past) | [Email](mailto:titanssuperior@gmail.com) | [LinkedIn](https://www.linkedin.com/in/aritro-saha/) | [Instagram](https://www.instagram.com/halcyon_past/) | [Youtube](https://www.youtube.com/@veripyed) |
  | Rupkatha De | [GitHub](https://github.com/rupkatha-de) | [Email](mailto:derupkatha@gmail.com) | [LinkedIn](https://www.linkedin.com/in/rupkatha-de-80a422231/) | [Instagram](https://www.instagram.com/rupkatha_26/) | NA |
  | Anusmita Panji | NA | [Email](mailto:kolianusmita@gmail.com) | [LinkedIn](https://www.linkedin.com/in/anusmita-panji-a509551b5) | [Instagram](https://www.instagram.com/anusmitap_21/) | NA |
