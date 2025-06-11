print("🤖 Welcome to Nirmala's Mental Health Chat Support Bot")
print("How are you feeling today? (happy/sad/anxious/tired/motivated)")

mood = input("Your mood: ").lower()

if mood == "happy":
    print("😊 That's wonderful! Keep smiling and spread the joy!")
elif mood == "sad":
    print("💙 It's okay to feel sad. Take a deep breath. You're stronger than you think.")
elif mood == "anxious":
    print("🧘 Try closing your eyes and breathe deeply for a minute. You are safe and in control.")
elif mood == "tired":
    print("😴 Rest is important. Take a short break, drink water, and recharge.")
elif mood == "motivated":
    print("🔥 Keep going! Your dreams are closer than they seem.")
else:
    print("🤔 I'm here for you. Remember: Every feeling is valid. You got this!")

print("\n💬 Type 'exit' to end the session.")