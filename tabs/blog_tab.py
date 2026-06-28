import streamlit as st
import json
import os
from datetime import datetime


def render_blog_tab():
    """Blog page with posts, categories and newsletter"""
    
    # ============================================
    # CUSTOM CSS
    # ============================================
    st.markdown("""
    <style>
        .category-tag {
            background-color: #3776ab;
            color: white;
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.75rem;
            font-weight: bold;
            text-transform: uppercase;
        }
        
        .post-container {
            background: white;
            border-left: 5px solid #3776ab;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .post-title {
            color: #3776ab;
            font-weight: 700;
            font-size: 1.4em;
            margin: 10px 0;
        }
        
        .post-meta {
            color: #999;
            font-size: 0.9em;
            margin-bottom: 15px;
        }
        
        .newsletter-box {
            background: linear-gradient(135deg, #3776ab 0%, #1e3a5f 100%);
            color: white;
            padding: 30px;
            border-radius: 12px;
            margin: 30px 0;
            text-align: center;
        }
        
        .newsletter-box h3 {
            margin-top: 0;
            font-size: 1.5em;
        }
        
        .newsletter-box p {
            opacity: 0.95;
            margin-bottom: 15px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # ============================================
    # LOAD POSTS FROM JSON
    # ============================================
    def load_posts():
        if os.path.exists("blog_data.json"):
            try:
                with open("blog_data.json", "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []
    
    # ============================================
    # RENDER SINGLE POST
    # ============================================
    def render_post(post):
        with st.container():
            col_img, col_txt = st.columns([1, 2.5])
            
            with col_img:
                img_path = post.get('image', '')
                if img_path and os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.info("📷 Article Image")
            
            with col_txt:
                st.markdown(f'<span class="category-tag">{post.get("category", "Tech & AI")}</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="post-title">{post.get("title", "Untitled")}</div>', unsafe_allow_html=True)
                st.caption(f"📅 {post.get('date', '')} | 🎯 Focus: {post.get('target', 'General')}")
                st.write(post.get('content', ''))
                
                if post.get('teaser'):
                    with st.expander("📱 Copy Social Media Post"):
                        st.code(post['teaser'])
            
            st.divider()
    
    # ============================================
    # HEADER
    # ============================================
    col_blog, col_sidebar = st.columns([4, 1])
    
    with col_blog:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="font-family: 'Segoe UI', sans-serif; font-weight: 800; font-size: 2.8rem; margin-bottom: 5px; line-height: 1.2;">
                <span style="color: #333;">Insights</span> 
                <span style="color: #3776ab;">does</span><span style="color: #FFD43B;">4u</span>
            </h1>
            <p style="color: #666; font-size: 1.1rem; font-style: italic;">
                SaaS Engineering, Advanced Automation & Growth Hacking
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Load posts
        posts = load_posts()
        
        # ============================================
        # TABS: All | Python & AI | Growth Hacking
        # ============================================
        t_all, t_tech, t_growth = st.tabs([
            "🗂️ Όλες οι Αναλύσεις", 
            "💻 Python & AI Updates", 
            "📈 Growth Hacking"
        ])
        
        # TAB 1: All posts
        with t_all:
            if posts:
                for p in posts:
                    render_post(p)
            else:
                st.info("📰 Δεν υπάρχουν ακόμη αναλύσεις.")
        
        # TAB 2: Python & AI
        with t_tech:
            tech_posts = [p for p in posts if "Python" in p.get('category', '') or "AI" in p.get('category', '')]
            if tech_posts:
                for p in tech_posts:
                    render_post(p)
            else:
                st.info("💻 Δεν βρέθηκαν αναλύσεις για Python & AI.")
        
        # TAB 3: Growth Hacking
        with t_growth:
            growth_posts = [p for p in posts if "Growth" in p.get('category', '')]
            if growth_posts:
                for p in growth_posts:
                    render_post(p)
            else:
                st.info("📈 Δεν βρέθηκαν αναλύσεις για Growth Hacking.")
    
    # ============================================
    # SIDEBAR: Newsletter & Promo
    # ============================================
    with col_sidebar:
        st.markdown("### 🚀 Stay Updated")
        
        # Newsletter signup
        st.markdown("""
        <div style="background: linear-gradient(180deg, #3776ab 0%, #1e3a5f 100%); padding: 20px; border-radius: 12px; color: white; text-align: center;">
            <h4 style="margin-top: 0; color: white;">📩 Newsletter</h4>
            <p style="font-size: 0.85rem; opacity: 0.9; line-height: 1.4;">
                Πραγματικές αναλύσεις για Python, Web Scraping και Growth Hacking.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        email = st.text_input("Email", placeholder="info@company.com", key="blog_newsletter_email")
        if st.button("Εγγραφή", use_container_width=True, key="blog_newsletter_btn"):
            if email and "@" in email:
                try:
                    with open("subscribers.txt", "a", encoding="utf-8") as f:
                        f.write(f"{email}\n")
                    st.success("✅ Καλώς ήρθες!")
                except:
                    st.error("❌ Σφάλμα αποθήκευσης.")
            else:
                st.warning("⚠️ Βάλτε ένα έγκυρο email.")
        
        st.divider()
        st.caption("© 2026 Does4U | High-ROI Content")


# ============================================
# EXPORT FUNCTION
# ============================================
if __name__ == "__main__":
    render_blog_tab()