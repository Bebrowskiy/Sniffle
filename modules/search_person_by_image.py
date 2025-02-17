import os
import logging
from deepface import DeepFace
import tensorflow as tf

from utils.ansi import *

if not os.path.exists("images"):
    os.makedirs("images")

tf.config.set_visible_devices([], 'GPU')

# Configure logging to suppress unnecessary messages
logging.basicConfig(level=logging.CRITICAL)  # Suppress everything but the critical errors

def analyze_image(image_path):
    # Checking for file availability
    if not os.path.isfile(image_path):
        print(f"{RED} Error: file '{image_path}' not found. {RESET}")
        return

    try:
        # Performing image analysis
        analysis = DeepFace.analyze(image_path, actions=["age", "gender", "race", "emotion"])
        
        # Check if the result of the analysis is a list
        if isinstance(analysis, list):
            analysis = analysis[0]  # Take the first element of the list, if the result is a list
        
        # Beautiful output of results
        print(f"\n{GREEN} Analysis results for the image '{image_path}':\n {RESET}")
        

        print(f"{CYAN}Age:{RESET} {GREEN}{analysis['age']} {RESET}")
        
        
        gender = max(analysis['gender'], key=analysis['gender'].get)
        print(f"{CYAN}Gender:{RESET} {GREEN}{gender} ({analysis['gender'][gender]:.2f}%){RESET}")
        

        print(f"{CYAN}Race:{RESET} {GREEN}{analysis['dominant_race']}{RESET}")
        
 
        print(f"{CYAN}Emotions:{RESET} {GREEN}{analysis['dominant_emotion']}{RESET}")
        

        print(f"\n{CYAN}Details by race:{RESET}")
        for race, probability in analysis['race'].items():
            print(f"{GREEN}  {race}: {probability:.2f}%{RESET}")
        

        print(f"\n{CYAN}Details by emotions:{RESET}")
        for emotion, probability in analysis['emotion'].items():
            print(f"{GREEN}  {emotion}: {probability:.2f}%{RESET}")
    
    except Exception as e:
        print(f"{RED} Analysis error: {e} {RESET}")

def main():
    print(f"{RED}!!!!Test Module!!!!{RESET}")
    print(f"{RED}Only AI photo analyze{RESET}\n")
    image_path = input("\033[1;34m[*] Image Path (default images/search.jpg): \033[0m")
    if image_path == '':
        image_path = "images/search.jpg"
    analyze_image(image_path)