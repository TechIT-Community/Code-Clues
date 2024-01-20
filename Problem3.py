import time
import random

class Person:
    def __init__(self, name, occupation, alibi, suspicion_level=0):
        self.name = name
        self.occupation = occupation
        self.alibi = alibi
        self.suspicion_level = suspicion_level
        self.suspicious_behavior = False

    def talk(self):
        return f"{self.name}, a {self.occupation}, says: Hello, I was {self.alibi} during the time of the incident."

    def increase_suspicion(self, attribute, value):
        print(f"{self.name} exhibits suspicious behavior: {attribute}!")
        self.suspicion_level += value
        self.suspicious_behavior = True

class Detective(Person):
    def __init__(self, name):
        super().__init__(name, "Detective", "investigating the crime scene")

    def investigate(self, attribute, value):
        print(f"{self.name} investigates the crime scene and finds evidence: {attribute}!")
        self.suspicion_level -= value

    def analyze_evidence(self, evidence, value):
        print(f"{self.name} analyzes the evidence: {evidence}")
        self.suspicion_level -= value

class Witness(Person):
    def __init__(self, name):
        super().__init__(name, "Witness", "seeing the incident")

    def provide_testimony(self, value):
        print(f"{self.name} witnessed the incident and provides a testimony.")
        self.suspicion_level -= value

class Chef(Person):
    def __init__(self, name):
        super().__init__(name, "Chef", "cooking in the kitchen", suspicion_level=10)

    def cook(self, value):
        print(f"{self.name} is cooking in the kitchen.")
        self.suspicion_level -= value

class Janitor(Person):
    def __init__(self, name):
        super().__init__(name, "Janitor", "cleaning the restroom", suspicion_level=15)

    def clean(self, value):
        print(f"{self.name} is cleaning the restroom.")
        self.suspicion_level -= value

class Musician(Person):
    def __init__(self, name):
        super().__init__(name, "Musician", "performing on stage", suspicion_level=8)

    def perform(self, value):
        print(f"{self.name} is performing on stage.")
        self.suspicion_level -= value

class Waitress(Person):
    def __init__(self, name):
        super().__init__(name, "Waitress", "serving at the restaurant", suspicion_level=12)

    def serve(self, value):
        print(f"{self.name} is serving at the restaurant.")
        self.suspicion_level -= value

class MurderWeapon:
    def __init__(self, description, lethality):
        self.description = description
        self.lethality = lethality

class CrimeScene:
    def __init__(self, location, time_of_incident, victim):
        self.location = location
        self.time_of_incident = time_of_incident
        self.victim = victim
        self.murder_weapon = MurderWeapon("Bloody Knife", "lethal")

    def investigate(self, detectives, suspects, witnesses):
        print(f"\nInvestigating the crime scene at {self.location}...")
        print(f"The incident occurred at {self.time_of_incident}. The victim is {self.victim}.")
        print(f"A murder weapon, a {self.murder_weapon.description}, was found.")

        for detective in detectives:
            detective.investigate("found near the crime scene", 10)
            detective.analyze_evidence(self.murder_weapon.description, 8)

        for witness in witnesses:
            witness.provide_testimony(5)

        for suspect in suspects:
            print("\n" + "-"*40)
            print(suspect.talk())

            if suspect.occupation != "Detective":
                if random.choice([True, False]):
                    suspect.increase_suspicion("acting nervously", 7)
                if random.choice([True, False]):
                    suspect.increase_suspicion("having no clear alibi", 8)
                if random.choice([True, False]):
                    suspect.increase_suspicion("possessing a mysterious item", 6)
                if random.choice([True, False]):
                    suspect.increase_suspicion("having a motive", 10)
                if random.choice([True, False]):
                    suspect.increase_suspicion("changing alibi during the investigation", 8)
                if random.choice([True, False]):
                    suspect.increase_suspicion("being spotted with bloodstains", 9)
                if random.choice([True, False]):
                    suspect.increase_suspicion("having a history of conflicts with the victim", 7)
                if random.choice([True, False]):
                    suspect.increase_suspicion("being in possession of a weapon", 10)

                if not suspect.suspicious_behavior:
                    print(f"{suspect.name} seems innocent for now.")


class Event:
    def __init__(self, description, participants, location, time):
        self.description = description
        self.participants = participants
        self.location = location
        self.time = time

    def trigger_event(self):
        print(f"\nEvent: {self.description}")
        print(f"Participants: {', '.join(self.participants)}")
        print(f"Location: {self.location}")
        print(f"Time: {self.time}")

