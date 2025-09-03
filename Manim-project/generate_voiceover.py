# generate_voiceover.py
from gtts import gTTS
import os

# Read the full narration text
with open("narration_intro.txt", "r", encoding="utf-8") as file:
    full_text = file.read()

# Split the narration into sections based on double line breaks
sections = full_text.strip().split("\n\n")

# Define filenames for each section
output_files = [
    "assets/audio/voiceover_opening.mp3",
    "assets/audio/voiceover_intro.mp3",
    "assets/audio/voiceover_closing.mp3"
]

# Ensure the audio folder exists
os.makedirs("assets/audio", exist_ok=True)

# Generate TTS for each section
for section_text, filename in zip(sections, output_files):
    tts = gTTS(text=section_text, lang='en', slow=False)  # slow=False = normal speed
    tts.save(filename)
    print(f"Generated {filename}")

print("All voiceovers generated successfully!")
