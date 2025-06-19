Virtual Hand-Tracking Keyboard
==============================

Description:
------------
This is a Python program that creates a virtual keyboard controlled by hand gestures using your webcam. 
You can type by hovering your index finger over keys on the screen and making a clicking gesture (bringing your thumb close to the index finger).

Features:
---------
- Real-time hand detection and tracking with cvzone and OpenCV.
- Virtual keyboard with letters, numbers, space, and delete keys.
- Buttons have semi-transparent backgrounds for a modern look.
- Displays typed text in a large placeholder area.
- Click detection with finger distance for intuitive interaction.

Requirements:
-------------
- Python 3.x
- OpenCV (install via pip: pip install opencv-python)
- cvzone (install via pip: pip install cvzone)
- mediapipe (install via pip: pip install mediapipe)

How to Run:
-----------
1. Make sure your webcam is connected and working.
2. Install the required Python packages listed above.
3. Run the script: python virtual_keyboard.py
4. A window will open showing the camera feed and the virtual keyboard.
5. Use your index finger to hover over the keys and "click" by bringing your thumb close to your index finger.
6. Press 'q' to quit the program.

Notes:
------
- For best tracking, use the program in a well-lit environment.
- You can customize the keyboard layout and button appearance in the source code.
- The click delay avoids multiple inputs on a single click.
