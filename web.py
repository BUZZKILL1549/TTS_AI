import os
import gradio as gr
from kokoro import KPipeline
import soundfile as sf
import tempfile

def generate_speech(text, voice, speed):
    """Generates speech from text"""
    if not text.strip():
        return None

    temp_dir = tempfile.mkdtemp()
    output_file = os.path.join(tmep_dir, "output.wav")

    generator = KPipeline(
        text,
        voice = voice,
        speed = float(speed)
    )

    for _, (_, _, audio) in enumerate(generator):
        sf.write(output_file, audio, 24000)
        return output_file

    return None

def main():
    try:
        import gradio
    except ImportError:
        import subprocess
        subprocess.check_call(["pip", "install", "gradio"])

    voices = ["af_heart", "en_us_cathy", "en_us_stella", "en_british_male_cs"]

    demo = gr.Interface(
       fn = generate_speech,
       inputs = [
           gr.Textbox(label = "Text to synthesize", lines = 5, placeholder = "Enter text to speech...")
           gr.Dropdown(choices = voices, value = "af_heart", lable = "Voice")
           gr.Slider(minimum = 0.5, maximum = 2.0, value = 1.0, step = 0.1, label = "Speed")
        ],
       outputs = gr.Audio(type = "filepath"),
       title = "Kokoro TTS",
       description = "TTS using Kokoro",
       allow_flagging = "never",
    )

    demo.launch(share = True)

if __name__ == "__main__":
    import sys
    if "gradio" not in sys.modules:
        import subprocess
        subprocess.check_call(["pip", "install", "gradio"])
    main()
