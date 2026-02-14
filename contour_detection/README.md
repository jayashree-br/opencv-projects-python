<h1 align="center">Real-Time Contour Detection using OpenCV</h1>

<p align="center">
A Computer Vision project that performs real-time contour detection using a webcam feed.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project captures live video from a webcam and processes each frame to detect object boundaries 
using contour detection techniques in OpenCV.
</p>

<p><b>Processing Pipeline:</b></p>
<ol>
  <li>Capture frame from webcam</li>
  <li>Convert frame to grayscale</li>
  <li>Apply Gaussian Blur</li>
  <li>Perform Canny edge detection</li>
  <li>Extract contours</li>
  <li>Draw contours on original frame</li>
</ol>

<hr>

<h2>🛠 Functions Used & Explanation</h2>

<h3>1. cv.VideoCapture()</h3>
<p>Initializes webcam input.</p>
<pre><code>cap = cv.VideoCapture(0)</code></pre>
<ul>
  <li><b>0</b> → Default webcam</li>
  <li>Reads frames continuously</li>
</ul>

<h3>2. cv.cvtColor()</h3>
<p>Converts the frame from BGR to Grayscale.</p>
<pre><code>gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)</code></pre>
<ul>
  <li>Reduces computational complexity</li>
  <li>Improves contour detection accuracy</li>
</ul>

<h3>3. cv.GaussianBlur()</h3>
<p>Applies Gaussian smoothing to reduce noise.</p>
<pre><code>blur = cv.GaussianBlur(gray, (5,5), 0)</code></pre>
<ul>
  <li><b>(5,5)</b> → Kernel size</li>
  <li>Reduces unwanted intensity variations</li>
</ul>

<h3>4. cv.Canny()</h3>
<p>Performs edge detection.</p>
<pre><code>edges = cv.Canny(blur, 125, 175)</code></pre>
<ul>
  <li><b>125</b> → Lower threshold</li>
  <li><b>175</b> → Upper threshold</li>
  <li>Detects strong gradients in the image</li>
</ul>

<h3>5. cv.findContours()</h3>
<p>Extracts contours from the edge-detected frame.</p>
<pre><code>contours, hierarchy = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)</code></pre>
<ul>
  <li><b>cv.RETR_LIST</b> → Retrieves all contours</li>
  <li><b>cv.CHAIN_APPROX_SIMPLE</b> → Compresses contour points</li>
  <li>Returns contour coordinates and hierarchy</li>
</ul>

<h3>6. cv.drawContours()</h3>
<p>Draws detected contours on the original frame.</p>
<pre><code>cv.drawContours(frame, contours, -1, (0,255,0), 2)</code></pre>
<ul>
  <li><b>-1</b> → Draw all contours</li>
  <li><b>(0,255,0)</b> → Green color</li>
  <li><b>2</b> → Thickness</li>
</ul>

<h3>7. cv.imshow()</h3>
<p>Displays the processed frame in a window.</p>

<h3>8. cv.waitKey()</h3>
<p>Waits for keyboard input to exit the program.</p>
<pre><code>if cv.waitKey(1) & 0xFF == ord('q'):
    break</code></pre>

<h3>9. cap.release() & cv.destroyAllWindows()</h3>
<p>Releases webcam and closes all OpenCV windows properly.</p>

<hr>

<h2>🚀 How to Run</h2>

<pre><code>
pip install -r requirements.txt
python contour_webcam.py
</code></pre>

<p>Press <b>q</b> to exit the webcam window.</p>

<hr>

<h2>🧠 Concepts Demonstrated</h2>

<ul>
  <li>Image preprocessing</li>
  <li>Noise reduction</li>
  <li>Edge detection</li>
  <li>Contour extraction</li>
  <li>Real-time video frame processing</li>
</ul>

<hr>

<h2>🎯 Learning Outcome</h2>

<p>
This project strengthened my understanding of how object boundaries are detected,
how preprocessing impacts detection accuracy, and how real-time Computer Vision
systems process video frame by frame.
</p>
