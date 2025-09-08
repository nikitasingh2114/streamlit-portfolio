import streamlit as st
import base64

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Nikita Singh | Portfolio", layout="wide")

# -------------------------------
# HELPER FUNCTION TO DISPLAY PDF
# -------------------------------
def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.title("💼 Nikita Singh")
st.write("📍 New Delhi, India | 📧 nikitasingh2114@gmail.com | 📞 +91 9140092337")
st.write("🔗 [LinkedIn](https://linkedin.com/in/nikita-singh-015a42192) | "
         "🔗 [GitHub](https://github.com/nikitasingh2114)")
st.markdown("---")

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
st.sidebar.title("📂 Portfolio Sections")
section = st.sidebar.radio("Go to:", ["Home", "Resume", "Projects", "Contact"])

# -------------------------------
# HOME SECTION
# -------------------------------
if section == "Home":
    st.header("👋 Welcome to My Portfolio")
    st.write("""
    I am a versatile professional with experience as a **QA Engineer, Full Stack Developer, 
    and Hybrid QA-Dev**.  
    Skilled in **ColdFusion, JavaScript, SQL, Manual Testing, API Testing, and Generative AI 
    (LangChain, HuggingFace, Streamlit, AWS Bedrock)**.  
    Passionate about building **scalable applications** and ensuring **quality through rigorous testing**.
    """)

# -------------------------------
# RESUME SECTION
# -------------------------------
elif section == "Resume":
    st.header("📄 My Resume")

    option = st.selectbox(
        "Select Resume to View:",
        ["QA Engineer", "Full Stack Developer", "Hybrid (QA + Dev)"]
    )

    if option == "QA Engineer":
        st.subheader("QA Engineer Resume")
        display_pdf("Nikita_Singh_Resume_QA.pdf")
        st.download_button("⬇️ Download QA Resume",
                           data=open("Nikita_Singh_Resume_QA.pdf", "rb").read(),
                           file_name="Nikita_Singh_Resume_QA.pdf")

    elif option == "Full Stack Developer":
        st.subheader("Full Stack Developer Resume")
        display_pdf("Nikita_Singh_Resume_Developer.pdf")
        st.download_button("⬇️ Download Developer Resume",
                           data=open("Nikita_Singh_Resume_Developer.pdf", "rb").read(),
                           file_name="Nikita_Singh_Resume_Developer.pdf")

    elif option == "Hybrid (QA + Dev)":
        st.subheader("Hybrid Resume")
        display_pdf("Nikita_Singh_Resume_Hybrid.pdf")
        st.download_button("⬇️ Download Hybrid Resume",
                           data=open("Nikita_Singh_Resume_Hybrid.pdf", "rb").read(),
                           file_name="Nikita_Singh_Resume_Hybrid.pdf")

# -------------------------------
# PROJECTS SECTION
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
# CONTACT SECTION
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
