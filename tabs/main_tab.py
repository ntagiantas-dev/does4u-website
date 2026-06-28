import streamlit as st
from utils.spyros_bot import SpyrosBot


def render_main_tab():
    """Landing page with hero + features + Spyros chat"""
    
    # ============================================
    # CUSTOM CSS - Python Colors
    # ============================================
    st.markdown("""
    <style>
        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, #3776ab 0%, #1e3a5f 100%);
            color: white;
            padding: 80px 40px;
            text-align: center;
            border-bottom: 8px solid #FFD43B;
            border-radius: 12px;
            margin-bottom: 40px;
        }
        
        .hero h1 {
            font-size: 3.5em;
            font-weight: 900;
            margin-bottom: 10px;
            letter-spacing: -2px;
        }
        
        .hero p {
            font-size: 1.3em;
            opacity: 0.95;
            margin-bottom: 30px;
        }
        
        .hero .accent {
            color: #FFD43B;
            font-weight: bold;
        }
        
        /* Feature Cards */
        .feature-card {
            background: white;
            border: 3px solid #3776ab;
            border-radius: 12px;
            padding: 30px;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            height: 100%;
        }
        
        .feature-card:hover {
            transform: translateY(-8px);
            border-color: #FFD43B;
            box-shadow: 0 12px 20px rgba(55, 118, 171, 0.2);
        }
        
        .feature-card .emoji {
            font-size: 3em;
            margin-bottom: 15px;
        }
        
        .feature-card h3 {
            color: #3776ab;
            font-size: 1.3em;
            margin-bottom: 15px;
            font-weight: 700;
        }
        
        .feature-card p {
            color: #555;
            font-size: 0.95em;
            line-height: 1.6;
        }
        
        /* Chat Container */
        .chat-container {
            background: white;
            border-left: 8px solid #3776ab;
            border-radius: 8px;
            padding: 25px;
            margin-top: 40px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
        
        .chat-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 3px solid #FFD43B;
        }
        
        .chat-header h2 {
            color: #3776ab;
            margin: 0;
            font-size: 1.5em;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # ============================================
    # STATE MANAGEMENT
    # ============================================
    if "show_spyros_chat" not in st.session_state:
        st.session_state.show_spyros_chat = False
    
    if "spyros_messages" not in st.session_state:
        st.session_state.spyros_messages = []
    
    if "spyros" not in st.session_state:
        try:
            st.session_state.spyros = SpyrosBot(api_key=st.secrets["OPENAI_API_KEY"])
        except:
            st.session_state.spyros = None
    
    # ============================================
    # HERO SECTION
    # ============================================
    st.markdown("""
    <div class="hero">
        <h1>🤖 Does4U</h1>
        <p>Automation Solutions for Small Business</p>
        <p style="font-size: 1em; opacity: 0.9;">We automate repetitive tasks using <span class="accent">Python, AI</span> and custom integrations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================
    # FEATURES SECTION
    # ============================================
    st.markdown("## What We Can Automate")
    
    features = [
        {
            "emoji": "🕷️",
            "title": "Web Scraping",
            "desc": "Collect data from websites automatically and keep your database updated in real-time"
        },
        {
            "emoji": "📊",
            "title": "Excel & Reporting",
            "desc": "Automated Excel generation with formatted reports, charts, and real-time data exports"
        },
        {
            "emoji": "💾",
            "title": "Data Collection",
            "desc": "Gather leads, customer info, and business data from multiple sources effortlessly"
        },
        {
            "emoji": "🧠",
            "title": "AI Workflows",
            "desc": "ChatGPT-powered automation for content generation, analysis, and intelligent processing"
        },
        {
            "emoji": "⚙️",
            "title": "Custom Python Scripts",
            "desc": "Tailored solutions for your specific business needs, built and maintained by experts"
        }
    ]
    
    # Create feature cards in columns
    cols = st.columns(3)
    for idx, feature in enumerate(features):
        col_idx = idx % 3
        with cols[col_idx]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="emoji">{feature['emoji']}</div>
                <h3>{feature['title']}</h3>
                <p>{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        if col_idx == 2 and idx < len(features) - 1:
            cols = st.columns(3)
    
    # ============================================
    # CTA SECTION
    # ============================================
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h2 style='color: #3776ab; text-align: center; margin-bottom: 20px;'>Ready to Automate?</h2>", unsafe_allow_html=True)
        
        if st.button("💬 Chat with Spyros", key="open_spyros", use_container_width=True):
            st.session_state.show_spyros_chat = True
            st.rerun()
    
    # ============================================
    # SPYROS CHAT SECTION
    # ============================================
    if st.session_state.show_spyros_chat:
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
        
        # Chat header with close button
        col_title, col_close = st.columns([4, 1])
        with col_title:
            st.markdown("<div class='chat-header'><h2>🤖 Spyros - Pre-Sales AI Assistant</h2>", unsafe_allow_html=True)
        with col_close:
            if st.button("✕ Close", key="close_spyros"):
                st.session_state.show_spyros_chat = False
                st.session_state.spyros_messages = []
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Display chat messages
        if st.session_state.spyros and len(st.session_state.spyros_messages) > 0:
            for message in st.session_state.spyros_messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
        elif st.session_state.spyros is None:
            st.error("⚠️ Could not initialize Spyros. Check your OPENAI_API_KEY in Streamlit secrets.")
        
        # Chat input
        if st.session_state.spyros:
            if user_input := st.chat_input("Tell me about your business needs..."):
                # Add user message
                st.session_state.spyros_messages.append({"role": "user", "content": user_input})
                
                with st.chat_message("user"):
                    st.markdown(user_input)
                
                # Get Spyros response
                with st.chat_message("assistant"):
                    with st.spinner("Spyros is thinking..."):
                        try:
                            response = st.session_state.spyros.chat(user_input)
                            st.markdown(response)
                            st.session_state.spyros_messages.append({"role": "assistant", "content": response})
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
        
        st.markdown("</div>", unsafe_allow_html=True)


# ============================================
# EXPORT FUNCTION
# ============================================
if __name__ == "__main__":
    render_main_tab()