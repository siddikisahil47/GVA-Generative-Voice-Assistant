import sys
import os

from package import kokoro
from package import assistant_p
from utils import get_file_paths

# The only variables that need to be modifed
foldername = "assistantP"
personality = "assistantP"
voicename = "Rem"
useEL = True
usewhisper = True

# This code block only checks if it's being ran as a python script or as an exe
if getattr(sys, "frozen", False):
    script_dir = os.path.dirname(os.path.abspath(sys.executable))
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

foldername_dir, personality_dir, keys = get_file_paths(
    script_dir, foldername, personality
)

chatbot = kokoro.Kokoro(personality=personality_dir, keys=keys, voice_name=voicename)

assistant = assistant_p.AssistantP(chatbot)

assistant.run(
    save_foldername=foldername_dir,
    useEL=useEL,
    # voice_name=voicename,
    usewhisper=usewhisper,
)
