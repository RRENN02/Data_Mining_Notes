import random

# Parameters
num_agents = 100
threshold = 60
weeks = 50

# Initialize
history = [random.randint(0, num_agents)]  # Random initial attendance

# Simulate
for week in range(weeks):
    decisions = []
    
    for agent in range(num_agents):
        # Simple strategy: predict based on last week's attendance
        predicted_attendance = history[-1]
        
        if predicted_attendance < threshold:
            decisions.append(1)  # Decide to go
        else:
            decisions.append(0)  # Decide to stay home

    actual_attendance = sum(decisions)
    history.append(actual_attendance)
    
    print(f"Week {week+1}: {actual_attendance} people at the bar")

