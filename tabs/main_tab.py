import streamlit as st
from utils.email_service import EmailService


def render_main_tab():
    """Landing page with hero + features + lead capture form"""
    
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
        
        /* Welcome Section */
        .welcome-box {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-left: 6px solid #FFD43B;
            border-radius: 8px;
            padding: 25px;
            margin: 30px 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        
        .welcome-box h2 {
            color: #3776ab;
            font-size: 1.4em;
            margin-bottom: 12px;
            margin-top: 0;
        }
        
        .welcome-box p {
            color: #555;
            font-size: 1em;
            line-height: 1.6;
            margin: 8px 0;
        }
        
        /* Progress Tracker */
        .progress-tracker {
            background: white;
            border: 2px solid #3776ab;
            border-radius: 8px;
            padding: 20px;
            margin: 25px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        
        .progress-tracker h3 {
            color: #3776ab;
            font-size: 1.1em;
            margin-bottom: 15px;
            margin-top: 0;
            font-weight: 700;
        }
        
        .tracker-item {
            display: flex;
            align-items: center;
            padding: 8px 0;
            font-size: 0.95em;
        }
        
        .tracker-status {
            display: inline-block;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 12px;
            font-weight: bold;
            text-align: center;
            line-height: 20px;
            font-size: 0.8em;
        }
        
        .status-empty {
            background-color: #e74c3c;
            color: white;
        }
        
        .status-filled {
            background-color: #27ae60;
            color: white;
        }
        
        .tracker-label {
            color: #555;
        }
        
        .tracker-label .required {
            color: #e74c3c;
            font-weight: bold;
        }
        
        /* Form Container */
        .form-container {
            background: white;
            border-left: 8px solid #3776ab;
            border-radius: 8px;
            padding: 30px;
            margin-top: 40px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
        
        .form-title {
            color: #3776ab;
            font-weight: 700;
            font-size: 1.5em;
            margin-bottom: 20px;
            border-bottom: 3px solid #FFD43B;
            padding-bottom: 15px;
        }
        
        .form-section {
            margin: 20px 0;
        }
        
        .form-section-title {
            color: #3776ab;
            font-weight: 700;
            font-size: 1.1em;
            margin: 25px 0 15px 0;
            border-bottom: 2px solid #e9ecef;
            padding-bottom: 10px;
        }
        
        .required-asterisk {
            color: #e74c3c;
            font-weight: bold;
        }
        
        .form-hint {
            color: #999;
            font-size: 0.85em;
            margin-top: 5px;
            font-style: italic;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # ============================================
    # STATE MANAGEMENT
    # ============================================
    if "form_submitted" not in st.session_state:
        st.session_state.form_submitted = False
    
    if "form_data" not in st.session_state:
        st.session_state.form_data = None
    
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
    # WELCOME SECTION
    # ============================================
    st.markdown("""
    <div class="welcome-box">
        <h2>👋 Welcome!</h2>
        <p>Great to meet you! We understand that running a business means dealing with repetitive, time-consuming tasks. Whether it's copying data between systems, generating reports, or managing leads – we've got solutions.</p>
        <p><strong>Here's how we work:</strong></p>
        <p><strong>Step 1 - You Tell Us Your Problem:</strong> Fill out this form with details about your automation needs and current workflow<br>
        <strong>Step 2 - We Review & Analyze:</strong> Our team carefully evaluates your specific situation to understand the scope and requirements<br>
        <strong>Step 3 - Custom Solution:</strong> We design and implement a tailored automation solution perfectly fitted to YOUR needs</p>
        <p style="margin-bottom: 0;"><em>Let's get started! Please fill in the form below so we can provide you with an accurate quote and timeline.</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================
    # LEAD CAPTURE FORM
    # ============================================
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    st.markdown("<div class='form-title'>📋 Let's Get Started</div>", unsafe_allow_html=True)
    
    # Initialize form state tracking
    if "form_values" not in st.session_state:
        st.session_state.form_values = {
            "name": "",
            "email": "",
            "company": "",
            "problem": "",
            "current": "",
            "desired": "",
            "volume": ""
        }
    
    with st.form("lead_form", clear_on_submit=False):
        # ============================================
        # PROGRESS TRACKER
        # ============================================
        st.markdown("<div class='progress-tracker'>", unsafe_allow_html=True)
        st.markdown("<h3>📊 Form Progress</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #666; font-size: 0.9em; margin-top: -10px;'>Fill in all required fields so we can give you an accurate quote</p>", unsafe_allow_html=True)
        
        # Collect values for tracking (temporary, just for display)
        tracker_items = [
            ("name", "👤 Full Name"),
            ("email", "📧 Email Address"),
            ("company", "🏢 Company Name"),
            ("problem", "🎯 Problem Description"),
            ("current", "⚙️ Current Process"),
            ("desired", "✨ Desired Outcome"),
            ("volume", "📈 Data Volume")
        ]
        
        for field_key, field_label in tracker_items:
            status_icon = "✓"
            status_class = "status-filled"
            label_color = "color: #27ae60;"
        
            st.markdown(f"""
            <div class="tracker-item">
                <div class="tracker-status {status_class}">{status_icon}</div>
                <div class="tracker-label" style="{label_color}">{field_label} <span class="required">*</span></div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # ============================================
        # CONTACT INFORMATION SECTION
        # ============================================
        st.markdown("<div class='form-section-title'>👤 Contact Information</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input(
                "Full Name *",
                placeholder="John Doe",
                key="form_name"
            )
        
        with col2:
            email = st.text_input(
                "Email Address *",
                placeholder="john@company.com",
                key="form_email"
            )
        
        company = st.text_input(
            "Company Name *",
            placeholder="Your Company",
            key="form_company"
        )
        
        # ============================================
        # PROBLEM & SOLUTION SECTION
        # ============================================
        st.markdown("<div class='form-section-title'>🎯 Problem & Solution</div>", unsafe_allow_html=True)
        st.markdown("<p style='color: #666; font-size: 0.9em; margin-top: -10px;'>Help us understand your specific automation challenge in detail</p>", unsafe_allow_html=True)
        
        problem = st.text_area(
            "What problem do you want to automate? *",
            placeholder="Describe the repetitive task or problem you face...",
            height=100,
            key="form_problem"
        )
        st.markdown("<p class='form-hint'>💡 Example: We manually copy customer data from emails into Excel daily</p>", unsafe_allow_html=True)
        
        current = st.text_area(
            "How does it work now? (current process) *",
            placeholder="Briefly describe your current manual process...",
            height=80,
            key="form_current"
        )
        st.markdown("<p class='form-hint'>💡 Example: Sales team receives emails and manually updates spreadsheet</p>", unsafe_allow_html=True)
        
        desired = st.text_area(
            "What should happen automatically? (desired outcome) *",
            placeholder="Describe your ideal automated outcome...",
            height=80,
            key="form_desired"
        )
        st.markdown("<p class='form-hint'>💡 Example: Data goes directly from email to Excel sheet without manual work</p>", unsafe_allow_html=True)
        
        # ============================================
        # TECHNICAL DETAILS SECTION
        # ============================================
        st.markdown("<div class='form-section-title'>🔧 Technical Details</div>", unsafe_allow_html=True)
        
        websites = st.text_input(
            "Websites involved (comma-separated)",
            placeholder="example.com, site2.com",
            key="form_websites"
        )
        
        documents = st.text_input(
            "Document types involved (Excel, PDF, etc.)",
            placeholder="Excel, PDF, CSV",
            key="form_documents"
        )
        
        volume = st.text_input(
            "Estimated data volume *",
            placeholder="e.g., 1000 records/day, 500 files/month",
            key="form_volume"
        )
        st.markdown("<p class='form-hint'>💡 This helps us understand the scale and choose the right solution</p>", unsafe_allow_html=True)
        
        # ============================================
        # ADDITIONAL NOTES SECTION
        # ============================================
        st.markdown("<div class='form-section-title'>📝 Additional Information</div>", unsafe_allow_html=True)
        
        notes = st.text_area(
            "Anything else we should know? (optional)",
            placeholder="Any additional context or requirements...",
            height=80,
            key="form_notes"
        )
        
        # ============================================
        # SUBMIT BUTTON
        # ============================================
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button("📤 Submit & Send Report", use_container_width=True)
        
        # ============================================
        # FORM VALIDATION & SUBMISSION
        # ============================================
        if submitted:
            # Validation
            errors = []
            
            if not name or name.strip() == "":
                errors.append("❌ Full Name is required")
            if not email or email.strip() == "" or "@" not in email:
                errors.append("❌ Valid Email is required")
            if not company or company.strip() == "":
                errors.append("❌ Company Name is required")
            if not problem or problem.strip() == "":
                errors.append("❌ Problem Description is required")
            if not current or current.strip() == "":
                errors.append("❌ Current Process is required")
            if not desired or desired.strip() == "":
                errors.append("❌ Desired Outcome is required")
            if not volume or volume.strip() == "":
                errors.append("❌ Estimated Volume is required")
            
            # Show errors
            if errors:
                st.error("⚠️ Please fix the following errors:")
                for error in errors:
                    st.error(error)
            
            # Submit if valid
            else:
                form_data = {
                    "name": name.strip(),
                    "email": email.strip(),
                    "company": company.strip(),
                    "problem_description": problem.strip(),
                    "current_process": current.strip(),
                    "desired_outcome": desired.strip(),
                    "websites": [w.strip() for w in websites.split(",") if w.strip()],
                    "documents": [d.strip() for d in documents.split(",") if d.strip()],
                    "estimated_volume": volume.strip(),
                    "additional_notes": notes.strip() if notes else ""
                }
                
                # Send email
                email_service = EmailService()
                success, message = email_service.send_report(form_data)
                
                if success:
                    st.success("✅ " + message)
                    st.info("📧 We've received your information. Our team will review your needs and contact you with a customized quote.")
                    st.session_state.form_submitted = True
                else:
                    st.error("❌ " + message)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # ============================================
    # FOOTER NOTE
    # ============================================
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #999; font-size: 0.9em; padding: 20px;">
        <p>🔒 Your information is secure and will only be used to discuss your automation needs.</p>
        <p>Questions? Reach out to us at <strong>does4u.ceo@gmail.com</strong></p>
    </div>
    """, unsafe_allow_html=True)


# ============================================
# EXPORT FUNCTION
# ============================================
if __name__ == "__main__":
    render_main_tab()