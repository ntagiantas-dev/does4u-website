import streamlit as st
from tabs.main import render_main_tab
from tabs.blog import render_blog_tab
from tabs.demos import render_demos_tab


# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="Does4U | Automation Solutions",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================
# HIDE STREAMLIT DEFAULTS
# ============================================
st.markdown("""
<style>
    /* Hide sidebar collapse button */
    [data-testid="collapsedControl"] { display: none !important; }
    
    /* Hide footer */
    footer { display: none !important; }
    
    /* Smooth transitions */
    .stTabs [role="tab"] {
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# MAIN APP - 3 TABS
# ============================================
tab_main, tab_blog, tab_demos = st.tabs([
    "🏠 Main",
    "📰 Blog", 
    "🎯 Demos"
])

with tab_main:
    render_main_tab()

with tab_blog:
    render_blog_tab()

with tab_demos:
    render_demos_tab()

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #999; font-size: 0.9em; padding: 20px;">
    <p>© 2026 Does4U Automation Agency | Powered by Python, AI & Streamlit</p>
    <p>Email: does4u.ceo@gmail.com</p>
</div>
""", unsafe_allow_html=True)