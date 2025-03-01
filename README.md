# Virtual Mouse Control With Gesture Recognition and Voice Assistant

A Final Year Project for VIT, this project demonstrates a novel way to control a computer interface using hand gestures and voice commands. It leverages MediaPipe for real-time gesture recognition, integrates a custom voice assistant named **Krishna**, and incorporates generative AI (using Google Gemini) for enhanced query responses. The system offers an alternative and accessible method of interaction by combining gesture recognition and voice control in a unified platform.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

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
- **Sleep/Wake Up Commands**: Control the system’s active state.
- **Divine Mode (GenAI Integration)**: Leverage Google Gemini 2.0 Flash for generative AI responses including screenshot analysis and description.

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
To launch the integrated voice assistant:
```bash
python Voice_Assistant.py
```

### Running Only Gesture Recognition
To run gesture recognition independently:
```bash
python Gesture_Controller.py
```

The system will start the webcam feed for gesture recognition. For voice commands, ensure your microphone is set up correctly.

---

## Project Structure

```
├── README.md
├── requirements.txt
├── .env                # Contains GEMINI_API_KEY
├── src
│   ├── Voice_Assistant.py   # Main entry for voice assistant and integration with gesture control.
│   ├── Gesture_Controller.py # Code for capturing and processing hand gestures using MediaPipe.
│   ├── GenAI.py             # Integration with Google Gemini generative AI.
│   ├── app.py               # Eel-based GUI for the chat interface.
│   └── web/                # contains the files for the UI of the chatbot
│   └── logs/       # Contains logs of the chatbot
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
  | Name | Github  | Email | Linkedin | Instagram |
  | ------------- | ------------- | ------------- | ------------- | ------------- |
  | Aritro Saha | [GitHub](https://github.com/halcyon-past) | [Email](titanssuperior@gmail.com) | [LinkedIn](https://www.linkedin.com/in/aritro-saha/) | [Instagram](https://www.instagram.com/halcyon_past/) |

  
