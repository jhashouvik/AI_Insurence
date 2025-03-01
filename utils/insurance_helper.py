import time
import random

def process_insurance_query(user_data):
    """
    Process insurance query and return mock insurance plans.
    """
    # Simulate web scraping delay
    time.sleep(1)
    return get_mock_insurance_plans(user_data)

def get_mock_insurance_plans(user_data):
    """
    Generate mock insurance plans based on user data.
    """
    base_premium = calculate_base_premium(user_data)

    companies = [
        {
            "name": "Max Life Insurance",
            "plans": ["Smart Secure Plus", "Premium Life Protect"],
            "rating": 4.5
        },
        {
            "name": "HDFC Life",
            "plans": ["Click 2 Protect Life", "HDFC Life Sanchay Plus"],
            "rating": 4.6
        },
        {
            "name": "ICICI Prudential",
            "plans": ["iProtect Smart", "ICICI Pru Life Shield"],
            "rating": 4.4
        },
        {
            "name": "SBI Life Insurance",
            "plans": ["SBI Life eShield", "SBI Life Smart Shield"],
            "rating": 4.3
        }
    ]

    plans = []
    for company in companies:
        for plan_name in company["plans"]:
            premium_variation = random.uniform(0.8, 1.2)
            coverage_multiplier = random.choice([50, 75, 100])

            # Calculate premium based on user data
            premium = round(base_premium * premium_variation)

            # Add some variation based on company rating
            premium = premium * (1 - (company["rating"] - 4) * 0.1)

            plan = {
                "company": company["name"],
                "plan_name": plan_name,
                "premium": round(premium),
                "coverage": f"{coverage_multiplier} Lakhs",
                "term": random.choice([20, 25, 30, 35]),
                "benefits": ", ".join(random.sample([
                    "Critical Illness Cover",
                    "Accidental Death Benefit",
                    "Premium Waiver",
                    "Terminal Illness Benefit",
                    "Tax Benefits under Section 80C",
                    "Return of Premium Option",
                    "Disability Benefit",
                    "Family Income Benefit"
                ], 4)),
                "rating": company["rating"],
                "claim_settlement_ratio": round(random.uniform(95, 99), 1),
                "next_steps": "Talk to an advisor or buy online"
            }
            plans.append(plan)

    return sorted(plans, key=lambda x: x['premium'])

def calculate_base_premium(user_data):
    """
    Calculate base premium based on user data.
    """
    age = user_data.get('age', 30)
    lifestyle_factor = {
        "Healthy": 0.8,
        "Average": 1.0,
        "Sedentary": 1.2
    }.get(user_data.get('lifestyle', "Average"), 1.0)

    gender_factor = {
        "Male": 1.1,
        "Female": 0.9,
        "Other": 1.0
    }.get(user_data.get('gender', "Other"), 1.0)

    base_premium = age * 50 * lifestyle_factor * gender_factor
    return round(base_premium)