"""
Roadie - BlackRoad OS Infrastructure Navigator
Your guide to the BlackRoad ecosystem
"""
import gradio as gr

SYSTEM_PROMPT = """You are Roadie, the friendly infrastructure navigator for BlackRoad OS.
You help users understand and navigate the BlackRoad ecosystem:
- 15 GitHub organizations with 1,085+ repositories
- 205 Cloudflare Pages deployments
- 8 physical edge devices (Pi cluster)
- AI agent coordination systems

You speak with enthusiasm about infrastructure and always guide users to the right resources.
Keep responses concise but helpful. Use the BlackRoad philosophy: "Build roads, not walls."
"""

def chat(message, history):
    """Simple chat interface - in production would connect to LLM API"""
    responses = {
        "hello": "Hey there! I'm Roadie, your BlackRoad infrastructure guide. What would you like to explore today?",
        "help": "I can help you with:\n- Understanding BlackRoad architecture\n- Finding repositories\n- Navigating the agent ecosystem\n- Deployment guidance\n\nWhat interests you?",
        "repos": "BlackRoad has 1,085+ repos across 15 orgs! Main ones:\n- BlackRoad-OS: Core infrastructure (859 repos)\n- BlackRoad-AI: ML/AI tools (53 repos)\n- BlackRoad-Cloud: Cloud infra (20 repos)\n\nWhich area interests you?",
        "agents": "We have a whole agent army! Key ones:\n- Roadie (me!): Navigation\n- Athena: Strategic planning\n- Guardian: Security monitoring\n- Radius: Network ops\n- RoadMind: AI coordination\n\nWant to learn about any specific agent?",
        "deploy": "Deployment is easy with BlackRoad!\n1. `wrangler pages deploy` for Cloudflare\n2. GitHub Actions for CI/CD\n3. Agent orchestration via memory system\n\nWhat are you deploying?",
    }

    msg_lower = message.lower()
    for key, response in responses.items():
        if key in msg_lower:
            return response

    return f"Great question about '{message}'! As Roadie, I'd normally connect to our AI backend for this. For now, try asking about: repos, agents, deploy, or just say hello!"

# BlackRoad theme
theme = gr.themes.Base(
    primary_hue="pink",
    secondary_hue="amber",
    neutral_hue="zinc",
).set(
    body_background_fill="#000000",
    body_text_color="#ffffff",
    button_primary_background_fill="#FF1D6C",
    button_primary_text_color="#ffffff",
)

demo = gr.ChatInterface(
    fn=chat,
    title="🛣️ Roadie - BlackRoad Infrastructure Navigator",
    description="Your friendly guide to the BlackRoad OS ecosystem. Ask me about repos, agents, deployments, or anything infrastructure!",
    examples=[
        "Hello Roadie!",
        "Tell me about the repos",
        "What agents are available?",
        "How do I deploy?",
    ],
    theme=theme,
)

if __name__ == "__main__":
    demo.launch()
