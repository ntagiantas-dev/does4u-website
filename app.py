import streamlit as st
from tabs.main_tab import render_main_tab
from tabs.blog_tab import render_blog_tab
from tabs.demos_tab import render_demos_tab
from tabs.admin_tab import render_admin_tab

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
    
    /* Admin unlock form styling */
    .admin-unlock-form {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: white;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        z-index: 999;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# ADMIN UNLOCK SYSTEM
# ============================================

# Initialize session state for admin access
if "admin_unlocked" not in st.session_state:
    st.session_state.admin_unlocked = False

def check_admin_password(password: str) -> bool:
    """Check if password matches the admin password from secrets"""
    try:
        admin_password = st.secrets.get("ADMIN_PASSWORD", "")
        return password == admin_password and password != ""
    except:
        return False

# Hidden admin unlock form (bottom right corner)
with st.container():
    st.markdown("""
    <div style="position: fixed; bottom: 20px; right: 20px; background: white; padding: 15px; 
    border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); z-index: 999;">
    """, unsafe_allow_html=True)
    
    # Compact unlock form
    col1, col2 = st.columns([2, 1])
    with col1:
        admin_pass = st.text_input(
            "🔐",
            type="password",
            placeholder="Admin access",
            label_visibility="collapsed",
            key="admin_password_input"
        )
    
    with col2:
        if st.button("🔓", key="admin_unlock_btn", help="Unlock admin panel"):
            if check_admin_password(admin_pass):
                st.session_state.admin_unlocked = True
                st.success("✅ Admin unlocked!")
                st.rerun()
            else:
                st.error("❌ Wrong password")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================
# MAIN APP - DYNAMIC TABS
# ============================================

# Build tabs list based on admin status
tabs_list = [
    "🏠 Main",
    "📰 Blog", 
    "🎯 Demos"
]

# Add admin tab only if unlocked
if st.session_state.admin_unlocked:
    tabs_list.append("⚙️ Admin")

# Create tabs
tabs = st.tabs(tabs_list)

# Render tabs based on admin status
with tabs[0]:
    render_main_tab()

with tabs[1]:
    render_blog_tab()

with tabs[2]:
    render_demos_tab()

# Admin tab only visible if unlocked
if st.session_state.admin_unlocked and len(tabs_list) == 4:
    with tabs[3]:
        render_admin_tab()

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