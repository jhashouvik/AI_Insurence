def process_company_comparison(company1, company2):
    """
    Generate a comparison between two companies.
    """
    company_data = {
        "LTIMindtree": {
            "services": [
                "Digital Transformation",
                "Cloud Services",
                "Data Analytics",
                "AI/ML Solutions",
                "Enterprise Integration",
                "Quality Engineering",
                "IoT Solutions"
            ]
        },
        "Accenture": {
            "services": [
                "Strategy Consulting",
                "Technology Services",
                "Digital Transformation",
                "Cloud Solutions",
                "Industry X.0",
                "Security Services",
                "Operations Optimization"
            ]
        },
        "TCS": {
            "services": [
                "IT Services",
                "Business Solutions",
                "Consulting",
                "Digital Transformation",
                "Cloud Computing",
                "Analytics & Insights",
                "Blockchain Solutions"
            ]
        },
        "Infosys": {
            "services": [
                "Digital Services",
                "Cloud Services",
                "Enterprise Solutions",
                "AI & Automation",
                "Data Analytics",
                "Cybersecurity",
                "Engineering Services"
            ]
        },
        "Wipro": {
            "services": [
                "Digital Strategy",
                "Cloud Computing",
                "Enterprise Solutions",
                "Analytics & AI",
                "Cybersecurity",
                "Engineering Services",
                "Consulting"
            ]
        }
    }

    differences = generate_differences(
        company_data[company1]["services"],
        company_data[company2]["services"]
    )

    return {
        "company1": {
            "name": company1,
            "services": company_data[company1]["services"]
        },
        "company2": {
            "name": company2,
            "services": company_data[company2]["services"]
        },
        "differences": differences
    }

def generate_differences(services1, services2):
    """
    Generate key differences between services.
    """
    unique_to_1 = set(services1) - set(services2)
    unique_to_2 = set(services2) - set(services1)
    common = set(services1) & set(services2)

    differences = []

    if unique_to_1:
        differences.append(
            f"Unique services in first company: {', '.join(unique_to_1)}"
        )
    if unique_to_2:
        differences.append(
            f"Unique services in second company: {', '.join(unique_to_2)}"
        )
    if common:
        differences.append(
            f"Both companies excel in: {', '.join(list(common)[:3])}"
        )

    return differences