import os
import streamlit as st

# 1. Permanent Folder Path
UPLOAD_FOLDER = os.path.join(os.getcwd(), "saved_photos")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 2. Stylish Header
st.markdown(
    """
    <style>
    .header-card {
        background: linear-gradient(135deg, #4A90E2, #185a9d);
        padding: 30px;
        border-radius: 40px 40px 10px 10px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.15);
    }
    .header-card h1 {
        color: white !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        margin: 0;
    }
    .header-card p {
        color: #e0e0e0;
        font-size: 16px;
        margin-top: 5px;
    }
    </style>
    
    <div class="header-card">
        <h1>📸 Shani Photo Sharing App</h1>
        <p>hello my friend</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 3. Photo Upload Section
uploaded_file = st.file_uploader(
    "PC se Photo Upload Karein", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    # Check karein ki photo pehle se saved toh nahi hai
    if not os.path.exists(file_path):
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Photo '{uploaded_file.name}' सफलतापूर्वक सेव हो गई!")

st.write("---")
st.subheader("🖼️ Upload Ki Gayi Photos")

# 4. Show Photos
photos = os.listdir(UPLOAD_FOLDER)

if photos:
    cols = st.columns(2)
    for index, photo_name in enumerate(photos):
        photo_path = os.path.join(UPLOAD_FOLDER, photo_name)
        with cols[index % 2]:
            st.image(photo_path, caption=photo_name, use_container_width=True)
            if st.button(f"🗑️ Delete", key=f"del_{index}"):
                os.remove(photo_path)
                st.rerun()
else:
    st.info("Abhi tak koi photo upload nahi hui hai.")