# 1. Core Setup
import streamlit as st
import time 

# 2. Page Configuration and Title
st.set_page_config(
    page_title="ARCHON: Compliance Detective",
    layout="centered",
)

st.title("🤖 ARCHON: The Compliance Detective")
st.subheader("99.1% Accuracy. Hours vs. Weeks.")

st.markdown("""
ARCHON is designed to rapidly process thousands of documents to detect rule breaches. 
This demo simulates the high-speed, high-accuracy detection engine.
""")

st.write("---") # Separator

# 3. Simulated AI Logic (The Superpower)
# This function now accepts keywords defined by the user.
def simulate_detection(rule, evidence, non_compliant_keywords):
    """
    Checks the evidence against the rule using simulated 99.1% accurate logic.
    Keywords are provided by the user via the input field.
    """
    
    evidence_lower = evidence.lower()
    
    # Check if any user-defined keyword is present in the evidence
    is_non_compliant = any(keyword.strip() in evidence_lower for keyword in non_compliant_keywords)
    
    # Simulate the outcome based on the simple check
    if is_non_compliant:
        return "NON-COMPLIANT", 0.991
    else:
        return "COMPLIANT", 0.991

# 4. Input Fields
with st.container(border=True):
    st.markdown("**1. Define the Rule or Policy (What to check for):**")
    rule_input = st.text_area(
        "Company Rule to Detect Against:",
        value="All expense reports exceeding $500 must receive prior, written approval from a department head.",
        height=100
    )
    
    st.markdown("**2. Define Non-Compliant Keywords (Separate by commas):**")
    keyword_input = st.text_area(
        "Keywords (The AI looks for these terms in the evidence):",
        value="unapproved payment, missed deadline, failed to file, breach of conduct",
        height=75
    )


    st.markdown("**3. Provide Document Evidence (The text to analyze):**")
    evidence_input = st.text_area(
        "Document Text/Evidence for Review:",
        value="The project manager submitted an expense report for $750. The associated email noted 'unapproved payment' for this transaction.",
        height=150
    )

# 5. Action Button
if st.button("🚨 Run ARCHON Detection Engine", use_container_width=True, type="primary"):
    
    # Split the keyword string into a list for the detection function
    keywords_list = [k.strip().lower() for k in keyword_input.split(',') if k.strip()]
    
    if not keywords_list:
        st.warning("Please provide at least one keyword to check.")
        st.stop()
        
    # --- Simulation of high-speed processing (The "Hours vs. Weeks" part) ---
    st.write("---")
    progress_bar = st.progress(0, text="Initializing 99.1% Accuracy Check...")
    
    for percent_complete in range(100):
        time.sleep(0.01) # Extremely fast processing
        progress_bar.progress(percent_complete + 1, text=f"Processing large document set... {percent_complete + 1}% complete")
    
    progress_bar.empty()
    st.write("---")

    # --- Run Detection Logic ---
    # Pass the user-defined keywords list to the function
    result, accuracy = simulate_detection(rule_input, evidence_input, keywords_list)
    
    # --- Display Results ---
    if result == "NON-COMPLIANT":
        st.error(f"## 🛑 {result} FINDING")
        st.markdown(f"**ARCHON's Confidence Score:** **{accuracy * 100:.1f}%** (Beats human average of 90%)")
        st.warning(f"Immediate attention required: The evidence text contains one or more flagged terms from your defined keywords list ({', '.join(keywords_list)}).")
    else:
        st.success(f"## ✅ {result} FINDING")
        st.markdown(f"**ARCHON's Confidence Score:** **{accuracy * 100:.1f}%**")
        st.info("No compliance breach detected by ARCHON's engine based on the provided keywords.")
        
    st.write("---")
    st.caption("Time taken: 0.98 seconds. (Simulated, real-world processing depends on data size.)")
