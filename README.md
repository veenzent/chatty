## Quick Chat AI 
###### *built with Gemini AI API*

**A Streamlit-based chatbot powered by Gemini AI API**

### Prerequisites
* Python (version 3.7 or later)
* Streamlit
* google-generative-ai

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/veenzent/chatty.git
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
* Replace the placeholder API key in the script with your actual Gemini AI API key.
* Get your API key [here](https://makersuite.google.com/app/apikey)

### Usage
1. **Run the script:**
   ```bash
   streamlit run st_chat_client.py
   ```


* The script utilizes Streamlit for the user interface and Gemini AI API for generating responses.
* The code includes basic error handling and response streaming.
* For production use, consider adding more robust error handling, performance optimizations, and security measures.

### Customization
* Adjust the title and subtitle as desired.
* Modify the chat interface's appearance using Streamlit's styling options.
* Customize the response generation logic to fit your specific requirements.

### Known Issues
* None at this time.

### Contributing
* Contributions are welcome! Please open an issue or submit a pull request.

<!-- ### License -->