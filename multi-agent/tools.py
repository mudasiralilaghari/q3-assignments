from agents import function_tool  # ✅ use this from openai-agents

@function_tool
def get_career_roadmap(career: str) -> str:
    career = career.lower()
    if "data scientist" in career:
        return "Roadmap for Data Scientist:\n1. Learn Python\n2. Master Numpy/Pandas\n3. Study ML & DL\n4. Build portfolio\n5. Apply for jobs"
    elif "web developer" in career:
        return "Roadmap for Web Developer:\n1. HTML, CSS, JS\n2. React or Next.js\n3. Backend with Node or Django\n4. Deploy projects\n5. Apply!"
    else:
        return f"Sorry, no roadmap found for '{career}'. Please try another."