import streamlit as st

# -------------------------------
# Basic Info
# -------------------------------
st.set_page_config(page_title="Nikita Singh | Portfolio", layout="wide")

st.title("💼 Nikita Singh")
st.write("New Delhi, India | 📧 nikitasingh2114@gmail.com | 📞 +91 9140092337")
st.write("🔗 [LinkedIn](https://linkedin.com/in/nikita-singh-015a42192) | "
         "🔗 [GitHub](https://github.com/nikitasingh2114)")

st.markdown("---")

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.title("📂 Portfolio Sections")
section = st.sidebar.radio("Go to:", ["Home", "Resume", "Projects", "Contact"])

# -------------------------------
# Home Section
# -------------------------------
if section == "Home":
    st.header("👋 Welcome to My Portfolio")
    st.write("""
    I am a versatile professional with experience as a **QA Engineer, Full Stack Developer, and Hybrid QA-Dev**.  
    Skilled in **ColdFusion, JavaScript, SQL, Manual Testing, API Testing, and Generative AI (LangChain, HuggingFace, Streamlit, AWS Bedrock)**.  
    Passionate about building **scalable applications** and ensuring **quality through rigorous testing**.
    """)

# -------------------------------
# Resume Section
# -------------------------------
elif section == "Resume":
    st.header("📄 My Resume")
    option = st.selectbox(
        "Select Resume to View:",
        ["QA Engineer", "Full Stack Developer", "Hybrid (QA + Dev)"]
    )

    if option == "QA Engineer":
        st.write("### QA Engineer Resume")
        st.download_button("⬇️ Download QA Resume", 
                           data=open("Nikita_Singh_Resume_QA.pdf", "rb").read(),
                           file_name="Nikita_Singh_Resume_QA.pdf")

    elif option == "Full Stack Developer":
        st.write("### Full Stack Developer Resume")
        st.download_button("⬇️ Download Developer Resume", 
                           data=open("Nikita_Singh_Resume_Developer.pdf", "rb").read(),
                           file_name="Nikita_Singh_Resume_Developer.pdf")

    elif option == "Hybrid (QA + Dev)":
        st.write("### Hybrid Resume")
        st.download_button("⬇️ Download Hybrid Resume", 
                           data=open("Nikita_Singh_Resume_Hybrid.pdf", "rb").read(),
                           file_name="Nikita_Singh_Resume_Hybrid.pdf")

# -------------------------------
# Projects Section
# -------------------------------
elif section == "Projects":
    st.header("🚀 Projects")
    st.write("""
    - **Educator Registry** → Role-based modules (ColdFusion, SQL, QA tested).  
    - **Transcript Viewer** → Dynamic program-user linkage validation.  
    - **FoodBuy Portal** → Backend APIs, integration & regression testing.  
    - **Program Management Tool** → Automated staff assignment.  
    - **Conversational Q&A Chatbot** → Built with LangChain + Streamlit.  
    - **RAG Document Q&A** → Implemented with HuggingFace & FAISS.  
    """)

# -------------------------------
# Contact Section
# -------------------------------
elif section == "Contact":
    st.header("📬 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("✅ Thanks! Your message has been sent.")
