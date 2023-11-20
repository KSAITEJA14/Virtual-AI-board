
# Virtual AI Board

## Introduction
This project is designed to create a virtual AI board that can recognize and interpret hand gestures in real-time. It uses advanced machine learning algorithms to process video input and identify specific hand markers and actions.

## System Requirements
- Python 3.8 or above
- Required Python libraries: [list any libraries that need to be installed]
- Docker (optional for containerization)

## Installation Steps
1. Clone the repository to your local machine.
2. Install the required Python libraries by running `pip install -r requirements.txt`

## Running the Project
1. Navigate to the cloned project directory.
2. Execute the `run.py` script to start the program: `python3 run.py`.

## Files Description
- `detectActions.py`: Contains logic for detecting hand actions.
- `draw_vid.py`: Responsible for drawing the output on the video feed.
- `run.py`: The main script to run the project.
- `Dockerfile`: Contains all the commands to assemble an image for docker.

## Docker Setup (Optional)
If you are using Docker, follow these steps to build and run the project in a container:
1. Build the Docker image: `docker build -t virtual-ai-board .`
2. Run the Docker container: `docker run -it --name virtual-ai-board virtual-ai-board`

## Additional Information
- The project uses a specific hand marker system as shown in the `hand_marks.png` image. Each marker corresponds to a specific point on the hand that the AI will track.

FOR DRAWING:

thumb finger should be left to the index finger 
logic: 
   thumb_tip_x > index_finger_MCP_x 

FOR CHANGING COLORS:

Thumb and index finger should be below the wrist
logic: 
    if wrist_y > index_finger_leftmost_y > index_finger_MCP_y:
        curr_result = True

https://github.com/VSMourya/Virual-AI-board/assets/30852815/45149548-5ffb-4049-a5f1-107dd2649944
