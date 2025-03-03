import streamlit as st
from utils.animation_helper import show_process_animation, show_company_comparison_animation
from utils.company_helper import process_company_comparison
from utils.insurance_helper import process_insurance_query
from utils.groq_helper import process_user_input  # Updated import

# Set up Streamlit page
st.set_page_config(
    page_title="GenAI Insurance & Company Comparison",
    page_icon="🤖",
    layout="wide"
)

def main():
    st.title("🤖 GenAI Insurance & Company Comparison Portal")

    tabs = st.tabs(["Insurance Search", "Company Comparison"])

    with tabs[0]:
        st.header("Insurance Plan Search")

        # Input methods
        input_method = st.radio(
            "Choose input method:",
            ["Natural Language", "Form Input"]
        )

        if input_method == "Natural Language":
            user_query = st.text_area(
                "Describe what you're looking for:",
                placeholder="E.g., Hi, I'm John, 30 years old male with a healthy lifestyle, looking for a term plan"
            )
            if st.button("Search Plans", type="primary"):
                if user_query:
                    with st.spinner("Processing your request..."):
                        # Process natural language input
                        parsed_data = process_user_input(user_query)
                        if parsed_data.get("error"):
                            st.error(parsed_data["error"])
                            return

                        # Show process animation
                        show_process_animation()

                        # Get and display results
                        plans = process_insurance_query(parsed_data)
                        display_insurance_results(plans)
                else:
                    st.warning("Please enter your query first.")

        else:
            with st.form("insurance_form"):
                col1, col2 = st.columns(2)
                with col1:
                    name = st.text_input("Name")
                    age = st.number_input("Age", 18, 100, 30)
                with col2:
                    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                    lifestyle = st.selectbox(
                        "Lifestyle",
                        ["Healthy", "Average", "Sedentary"]
                    )

                if st.form_submit_button("Search Plans", type="primary"):
                    if name and age:
                        with st.spinner("Processing your request..."):
                            # Show process animation
                            show_process_animation()

                            # Get and display results
                            plans = process_insurance_query({
                                "name": name,
                                "age": age,
                                "gender": gender,
                                "lifestyle": lifestyle
                            })
                            display_insurance_results(plans)
                    else:
                        st.warning("Please fill in all required fields.")

    with tabs[1]:
        st.header("Company Service Comparison")

        col1, col2 = st.columns(2)
        with col1:
            company1 = st.selectbox(
                "Select first company",
                ["LTIMindtree", "Accenture", "TCS", "Infosys", "Wipro"]
            )
        with col2:
            company2 = st.selectbox(
                "Select second company",
                ["Accenture", "LTIMindtree", "TCS", "Infosys", "Wipro"]
            )

        if st.button("Compare Companies", type="primary"):
            if company1 != company2:
                with st.spinner("Analyzing companies..."):
                    show_company_comparison_animation()
                    comparison_result = process_company_comparison(company1, company2)
                    display_company_comparison(comparison_result)
            else:
                st.warning("Please select different companies to compare.")

def display_insurance_results(plans):
    st.subheader("📋 Recommended Insurance Plans")

    for plan in plans:
        with st.expander(f"{plan['company']} - {plan['plan_name']} (Rating: ⭐{plan['rating']})"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Monthly Premium:** ₹{plan['premium']}")
                st.markdown(f"**Coverage:** ₹{plan['coverage']}")
                st.markdown(f"**Term:** {plan['term']} years")
            with col2:
                st.markdown(f"**Benefits:**")
                for benefit in plan['benefits'].split(", "):
                    st.markdown(f"- {benefit}")
                st.markdown(f"**Claim Settlement Ratio:** {plan['claim_settlement_ratio']}%")

            st.markdown("---")
            st.markdown(f"**Next Steps:** {plan['next_steps']}")

def display_company_comparison(comparison):
    st.subheader("🔄 Company Comparison Results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### {comparison['company1']['name']}")
        for service in comparison['company1']['services']:
            st.markdown(f"- {service}")

    with col2:
        st.markdown(f"### {comparison['company2']['name']}")
        for service in comparison['company2']['services']:
            st.markdown(f"- {service}")

    st.markdown("### 🎯 Key Differences")
    for diff in comparison['differences']:
        st.markdown(f"- {diff}")

if __name__ == "__main__":
    main()