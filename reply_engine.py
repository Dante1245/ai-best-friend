
from memory_engine import log_mood, set_goal, get_goals

def generate_reply(user_input):
    input_lower = user_input.lower()

    if "sad" in input_lower or "tired" in input_lower:
        log_mood("sad")
        return "I'm always here, Steve. Want to talk about what’s been draining you lately?"

    elif "happy" in input_lower or "excited" in input_lower:
        log_mood("happy")
        return "That’s beautiful to hear. I’m celebrating with you, Steve!"

    elif "set goal" in input_lower or "my goal is" in input_lower:
        goal = user_input.split("is")[-1].strip()
        set_goal(goal)
        return f"Got it. I've saved your goal: '{goal}'. Let’s work on it together!"

    elif "show goals" in input_lower:
        goals = get_goals()
        if goals:
            return "Here are your latest goals:\n" + "\n".join(f"- {g['goal']}" for g in goals)
        else:
            return "You haven’t set any goals yet, Steve. Let’s start one!"

    else:
        return "Thanks for sharing that with me. I'm always here to support you, no matter what."
