import streamlit as st


def render_demos_tab():
    """Demos page showcasing 5 automation solutions"""
    
    # ============================================
    # CUSTOM CSS
    # ============================================
    st.markdown("""
    <style>
        .demo-card {
            background: white;
            border: 3px solid #3776ab;
            border-radius: 12px;
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        .demo-card:hover {
            border-color: #FFD43B;
            box-shadow: 0 8px 20px rgba(55, 118, 171, 0.2);
        }
        
        .demo-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .demo-emoji {
            font-size: 2.5em;
        }
        
        .demo-title {
            color: #3776ab;
            font-weight: 700;
            font-size: 1.5em;
            margin: 0;
        }
        
        .demo-video-placeholder {
            background: #f0f0f0;
            border: 2px dashed #3776ab;
            border-radius: 8px;
            padding: 60px 20px;
            text-align: center;
            margin: 20px 0;
            color: #999;
            font-weight: bold;
        }
        
        .demo-description {
            color: #555;
            font-size: 1.05em;
            line-height: 1.7;
            margin: 15px 0;
        }
        
        .demo-tech {
            background: #f8f8f8;
            border-left: 4px solid #FFD43B;
            padding: 15px;
            border-radius: 4px;
            margin: 15px 0;
            font-size: 0.95em;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # ============================================
    # HEADER
    # ============================================
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #3776ab; font-weight: 800; font-size: 2.8rem;">🎯 Live Automation Demos</h1>
        <p style="color: #666; font-size: 1.1rem;">See how Does4U transforms repetitive tasks into automated workflows</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================
    # DEMO 1: Web Scraping
    # ============================================
    with st.container():
        st.markdown("""
        <div class="demo-card">
            <div class="demo-header">
                <span class="demo-emoji">🕷️</span>
                <h2 class="demo-title">Web Scraping</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            st.markdown("""
            <div class="demo-video-placeholder">
                📹 Video Demo<br>
                <small>(10-15 seconds)</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="demo-description">
            <strong>Αυτοματοποίηση συλλογής δεδομένων από ιστοσελίδες</strong>
            </div>
            
            Χρησιμοποιούμε Python web scraping για να συλλέγουμε δεδομένα από 
            ιστοσελίδες αυτόματα. Ιδανικό για:
            
            • Συλλογή leads από directories  
            • Παρακολούθηση τιμών ανταγωνιστών  
            • Τραβήγματα δεδομένων ακίνητων  
            • Aggregation news & content  
            
            <div class="demo-tech">
            <strong>🛠️ Technologies:</strong> BeautifulSoup, Selenium, SerpAPI, Tavily
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # ============================================
    # DEMO 2: Excel & Reporting
    # ============================================
    with st.container():
        st.markdown("""
        <div class="demo-card">
            <div class="demo-header">
                <span class="demo-emoji">📊</span>
                <h2 class="demo-title">Excel & Reporting</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            st.markdown("""
            <div class="demo-video-placeholder">
                📹 Video Demo<br>
                <small>(10-15 seconds)</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="demo-description">
            <strong>Αυτόματη δημιουργία Excel reports με formatting</strong>
            </div>
            
            Δημιουργούμε όμορφα, επαγγελματικά Excel αρχεία με χρώματα, 
            γραφήματα και live δεδομένα. Αποστέλλονται αυτόματα ή on-demand:
            
            • Daily/Weekly automated reports  
            • Lead scoring spreadsheets  
            • Sales performance dashboards  
            • Data export με conditional formatting  
            
            <div class="demo-tech">
            <strong>🛠️ Technologies:</strong> OpenPyXL, Pandas, XlsxWriter, Openpyxl
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # ============================================
    # DEMO 3: Data Collection
    # ============================================
    with st.container():
        st.markdown("""
        <div class="demo-card">
            <div class="demo-header">
                <span class="demo-emoji">💾</span>
                <h2 class="demo-title">Data Collection & Aggregation</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            st.markdown("""
            <div class="demo-video-placeholder">
                📹 Video Demo<br>
                <small>(10-15 seconds)</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="demo-description">
            <strong>Συγκέντρωση δεδομένων από πολλαπλές πηγές</strong>
            </div>
            
            Συλλέγουμε δεδομένα από Google Maps, LinkedIn, directories, 
            websites και ενοποιούμε τα σε μια ενιαία βάση δεδομένων:
            
            • Google Business Profiles scraping  
            • LinkedIn lead extraction  
            • Business directory aggregation  
            • Real-time data deduplication  
            
            <div class="demo-tech">
            <strong>🛠️ Technologies:</strong> SerpAPI, Tavily, Google Maps API, Custom APIs
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # ============================================
    # DEMO 4: AI Workflows (Spyros)
    # ============================================
    with st.container():
        st.markdown("""
        <div class="demo-card">
            <div class="demo-header">
                <span class="demo-emoji">🧠</span>
                <h2 class="demo-title">AI Workflows & Automation</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            st.markdown("""
            <div class="demo-video-placeholder">
                📹 Video Demo<br>
                <small>(10-15 seconds)</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="demo-description">
            <strong>ChatGPT-powered automation workflows</strong>
            </div>
            
            Χρησιμοποιούμε OpenAI GPT-4o-mini για έξυπνη αυτοματοποίηση:
            
            • AI lead qualification  
            • Automated email drafting  
            • Content generation at scale  
            • Customer support automation  
            • Pre-sales chatbot (Spyros)  
            
            <div class="demo-tech">
            <strong>🛠️ Technologies:</strong> OpenAI GPT-4o-mini, Streamlit, Custom Prompts
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # ============================================
    # DEMO 5: Custom Python Scripts
    # ============================================
    with st.container():
        st.markdown("""
        <div class="demo-card">
            <div class="demo-header">
                <span class="demo-emoji">⚙️</span>
                <h2 class="demo-title">Custom Python Scripts</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            st.markdown("""
            <div class="demo-video-placeholder">
                📹 Video Demo<br>
                <small>(10-15 seconds)</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="demo-description">
            <strong>Εξειδικευμένα scripts για τις δικές σας ανάγκες</strong>
            </div>
            
            Δημιουργούμε custom Python solutions που δουλεύουν με τα 
            συστήματα και τις διαδικασίες σας:
            
            • API integrations  
            • Database automation  
            • File processing pipelines  
            • Scheduled tasks & bots  
            • Monitored workflows  
            
            <div class="demo-tech">
            <strong>🛠️ Technologies:</strong> Python 3.x, Requests, SQLAlchemy, Celery, APScheduler
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # ============================================
    # CTA SECTION
    # ============================================
    st.markdown("""
    <div style="background: linear-gradient(135deg, #3776ab 0%, #1e3a5f 100%); 
                color: white; padding: 40px; border-radius: 12px; text-align: center; margin-top: 40px;">
        <h2 style="margin-top: 0; color: white;">Ready to See More?</h2>
        <p style="font-size: 1.1rem; opacity: 0.95;">
            Each demo can be customized for your specific business needs.
        </p>
        <p style="font-size: 0.95rem; opacity: 0.85;">
            Contact us through the Main tab's "Chat with Spyros" to discuss your automation requirements.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ============================================
# EXPORT FUNCTION
# ============================================
if __name__ == "__main__":
    render_demos_tab()