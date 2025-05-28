import streamlit as st
import requests
import io
from PIL import Image

# Configure the page
st.set_page_config(
    page_title="Animal Safety Checker",
    page_icon="🦁",
    layout="wide"
)

# App title and description
st.title("🦁 Animal Safety Checker")
st.markdown("""
Upload an image of an animal you've spotted in the wild, and I'll help you determine if it's dangerous in your location!
""")

# Create two columns for layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 Upload Image")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image of the animal",
        type=['png', 'jpg', 'jpeg'],
        help="Upload a clear image of the animal you want to identify"
    )
    
    # Display uploaded image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

with col2:
    st.header("📍 Location Information")
    
    # Location input
    location = st.text_input(
        "Enter your current location (country/region)",
        placeholder="e.g., Kenya, California, Australia",
        help="This helps provide location-specific safety information"
    )
    
    # Submit button
    if st.button("🔍 Analyze Animal", type="primary", use_container_width=True):
        if uploaded_file is not None and location:
            with st.spinner("Analyzing the animal and checking safety information..."):
                try:
                    # Prepare the file for upload
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    
                    # Make request to FastAPI backend
                    response = requests.post(
                        f"http://localhost:8000/animal/file/{location}",
                        files=files
                    )
                    
                    if response.status_code == 200:
                        result = response.text.strip('"')  # Remove quotes if present
                        
                        # Display results
                        st.success("Analysis Complete!")
                        
                        # Create an expandable section for the full response
                        with st.expander("🔍 Detailed Analysis", expanded=True):
                            st.markdown(result)
                            
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                        
                except requests.exceptions.ConnectionError:
                    st.error("❌ Could not connect to the backend server. Make sure the FastAPI server is running on http://localhost:8000")
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
        else:
            if not uploaded_file:
                st.warning("⚠️ Please upload an image first")
            if not location:
                st.warning("⚠️ Please enter your location")

# Sidebar with instructions
with st.sidebar:
    st.header("📋 How to Use")
    st.markdown("""
    1. **Upload an Image**: Click 'Browse files' and select a clear photo of the animal
    2. **Enter Location**: Type your current country or region
    3. **Analyze**: Click the 'Analyze Animal' button
    4. **Get Results**: View the AI-powered safety assessment
    """)
    
    st.header("⚠️ Important Notes")
    st.markdown("""
    - Use clear, well-lit images for best results
    - This tool provides general guidance only
    - Always follow local wildlife safety guidelines
    - When in doubt, maintain a safe distance
    """)
    
    st.header("🔧 Backend Status")
    try:
        response = requests.get("http://localhost:8000/", timeout=2)
        if response.status_code == 200:
            st.success("✅ Backend Connected")
        else:
            st.error("❌ Backend Error")
    except:
        st.error("❌ Backend Offline")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and FastAPI") 