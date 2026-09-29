<h1 style="font-family:Arial; font-size:32px;">Perceptron Shape Classifier (L vs T) — Web Deployment</h1>


<h2 style="font-family:Verdana;">Overview</h2>


This project implements a single‑layer perceptron that classifies simple 10×10 pixel drawings as either L or T. The perceptron is trained on a small custom dataset and deployed to the web using JavaScript, allowing users to draw shapes and receive predictions directly in the browser.

This project demonstrates foundational machine learning concepts including perceptron learning, weight updates, activation functions, and browser‑based inference.


<h2 style="font-family:Verdana;">Live Demo</h2>


You can test the perceptron directly in your browser:

👉 https://svaughn26.github.io/perceptron/


<h2 style="font-family:Verdana;">Technologies Used</h2>


JavaScript — perceptron logic, training loop, UI interaction

HTML/CSS — drawing grid and interface

JSON — dataset storage

GitHub Pages — hosting

Machine Learning Concepts — perceptron, activation function, weight updates


<h2 style="font-family:Verdana;">Model Architecture</h2>

**The perceptron uses:**

Inputs: 100 pixels (10×10 grid)

Weights: 100 learnable parameters

Bias: Single bias term

Activation: Sign function

Outputs:

+1 → T

–1 → L

The model learns by adjusting weights based on misclassified samples.

**Project Structure**
Code
perceptron/
│── index.html          # Main UI for drawing and prediction
│── annotate.html       # Dataset annotation tool
│── app.js              # Perceptron logic + training
│── data.json           # Training dataset
│── styles.css          # UI styling
│── .nojekyll           # Required for GitHub Pages hosting

*How to Run Locally*
1. Clone the repository
Code
git clone https://github.com/svaughn26/perceptron
cd perceptron

2. Open the demo
Simply open:

Code
index.html
No server required.

3. Train the perceptron
Click Train Perceptron to load the dataset and begin training.

4. Draw and predict
Use the grid to draw an L or T, then click Predict to see the model’s output.

<h2 style="font-family:Verdana;">What I Learned</h2>

How perceptrons learn using weight updates

How to represent images as numerical vectors

How to deploy ML models in the browser

How to build interactive UI components with JavaScript

How to manage datasets using JSON

How to host projects using GitHub Pages

<h2 style="font-family:Verdana;">Future Improvements</h2>

Add visualization of weight updates

Add confidence scores

Add support for additional shapes

Improve UI styling and responsiveness

Expand dataset for better accuracy
