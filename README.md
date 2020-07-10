# LifeGuard

### Usage
*   Install necessary packages
    ```bash
    pip install -r requirements.txt
    ```
*   Run the file
    ```bash
    python DrownDetect.py
    ```

### Approach
*   Detect a person and enclose it in a rectangle (blue)
*   Extract the centre of the bounding box and track it for some iterations
*   If it's static, the person is flagged as drowning

### References
https://pjreddie.com/darknet/yolo/
