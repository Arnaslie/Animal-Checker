# 🦁 Animal Safety Checker

An AI-powered application that helps you identify animals from photos and determine if they're dangerous in your specific location. Using the Perplexity Sonar API to capture real-time animal information, as information about animals can vary on current context (i.e. season of the year, current location)

## Features

- 📸 **Image Upload**: Upload photos of animals you encounter in the wild
- 🔍 **AI Identification**: Uses Google's Vision Transformer to identify animals
- 🌍 **Location-Aware Safety**: Gets location-specific safety information via Perplexity AI
- 🎨 **User-Friendly Interface**: Simple Streamlit web interface
- ⚡ **Fast Processing**: Real-time analysis and results

## Setup Instructions

### 1. Install Dependencies

Make sure you have Python 3.11+ installed, then install the project dependencies:

```bash
# If using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root with your Perplexity API key:

```bash
echo "PERPLEXITY_API_KEY=your_api_key_here" > .env
```

You can get a Perplexity API key from: https://www.perplexity.ai/settings/api

### 3. Run the Application

#### Option A: Run Both Services Together (Recommended)
```bash
python run_app.py
```

This will start both the FastAPI backend (port 8000) and Streamlit frontend (port 8501).

#### Option B: Run Services Separately

**Terminal 1 - Backend:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Terminal 2 - Frontend:**
```bash
streamlit run streamlit_app.py --server.port 8501
```

### 4. Access the Application

Open your web browser and go to: http://localhost:8501

## How to Use

1. **Upload an Image**: Click "Browse files" and select a clear photo of the animal
2. **Enter Location**: Type your current country (e.g., "Kenya", "US", "Australia")
3. **Analyze**: Click the "🔍 Analyze Animal" button
4. **Get Results**: View the AI-powered safety assessment

## API Endpoints

The FastAPI backend provides the following endpoints:

- `GET /` - Health check
- `POST /animal/file/{location}` - Upload image and get safety analysis

## Project Structure

```
├── app/
│   ├── main.py              # FastAPI application
│   ├── routers/
│   │   ├── animal.py        # Animal identification endpoints
│   │   └── sonar.py         # Perplexity AI 
├── streamlit_app.py         # Streamlit frontend
├── run_app.py              # Script to run both services
├── pyproject.toml          # Project dependencies
└── .env                    # Environment variables (create this)
```

## Technologies Used

- **Backend**: FastAPI, PyTorch, Transformers (Google ViT)
- **Frontend**: Streamlit
- **AI Services**: Perplexity Sonar AI
- **Image Processing**: PIL (Pillow)

## Important Notes

- ⚠️ This tool provides general guidance only
- Always follow local wildlife safety guidelines
- When in doubt, maintain a safe distance from wild animals
- Use clear, well-lit images for best identification results

## Troubleshooting

### Backend Connection Issues
- Make sure the FastAPI server is running on port 8000
- Check that your `.env` file contains a valid Perplexity API key
- Verify no other services are using port 8000

### Image Upload Issues
- Supported formats: PNG, JPG, JPEG
- Make sure images are not corrupted
- Try with smaller image files if upload fails

### GPU/CUDA Issues
- The app will automatically fall back to CPU if GPU is not available
- For faster processing, ensure PyTorch is installed with CUDA support

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
