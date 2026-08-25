 ## 1. WHAT IS DEEP LEARNING?
- Deep learning is a branch of machine learning inspired by the human brain.
- It uses artificial neural networks with many layers (hence "deep") to learn directly from raw data like images, sound, and text without needing human help to point out features.

## 2. MAIN TYPES OF DEEP LEARNING
- ANN (Artificial Neural Networks): Simple networks with connected layers, mostly used for standard tables of numbers or text data.
- CNN (Convolutional Neural Networks): Special networks designed specifically for images, videos, and visual data.
- RNN / LSTM: Networks with memory, used for things that happen in a sequence over time, like speech or text sentences.
- Transformers: Modern, powerful models used for advanced AI, language translation, and large language models.

## 3. WHAT IS A CNN (CONVOLUTIONAL NEURAL NETWORK)?
- A CNN is a type of deep learning model built specifically to process images.
- Instead of looking at an entire image at once in a confusing way, a CNN scans the image piece by piece to find edges, shapes, and patterns, making it great for things like face recognition or object detection.

## 4. THE LAYERS OF A CNN
A CNN is made of several steps or layers stacked together:
1. Input Layer: Takes in the raw image and its pixel values.
2. Convolutional Layer: The main building block. It uses filters to scan the image and pull out features like lines, curves, and textures.
3. ReLU Activation Layer: Adds math to the network so it can learn complicated, non-linear patterns instead of just straight lines.
4. Pooling Layer: Shrinks the image size to make processing faster and reduce memory use.
5. Flatten Layer: Flattens the 2D/3D image data into a long 1D list of numbers.
6. Fully Connected (Dense) Layer: Combines all the learned features together to start understanding what the object actually is.
7. Output Layer: Gives the final answer or prediction (for example: "Cat" or "Dog").