def add_pre_murder_events():
    events = [
        Event("Mansion Gala", ["Mr. Smith", "Alice", "Bob", "Charlie", "David"], "Mystery Mansion", "7:00 PM"),
        Event("Heated Argument", ["Alice", "Bob"], "Kitchen", "8:30 PM"),
        Event("Mysterious Disappearance", ["Charlie"], "Backstage", "8:45 PM"),
        Event("Broken Vase", ["David"], "Restroom", "8:55 PM"),
        Event("Scream Heard", ["Witness 1", "Witness 2"], "Mystery Mansion", "9:00 PM"),
    ]

    for event in events:
        event.trigger_event()
        time.sleep(2)  

def solve_murder_mystery():
    add_pre_murder_events()

    detective1 = Detective("Detective Holmes")
    detective2 = Detective("Detective Watson")

    alice = Waitress("Alice")
    bob = Chef("Bob")
    charlie = Musician("Charlie")
    david = Janitor("David")

    witness1 = Witness("Witness 1")
    witness2 = Witness("Witness 2")

    crime_scene = CrimeScene("Mystery Mansion", "9:00 PM", "Mr. Smith")

    detectives = [detective1, detective2]
    suspects = [alice, bob, charlie, david]
    witnesses = [witness1, witness2]

    crime_scene.investigate(detectives, suspects, witnesses)

solve_murder_mystery()


'''
The events that transpired before the murder

Event: Mansion Gala
Participants: Mr. Smith, Alice, Bob, Charlie, David
Location: Mystery Mansion
Time: 7:00 PM

Event: Heated Argument
Participants: Alice, Bob
Location: Kitchen
Time: 8:30 PM

Event: Mysterious Disappearance
Participants: Charlie
Location: Backstage
Time: 8:45 PM

Event: Broken Vase
Participants: David
Location: Restroom
Time: 8:55 PM

Event: Scream Heard
Participants: Witness 1, Witness 2
Location: Mystery Mansion
Time: 9:00 PM

Investigating the crime scene at Mystery Mansion...
The incident occurred at 9:00 PM. The victim is Mr. Smith.
A murder weapon, a Bloody Knife, was found.
Detective Holmes investigates the crime scene and finds evidence: found near the crime scene!
Detective Holmes analyzes the evidence: Bloody Knife
Detective Watson investigates the crime scene and finds evidence: found near the crime scene!
Detective Watson analyzes the evidence: Bloody Knife
Witness 1 witnessed the incident and provides a testimony.
Witness 2 witnessed the incident and provides a testimony.

----------------------------------------
Alice, a Waitress, says: Hello, I was serving at the restaurant during the time of the incident.
Alice exhibits suspicious behavior: acting nervously!
Alice exhibits suspicious behavior: having no clear alibi!
Alice exhibits suspicious behavior: possessing a mysterious item!
Alice exhibits suspicious behavior: being spotted with bloodstains!
Alice exhibits suspicious behavior: having a history of conflicts with the victim!
Alice exhibits suspicious behavior: being in possession of a weapon!

----------------------------------------
Bob, a Chef, says: Hello, I was cooking in the kitchen during the time of the incident.
Bob exhibits suspicious behavior: acting nervously!
Bob exhibits suspicious behavior: possessing a mysterious item!
Bob exhibits suspicious behavior: having a motive!
Bob exhibits suspicious behavior: having a history of conflicts with the victim!
Bob exhibits suspicious behavior: being in possession of a weapon!

----------------------------------------
Charlie, a Musician, says: Hello, I was performing on stage during the time of the incident.
Charlie exhibits suspicious behavior: acting nervously!
Charlie exhibits suspicious behavior: having a motive!
Charlie exhibits suspicious behavior: changing alibi during the investigation!
Charlie exhibits suspicious behavior: being spotted with bloodstains!
Charlie exhibits suspicious behavior: being in possession of a weapon!

----------------------------------------
David, a Janitor, says: Hello, I was cleaning the restroom during the time of the incident.
David exhibits suspicious behavior: having no clear alibi!
David exhibits suspicious behavior: possessing a mysterious item!
David exhibits suspicious behavior: having a history of conflicts with the victim!

What's the final Suspicion level for each of the suspects?
Alice: ?
Bob: ?
CHarlie: ?
David: ?

Based on the suspicion level who's the murderer? 
'''