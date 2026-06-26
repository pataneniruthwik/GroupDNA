# Step 1 - Open the chat file
file = open("chat.txt", "r")

# Step 2 - Read all lines
lines = file.readlines()

# Step 3 - Close the file
file.close()

print("====================================================")
print("               GROUPDNA REPORT")
print("      Your WhatsApp Group Chat, Decoded")
print("====================================================")

# Lists to store chat and system messages
messages = []
system_messages = []

# Process each line
for line in lines:

    line = line.strip()

    # Split into Date-Time and Remaining Part
    parts = line.split(" - ")

    # Skip incorrect line format
    if len(parts) < 2:
        continue

    date_time = parts[0]
    remaining = parts[1]

    # Split Date and Time
    date, time = date_time.split(", ")

    # Check whether it is a normal chat message
    if ": " in remaining:

        # Split Sender and Message
        sender, message = remaining.split(": ", 1)

        # Store normal chat message
        chat = {
            "date": date,
            "time": time,
            "sender": sender,
            "message": message
        }

        messages.append(chat)

    else:

        # Store system message
        system = {
            "date": date,
            "time": time,
            "event": remaining
        }

        system_messages.append(system)

# Group Overview
print("\n========== GROUP OVERVIEW ==========\n")

print("Total Chat Messages   :", len(messages))
print("Total System Messages :", len(system_messages))
print("Total Entries         :", len(messages) + len(system_messages))

# Participant Analysis
print("\n========== PARTICIPANT ANALYSIS ==========\n")

# Dictionary to count messages of each participant
member_count = {}

# Read every stored chat message
for chat in messages:

    sender = chat["sender"]

    # If sender already exists, increase the count
    if sender in member_count:
        member_count[sender] += 1

    # Otherwise create a new sender entry
    else:
        member_count[sender] = 1

# Display message count of every participant
for sender, count in member_count.items():
    print(sender, ":", count)

# Display total number of participants
print("\nTotal Participants :", len(member_count))

# Find most active participant
most_active = max(member_count, key=member_count.get)

print("Most Active Member :", most_active)
print("Messages Sent      :", member_count[most_active])

# Find least active participant
least_active = min(member_count, key=member_count.get)

print("Least Active Member:", least_active)
print("Messages Sent      :", member_count[least_active])
# Activity Analysis
print("\n========== ACTIVITY ANALYSIS ==========\n")

# Dictionary to count messages by hour
hour_count = {}

# Read every stored chat message
for chat in messages:

    hour = chat["time"].split(":")[0]

    # If hour already exists, increase the count
    if hour in hour_count:
        hour_count[hour] += 1

    # Otherwise create a new hour entry
    else:
        hour_count[hour] = 1

# Display message count of every hour
for hour, count in hour_count.items():
    print(hour, ":", count)
# Find most active hour
most_active_hour = max(hour_count, key=hour_count.get)

print("\nMost Active Hour :", most_active_hour)
print("Messages Sent    :", hour_count[most_active_hour])

# Find least active hour
least_active_hour = min(hour_count, key=hour_count.get)

print("\nLeast Active Hour :", least_active_hour)
print("Messages Sent     :", hour_count[least_active_hour])

# Date Analysis
print("\n========== DATE ANALYSIS ==========\n")

# Dictionary to count messages by date
date_count = {}

# Read every stored chat message
for chat in messages:

    date = chat["date"]

    # If date already exists, increase the count
    if date in date_count:
        date_count[date] += 1

    # Otherwise create a new date entry
    else:
        date_count[date] = 1

# Display message count of every date
for date, count in date_count.items():
    print(date, ":", count)

# Find most active date
most_active_date = max(date_count, key=date_count.get)

print("\nMost Active Date :", most_active_date)
print("Messages Sent    :", date_count[most_active_date])

# Find least active date
least_active_date = min(date_count, key=date_count.get)

print("\nLeast Active Date :", least_active_date)
print("Messages Sent     :", date_count[least_active_date])
# Message Analysis
print("\n========== MESSAGE ANALYSIS ==========\n")

deleted_count = 0
media_count = 0

# Read every stored chat message
for chat in messages:

    message = chat["message"]

    # Count deleted messages
    if "deleted" in message.lower():
        deleted_count += 1

    # Count media messages
    if "<media omitted>" in message.lower():
        media_count += 1

print("Deleted Messages :", deleted_count)
print("Media Messages   :", media_count)
# Personality Analysis
print("\n========== PERSONALITY ARCHETYPES ==========\n")
# Dictionary to store persona of each participant
persona = {}

for sender, count in member_count.items():
# Check every participant
# Assign personality archetype
 if count >= 500:
    persona[sender] = "THE SPAMMER"
    print("Persona :", persona[sender])
 elif count >= 200:
    persona[sender] = "THE SOCIAL BUTTERFLY"
    print("Persona :", persona[sender])

 elif count >= 50:
    persona[sender] = "THE STORYTELLER"
    print("Persona :", persona[sender])

 else:
    persona[sender] = "THE GHOST"
    print("Persona :", persona[sender])

# Search Message by Date and Time
print("\n========== SEARCH MESSAGE ==========\n")

choice = input("Do you want to search a message? (yes/no): ")

if choice.lower() == "yes":

    search_date = input("Enter Date (dd/mm/yy): ")
    search_time = input("Enter Time (hh:mm): ")

    found = False

    # Search every stored chat message
    for chat in messages:

        if chat["date"] == search_date and chat["time"] == search_time:

            print("\nMessage Found")
            print("Sender  :", chat["sender"])
            print("Persona  :", persona[chat["sender"]])
            print("Message  :", chat["message"])

            found = True
            break

    if found == False:
        print("\nNo message found.")

else:
    print("\nThank You!")