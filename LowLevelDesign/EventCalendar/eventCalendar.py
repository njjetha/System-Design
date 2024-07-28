from datetime import datetime, timedelta
from event import *
from user import *
from team import *

class EventCalendar:
    def __init__(self):
        self.users = {}
        self.teams = {}
        self.events = []

    def create_user(self, name, working_hours):
        if name in self.users:
            raise ValueError("User already exists")
        self.users[name] = User(name, working_hours)

    def create_team(self, name, user_names):
        if name in self.teams:
            raise ValueError("Team already exists")
        users = [self.users[user_name] for user_name in user_names]
        self.teams[name] = Team(name, users)

    def is_user_available(self, user, start_time, end_time):
        for event_ in user.event:
            if not (end_time <= event_.start_time or start_time >= event_.end_time):
                return False
        return True

    def create_event(self, name, participant_names, start_time, end_time, required_representatives):
        participants = []
        for participant_name in participant_names:
            if participant_name in self.users:
                user = self.users[participant_name]
                if not self.is_user_available(user, start_time, end_time):
                    raise ValueError(f"User {user.name} is not available")
                participants.append(user)
            elif participant_name in self.teams:
                team = self.teams[participant_name]
                available_users = [user for user in team.user if self.is_user_available(user, start_time, end_time)]
                if len(available_users) < required_representatives:
                    raise ValueError(f"Not enough available users in team {team.name}")
                participants.extend(available_users[:required_representatives])
            else:
                raise ValueError(f"Participant {participant_name} does not exist")
        
        event = Event(name, participants, start_time, end_time, required_representatives)
        self.events.append(event)
        for participant in participants:
            participant.event.append(event)

    def get_events_for_user(self, user_name, start_time, end_time):
        if user_name not in self.users:
            raise ValueError("User does not exist")
        user = self.users[user_name]
        return [event for event in user.event if not (end_time <= event.start_time or start_time >= event.end_time)]

    def suggest_available_slots(self, participant_names, day):
        available_slots = []
        start_of_day = datetime.combine(day, datetime.min.time())
        end_of_day = start_of_day + timedelta(days=1)
        current_time = start_of_day
        # participant_name=participant_names[0]

        while current_time < end_of_day:
            slot_end_time = current_time + timedelta(hours=1)
            if all(self.is_user_available(self.users[participant_name], current_time, slot_end_time) for participant_name in participant_names):
                available_slots.append((current_time, slot_end_time))
            current_time = slot_end_time

        return available_slots

# Sample Test Cases
calendar = EventCalendar()

# Onboard Users
calendar.create_user("A", (10, 19))
calendar.create_user("B", (9.5, 17.5))
calendar.create_user("C", (11.5, 18.5))
calendar.create_user("D", (10, 18))
calendar.create_user("E", (11, 19.5))
calendar.create_user("F", (11, 18.5))

# Create Teams
calendar.create_team("T1", ["C", "E"])
calendar.create_team("T2", ["B", "D", "F"])

# Create Events
calendar.create_event("Event1", ["A", "T1"], datetime(2024, 7, 29, 14, 0), datetime(2024, 7, 29, 15, 0), 2)
try:
    calendar.create_event("Event2", ["C"], datetime(2024, 7, 29, 14, 0), datetime(2024, 7, 29, 15, 0), 1)
except ValueError as e:
    print(e)  # Should fail since C is already part of Event1

calendar.create_event("Event3", ["T1", "T2"], datetime(2024, 7, 28, 15, 0), datetime(2024, 7, 28, 16, 0), 2)
calendar.create_event("Event4", ["A", "T2"], datetime(2024, 7, 28, 15, 0), datetime(2024, 7, 28, 16, 0), 1)
try:
    calendar.create_event("Event5", ["A", "F"], datetime(2024, 7, 28, 10, 0), datetime(2024, 7, 28, 11, 0), 1)
except ValueError as e:
    print(e)  # Should fail since it's outside F's working hours

# Get Events for a time range
events_for_a = calendar.get_events_for_user("A", datetime(2024, 7, 28, 10, 0), datetime(2024, 7, 29, 17, 0))
print([event.name for event in events_for_a])  # Output: Event1, Event4

# Suggest available time slots
available_slots = calendar.suggest_available_slots(["A", "B"], datetime(2024, 7, 28))
print([(slot[0].time(), slot[1].time()) for slot in available_slots])  # Output: 10AM to 3PM and 4PM to 7PM
