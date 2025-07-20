task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
	case "high":
		if time_bound == "yes":
			print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
		else:
			print(f"Reminder: {task} is a high priority do it when free")
	case "medium":
		if time_bound == "yes":
			print(f"Reminder: {task} is a medium priority that requires immediate attention today!")
		else:
			print(f"Reminder: {task} is a medium priority do it when free")
	case "low":
		if time_bound == "yes":
			print(f"Reminder: {task} is a low priority that requires immediate attention today!")
		else:
			print(f"Reminder: {task} is a low priority do it when free")
