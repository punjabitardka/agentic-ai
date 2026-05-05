import streamlit as st
from surface import surfaceagent 

agent = surfaceagent()
request_code = agent.req_code()

# ui configuration in css
st.set_page_config(page_title="Vision OSINT", page_icon="🕵️", layout="wide")

st.markdown("""
    <style>
    /* 1. Global Reset & Modern Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top left, #0f172a, #020617); /* Deep Navy Gradient */
        font-family: 'Inter', sans-serif;
        color: #f8fafc;
    }

    /* 2. Glassmorphism Search Bar */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(10px);
    }

    /* 3. Professional Action Button */
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #2563eb); /* Modern Blue Gradient */
        color: white;
        border: none;
        padding: 0.6rem 2rem;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(37, 99, 235, 0.3);
    }

    /* 4. Results Cards (Glass Effect) */
    .result-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        transition: border 0.3s ease;
    }
    
    .result-card:hover {
        border: 1px solid #3b82f6;
    }

    /* 5. Custom Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.8);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("OSINT Engine For Facial Recognition")
st.write("---") 


uploaded_file = st.file_uploader("Upload from Gallery", type=['jpg', 'jpeg', 'png'])

#check the picked file
if uploaded_file is not None:
    # Show the user upload
    st.image(uploaded_file, caption="Target Image", width=250)
image_url = st.text_input("Enter Image URL", placeholder="https://example.com/target.jpg")

if st.button("Run OSINT Search"):
    final_target = None 
 
    if uploaded_file is not None:
        try:
            final_target= agent.upload_cloud(uploaded_file.read())
            st.info(f"File Received: {uploaded_file.name} ({len(final_target)} bytes)")
        except Exception as e:
            st.error(f"Upload Error: {e}")
    
    if final_target:
        if request_code == True:
            with st.spinner("Searching global databases..."):
                try:
                    results = agent.search_image(final_target)
                    if results:
                        st.success("Results Found:")
                        st.write(results)
                    else:
                        st.warning("No matches found in the current indices.")
                except Exception as e:
                    st.error(f"Engine Error: {e}")
        else:
            st.info("Primary Key Depleted. Using VR2 Engine...")
            results_vr2 = agent.search_image_VR2(final_target)
            st.success("VR2 Engine Results:")
            st.write(results_vr2)
    else:
            st.error("The app didn't receive your file. If you see a Red X, disable 'Brave Shields' or use the Direct URL provided above.")
            