#!/bin/bash

echo "Starting Face Detection"
konsole -e bash -c "python3 Face_Detection.py" & disown

echo "Starting Face Calculate"
konsole -e bash -c "python3 Face_Calculate.py" & disown

echo "Starting YOLOv8_Face_Tracking"
konsole -e bash -c "python3 YOLOv8_Face_Tracking.py"
