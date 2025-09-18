import os
import sys
from pathlib import Path

def play_sound():
    script_dir = Path(__file__).parent
    wav_file = script_dir / "nice.wav"
    
    if not wav_file.exists():
        print(f"Error: {wav_file} not found")
        return False
    
    if sys.platform == "win32":
        import winsound
        winsound.PlaySound(str(wav_file), winsound.SND_FILENAME)
    elif sys.platform == "darwin":
        os.system(f"afplay {wav_file}")
    else:
        try:
            import pygame
            pygame.mixer.init()
            pygame.mixer.music.load(str(wav_file))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except ImportError:
            os.system(f"aplay {wav_file} 2>/dev/null || play {wav_file} 2>/dev/null")
    
    return True

def main():
    print("Hello from hooks!")
    play_sound()


if __name__ == "__main__":
    main()
