
def greet(name, years):
    return f"નમસ્તે {name}! {years} વર્ષ Java + AI = 🚀"


name = "Parth"
experience_years = 5

# Add 5 skills
skills = [
    "Java",
    "Spring Boot",
    "Redis",
    "PostgreSQL",
    "Microservices"
]

# AI usage of each skill
ai_usage = [
    "Spring AI / LangChain4j",
    "AI Backend APIs",
    "LLM Response Caching",
    "Vector Database / RAG Storage",
    "AI Microservices Architecture"
]

# Print greeting
print(greet(name, experience_years))

print("\n🚀 My Skills + AI Applications:\n")

# Loop through skills and AI usage
for skill, usage in zip(skills, ai_usage):
    print(f"✅ {skill} → {usage}")
