# Generative Voice Assistant (GVA)

**Break the boundaries of communication with GVA, a powerful AI assistant that understands and responds like a human.**

## Features ✨

* **Natural, Conversational Interactions:** Converse freely with GVA, just as you would with a friend.
* **Advanced Language Understanding:** GVA comprehends complex questions and requests, providing insightful responses.
* **Text-to-Speech and Speech-to-Text:** Communicate seamlessly using both voice and text.
* **Conversation History Storage:** GVA remembers past conversations, enabling it to learn and adapt over time.
* **Tailored Responses:** GVA's personality and responses can be customized to match your preferences.

## Technologies ️

* **Python**
* **LLM (OpenAI)**
* **Libraries:**
  * SpeechRecognition
  * elevenlabslib
  * openai
  * pyttsx3
  * sounddevice
  * soundfile
  * pyaudio
  * pyyaml
  * pyinstaller

## Set Up

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure Settings:**
   - Update `keys.yaml` with your API keys for OpenAI and Eleven Labs.
   - Customize voice, personality, and other preferences in `assistant_p.py`.
   - Here's a quick description of the variables I reccommend be modified. If you want to see how this is implemented in code, check out the python scripts in the assistants folder. You'll find these at the top of the python script.
   ```bash
   foldername = "assistantP"
   personality = "assistantP"
   voicename = "Rem"
   useEL = False
   usewhisper = True
   ```

The 5-ish variables you can modify:
  * You set the foldername of where the conversations will be stored, this will be set in the conversations folder.
  * You set the personality by inputing the name of your text file and then editting the contents of the txt file name that is specified. What this does is "prime" the ChatGPT conversation and sets the personality of the bot. All of your prompts must go in the prompts folder and I have some examples in there already.
  * If you're using Eleven Labs for voice generation, change voicename to whatever voice you want that is available to you in Eleven Labs.
  * If you want to use Eleven Labs, change useEL to True
  * If you want to use Whisper instead of google voice recognition, change usewhisper to True.

    
The other text below the 5 variables in the script are objects and function calls to set-up the voice assisant using the class and function in the voice_assistant module.

Most of the functions in the voice_assistant module have docstrings that you can read to clairfy what it does, but I'm still working on making it more clear.

3. **Run:**
   
   ```bash
   cd assistants
   dir
   python assistantp.py
   ```

## Usage

1. Initiate a conversation by speaking to GVA or typing your input.
2. Engage in natural dialogue, asking questions, seeking advice, or simply enjoying conversation.

## Contribute

Interested in collaborating? Check out the issues and pull requests to contribute to the project's development.


## Contact
For any queries or feedback, reach out to siddikisahil47@gmail.com.

