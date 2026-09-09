import streamlit as st
import tempfile
import os

from src.classifier import WasteClassifier
from src.recommendations import WasteRecommendation
from src.sustainability import SustainabilityImpact


# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="EcoSort AI",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================
# CUSTOM CSS - APPLICATION DESIGN
# =========================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f4fbf5, #e8f5e9);
    }

    /* Main title */
    .main-title {
        font-size: 55px;
        font-weight: 800;
        color: #14532d;
        text-align: center;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        font-size: 22px;
        color: #4b5563;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Hero section */
    .hero-box {
        background: linear-gradient(135deg, #166534, #22c55e);
        padding: 45px;
        border-radius: 25px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
    }

    /* Cards */
    .eco-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        min-height: 170px;
        margin-bottom: 20px;
    }

    /* Card headings */
    .eco-card h3 {
        color: #166534;
    }

    /* Section titles */
    .section-title {
        color: #14532d;
        font-size: 32px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #14532d;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        background-color: #16a34a;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 12px;
        font-size: 18px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #15803d;
        color: white;
        border: none;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #22c55e;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    }

</style>
""", unsafe_allow_html=True)


# =========================================
# LOAD AI COMPONENTS
# =========================================

@st.cache_resource
def load_components():

    classifier = WasteClassifier()
    recommender = WasteRecommendation()
    impact_analyzer = SustainabilityImpact()

    return classifier, recommender, impact_analyzer


classifier, recommender, impact_analyzer = load_components()


# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.markdown("# ♻️ EcoSort AI")

    st.caption("Smart Waste. Smarter Future. 🌱")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "📷 Scan Waste",
            "🌱 Sustainability",
            "ℹ️ About"
        ]
    )

    st.divider()

    st.markdown("### 🌍 Our Mission")

    st.caption(
        "Using Artificial Intelligence to support "
        "responsible waste management."
    )

    st.divider()

    st.caption("Supporting UN SDG 12 ♻️")


# =========================================
# HOME PAGE
# =========================================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="hero-box">
            <h1>♻️ EcoSort AI</h1>
            <h2>Smart Waste. Smarter Future. 🌱</h2>
            <p style="font-size:18px;">
                Identify waste items using Artificial Intelligence
                and discover how to dispose of them responsibly.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">✨ Why EcoSort AI?</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="eco-card">
                <h3>🤖 AI Powered</h3>
                <p>
                Uses YOLO and Vision Transformer
                models to identify waste objects.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="eco-card">
                <h3>♻️ Smart Sorting</h3>
                <p>
                Provides waste categories and
                responsible disposal guidance.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="eco-card">
                <h3>🌍 Sustainable</h3>
                <p>
                Supports responsible consumption
                and UN Sustainable Development Goal 12.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">🔄 How It Works</div>',
        unsafe_allow_html=True
    )

    step1, step2, step3 = st.columns(3)

    with step1:

        st.markdown(
            """
            <div class="eco-card">
                <h3>1️⃣ Upload</h3>
                <p>
                Upload an image of your waste item.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with step2:

        st.markdown(
            """
            <div class="eco-card">
                <h3>2️⃣ AI Analysis</h3>
                <p>
                EcoSort AI identifies the object
                using a hybrid AI workflow.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with step3:

        st.markdown(
            """
            <div class="eco-card">
                <h3>3️⃣ Dispose Smartly</h3>
                <p>
                Get responsible disposal and
                sustainability guidance.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">🌱 Make Every Disposal Count</div>',
        unsafe_allow_html=True
    )

    st.info(
        "♻️ Small waste decisions can create a big "
        "environmental impact. EcoSort AI helps you "
        "make more informed choices."
    )


# =========================================
# SCAN WASTE PAGE
# =========================================

elif page == "📷 Scan Waste":

    st.markdown(
        '<div class="main-title">📷 Scan Your Waste</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Upload an image and let AI help you understand '
        'how your waste should be handled.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "📷 Choose your waste image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        col1, col2 = st.columns([1, 1])

        with col1:

            st.image(
                uploaded_file,
                caption="Your Waste Item",
                use_container_width=True
            )

        with col2:

            st.markdown(
                """
                <div class="eco-card">
                    <h3>🤖 Ready for AI Analysis</h3>
                    <p>
                    EcoSort AI will identify your object,
                    provide waste guidance and show its
                    sustainability impact.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            analyze = st.button(
                "✨ Analyze with EcoSort AI"
            )


        if analyze:

            with st.spinner(
                "🤖 EcoSort AI is analyzing your image..."
            ):

                suffix = os.path.splitext(
                    uploaded_file.name
                )[1]

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                ) as temp_file:

                    temp_file.write(
                        uploaded_file.getvalue()
                    )

                    image_path = temp_file.name


                results = classifier.classify(
                    image_path
                )


            st.success("🎉 Analysis Complete!")

            st.markdown(
                '<div class="section-title">'
                '📊 Your AI Results'
                '</div>',
                unsafe_allow_html=True
            )


            for item in results:

                object_name = item["object"]

                confidence = item["confidence"]

                source = item.get(
                    "source",
                    "AI Model"
                )


                recommendation = (
                    recommender.get_recommendation(
                        object_name
                    )
                )


                impact = (
                    impact_analyzer.get_impact(
                        recommendation["category"]
                    )
                )


                # RESULTS METRICS

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "🤖 Detected Object",
                        object_name.title()
                    )

                with col2:

                    st.metric(
                        "🎯 AI Confidence",
                        f"{confidence}%"
                    )

                with col3:

                    st.metric(
                        "🧠 AI Model",
                        source
                    )


                st.write("")


                # DISPOSAL GUIDE

                st.markdown(
                    '<div class="section-title">'
                    '♻️ Disposal Guide'
                    '</div>',
                    unsafe_allow_html=True
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.info(
                        f"""
                        ♻️ **Waste Category**

                        {recommendation['category']}
                        """
                    )

                with col2:

                    st.warning(
                        f"""
                        🗑️ **Correct Disposal**

                        {recommendation['bin']}
                        """
                    )


                st.success(
                    f"💡 {recommendation['recommendation']}"
                )


                # SUSTAINABILITY

                st.markdown(
                    '<div class="section-title">'
                    '🌱 Sustainability Impact'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.success(
                    impact["impact"]
                )

                st.info(
                    f"🌍 **SDG Alignment:** {impact['sdg']}"
                )


            if os.path.exists(image_path):

                os.remove(image_path)


    else:

        st.info(
            "👆 Upload an image to start your AI-powered "
            "waste analysis."
        )


# =========================================
# SUSTAINABILITY PAGE
# =========================================

elif page == "🌱 Sustainability":

    st.markdown(
        '<div class="main-title">🌱 Sustainability</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Better waste decisions for a healthier planet.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">'
        '♻️ The 3Rs of Sustainable Living'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="eco-card">
                <h3>♻️ Reduce</h3>
                <p>
                Reduce unnecessary consumption
                and avoid generating waste.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="eco-card">
                <h3>🔄 Reuse</h3>
                <p>
                Reuse products whenever possible
                before disposing of them.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="eco-card">
                <h3>♻️ Recycle</h3>
                <p>
                Help valuable materials return
                to the production cycle.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">'
        '🌍 UN Sustainable Development Goal 12'
        '</div>',
        unsafe_allow_html=True
    )

    st.success(
        """
        SDG 12 promotes Responsible Consumption
        and Production.

        EcoSort AI supports this goal by helping
        users make more informed decisions about
        waste segregation and disposal.
        """
    )


# =========================================
# ABOUT PAGE
# =========================================

elif page == "ℹ️ About":

    st.markdown(
        '<div class="main-title">ℹ️ About EcoSort AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-box">
            <h2>AI for Sustainable Waste Management</h2>
            <p>
            EcoSort AI combines Artificial Intelligence
            and sustainability to help users make better
            waste disposal decisions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">'
        '🤖 AI Technologies'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="eco-card">
        <h3>🧠 Hybrid AI Workflow</h3>

        <p>🤖 YOLO Object Detection</p>

        <p>🧠 Vision Transformer Image Classification</p>

        <p>♻️ Rule-Based Waste Recommendation Engine</p>

        <p>🌱 Sustainability Impact Analysis</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">'
        '🛡️ Responsible AI'
        '</div>',
        unsafe_allow_html=True
    )

    st.warning(
        """
        EcoSort AI provides decision support for waste
        segregation.

        AI predictions may be uncertain, especially when
        an item's material cannot be reliably identified
        from an image.

        Users should manually verify uncertain items
        before disposal.
        """
    )

    st.markdown(
        '<div class="section-title">'
        '🎯 Our Goal'
        '</div>',
        unsafe_allow_html=True
    )

    st.success(
        """
        To demonstrate how Artificial Intelligence
        can support sustainable communities and
        responsible waste management.
        """
    )


# =========================================
# FOOTER
# =========================================

st.divider()

st.caption(
    "♻️ EcoSort AI  |  AI for Sustainable Waste Management  |  Supporting SDG 12 🌍"
)