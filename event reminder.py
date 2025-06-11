import datetime

# Store events in a list of dictionaries
events = [
    {"date": "2025-06-10", "task": "Submit GitHub project"},
    {"date": "2025-06-15", "task": "Start bug bounty learning"},
    {"date": "2025-06-20", "task": "Resume building & upload"},
]

# Get today’s date
today = datetime.date.today().isoformat()

# Check for today's events
print(f"📅 Today is {today}")
found = False

for event in events:
    if event["date"] == today:
        print(f"🔔 Reminder: {event['task']}")
        found = True

if not found:
    print("✅ No tasks for today. Relax and focus!")

# Optional: Let user add an event
add = input("Do you want to add a new event? (yes/no): ").lower()
if add == "yes":
    new_date = input("Enter date (YYYY-MM-DD): ")
    new_task = input("Enter task: ")
    events.append({"date": new_date, "task": new_task})
    print("📝 Event added successfully!")