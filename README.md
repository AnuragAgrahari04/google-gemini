# 🤖 Google Gemini AI Assistant

A versatile AI assistant powered by Google's Gemini Pro and Gemini Pro Vision APIs, built with Python and Streamlit. This application allows you to have interactive conversations and analyze images seamlessly.

### 🚀 [View Live Demo](https://app-gemini-042004.streamlit.app)

![GitHub stars](https://img.shields.io/github/stars/AnuragAgrahari04/google-gemini?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/AnuragAgrahari04/google-gemini?style=for-the-badge)
![License](https://img.shields.io/github/license/AnuragAgrahari04/google-gemini?style=for-the-badge)

---

## 🌟 About The Project

This project serves as a powerful demonstration of the capabilities of Google's next-generation multimodal AI, Gemini. It provides a simple yet effective user interface created with Streamlit to interact with both the text-based `Gemini Pro` and the image-understanding `Gemini Pro Vision` models.

You can ask complex questions, get detailed explanations, and even upload images to have the AI describe and analyze them.

### ✨ Key Features

* **Conversational AI**: Engage in dynamic, context-aware conversations.
* **Image Analysis**: Upload an image and ask questions about it. The AI can describe the contents, identify objects, and answer context-specific queries.
* **Interactive UI**: A clean and user-friendly web interface built with Streamlit.
* **Multimodal Input**: Seamlessly switch between text-only and text-with-image prompts.

### 🛠️ Built With

This project is built using modern and efficient technologies:

* **[Python](https://www.python.org/)**
* **[Google Gemini API](https://ai.google.dev/)** (`google-generativeai`)
* **[Streamlit](https://streamlit.io/)**
* **[Pillow](https://python-pillow.org/)** (for image handling)

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Before you begin, ensure you have the following installed:
* **Python 3.8+**
* A **Google API Key**. You can obtain one from [Google AI Studio](https://makersuite.google.com/app/apikey).

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/AnuragAgrahari04/google-gemini.git](https://github.com/AnuragAgrahari04/google-gemini.git)
    cd google-gemini
    ```

2.  **Create and activate a virtual environment** (recommended):
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    Create a file named `.env` in the root of the project directory and add your Google API Key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

5.  **Run the application:**
    ```sh
    streamlit run app.py
    ```
    Open your browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

---

## 📖 Usage

You can interact with the app via the **[Live Demo](https://app-gemini-042004.streamlit.app)** or by running it locally.

1.  **Select the Application Mode**: Choose between "Gemini Pro" for text-based chat or "Gemini Pro Vision" for image analysis from the sidebar.
2.  **Ask Questions**: Type your question into the input box and hit "Ask the question" for the text model.
3.  **Upload an Image**: For the vision model, upload an image file (`.jpg`, `.jpeg`, `.png`) and then type your prompt related to the image. Click "Tell me about the image" to get a response.



---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  **Fork** the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a **Pull Request**

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📞 Contact

Anurag Agrahari - [@AnuragAgrahari04](https://github.com/AnuragAgrahari04)

Project Link: [https://github.com/AnuragAgrahari04/google-gemini](https://github.com/AnuragAgrahari04/google-gemini)

---

## 🙏 Acknowledgments

* [Google](https://ai.google.dev/) for creating the powerful Gemini API.
* [Streamlit](https://streamlit.io/) for making web app creation in Python so intuitive.
* [Othneil Drew's README Template](https://github.com/othneildrew/Best-README-Template) for inspiration.
