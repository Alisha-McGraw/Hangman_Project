import random
import time

# --- Game Data Dictionaries ---
SPACESHIPS = {
    "1": {"name": "The Ares V", "integrity": 150, "shield_bonus": 10, "desc": "A heavily armored freighter, slow but resilient (+150 HP, +10 Shield)."},
    "2": {"name": "The Hermes X", "integrity": 100, "shield_bonus": 25, "desc": "A sleek exploration vessel, fast with strong shielding (+100 HP, +25 Shield)."},
    "3": {"name": "The Daedalus", "integrity": 125, "shield_bonus": 15, "desc": "A balanced science ship, good all-around performance (+125 HP, +15 Shield)."},
}

COPILOTS = {
    "1": {"name": "Dr. Elara Vance (Engineer)", "skill": "Engineering", "bonus": 0.25, "desc": "Increases success chance on technical challenges."},
    "2": {"name": "Captain Jax (Pilot)", "skill": "Piloting", "bonus": 0.25, "desc": "Increases success chance on maneuvering and evasion."},
    "3": {"name": "HAL-9000 (AI)", "skill": "Logic", "bonus": 0.35, "desc": "Excels at complex trivia and logic problems."},
}

# --- Game Logic Class ---

class MartianOdyssey:
    """
    Manages the state, progression, and events of the Mars Mission game.
    """
    def __init__(self):
        # Ship stats
        self.ship_name = ""
        self.max_integrity = 0
        self.current_integrity = 0
        self.shield_strength = 0

        # Copilot stats
        self.copilot_name = ""
        self.copilot_skill = ""
        self.copilot_bonus = 0.0

        # Game State
        self.location = "Earth Orbit"
        self.stages = [
            self.asteroid_field,
            self.engine_repair_puzzle,
            self.deep_space_anomaly,
        ]
        self.game_over_flag = False

    def display_status(self):
        """Prints the current status of the mission."""
        print("-" * 50)
        print(f"STATUS REPORT | Location: {self.location}")
        print(f"Ship: {self.ship_name} | Copilot: {self.copilot_name}")
        print(f"Integrity: {self.current_integrity}/{self.max_integrity} HP | Shields: {self.shield_strength} (Total)")
        print("-" * 50)

    def take_damage(self, damage):
        """Applies damage, checks for shields, and updates integrity."""
        print(f"\n<<< WARNING: Incoming damage detected: {damage} points. >>>")
        
        # Apply shield reduction first
        damage_absorbed = min(damage, self.shield_strength // 2)
        remaining_damage = damage - damage_absorbed

        if damage_absorbed > 0:
            print(f"Shields absorb {damage_absorbed} points of damage.")

        if remaining_damage > 0:
            self.current_integrity -= remaining_damage
            print(f"Ship Integrity damaged by {remaining_damage} points.")
        else:
            print("Damage neutralized.")

        if self.current_integrity <= 0:
            self.current_integrity = 0
            self.game_over_flag = True
            print("\n!!! CRITICAL FAILURE: Ship integrity lost. Mission Aborted.")
        
        self.display_status()

    def get_user_choice(self, prompt, options_dict):
        """
        Handles user input and validation for choices.
        Now prints the options dynamically before prompting for input.
        """
        while True:
            # Print the numbered options with their descriptions
            for key, data in options_dict.items():
                # Check if 'desc' or 'name' is available for printing
                description = data.get('desc') or data.get('name') or data
                print(f"[{key}] {description}")
            
            # Print the main prompt
            print(prompt)
            
            try:
                # Get input from the user
                choice = input("Enter your choice (number): ").strip()
                
                # Validate the choice against the available keys
                if choice in options_dict.keys():
                    return choice
                print("Invalid choice. Please select a number from the options.")
            except EOFError:
                print("Input interrupted. Exiting.")
                self.game_over_flag = True
                return None
            time.sleep(0.1) # Small delay for better CLI feel

    def choose_ship(self):
        """Allows the player to select their spaceship."""
        print("\n" + "=" * 50)
        print("PHASE 1: SPACESHIP SELECTION")
        print("Please choose your vessel for the Martian Odyssey:")
        print("=" * 50)

        # Pass the entire SPACESHIPS dictionary to get_user_choice
        choice = self.get_user_choice("\nWhich ship will you pilot?", SPACESHIPS)
        if self.game_over_flag: return

        ship_data = SPACESHIPS[choice]
        self.ship_name = ship_data['name']
        self.max_integrity = ship_data['integrity']
        self.current_integrity = self.max_integrity
        self.shield_strength = ship_data['shield_bonus']

        print(f"\n--- Confirmed: You have selected {self.ship_name}. ---")
        self.display_status()

    def choose_copilot(self):
        """Allows the player to select their copilot."""
        print("\n" + "=" * 50)
        print("PHASE 2: COPILOT SELECTION")
        print("Choose a copilot. Their expertise will influence mission success:")
        print("=" * 50)

        # Pass the entire COPILOTS dictionary to get_user_choice
        choice = self.get_user_choice("\nWho will be your second in command?", COPILOTS)
        if self.game_over_flag: return

        copilot_data = COPILOTS[choice]
        self.copilot_name = copilot_data['name']
        self.copilot_skill = copilot_data['skill']
        self.copilot_bonus = copilot_data['bonus']

        print(f"\n--- Confirmed: Your copilot is {self.copilot_name}. ---")
        self.display_status()
        
    # --- Mission Stages ---

    def asteroid_field(self):
        """Stage 1: Navigating a hazardous asteroid field."""
        self.location = "The Asteroid Belt"
        self.display_status()
        print("\nStage 1: ASTEROID FIELD NAVIGATION")
        print("A dense belt of debris lies ahead. This requires swift maneuvering.")

        options = {
            "1": {"desc": "Pilot through the center, relying on speed and agility."},
            "2": {"desc": "Engage maximum shields and plow through the least dense side."},
            "3": {"desc": "Attempt a complex, long-range evasion pattern to bypass the bulk of the field."},
        }
        
        prompt = "\nWhat is your tactical decision?"
        # Pass the new options dict to get_user_choice
        choice = self.get_user_choice(prompt, options)
        if self.game_over_flag: return

        # Base success chance (30%) + skill bonus
        success_chance = 0.30
        if self.copilot_skill == "Piloting":
            success_chance += self.copilot_bonus # Pilot adds 25%

        outcome = random.random()

        if choice == "1" or choice == "3": # Choices requiring high piloting/agility
            if outcome < success_chance:
                print(f"SUCCESS: The ship, guided by {self.copilot_name}'s expertise, executed a perfect evasion pattern!")
            else:
                self.take_damage(random.randint(20, 40))
                print("FAILURE: The maneuvers were too tight. Asteroids breached the outer layer, causing internal damage.")
        elif choice == "2": # Choice relying on shield/tanking
            if self.shield_strength > 20:
                print(f"SUCCESS: Maximum shields hold! The impacts were harsh, but your {self.ship_name}'s high shielding rating absorbed the worst of the debris.")
                self.take_damage(random.randint(5, 15)) # Small unavoidable damage
            else:
                self.take_damage(random.randint(30, 50))
                print("FAILURE: Your shielding was insufficient for a direct approach. Heavy impacts caused structural damage.")
        
        print("--- End of Stage 1 ---")

    def engine_repair_puzzle(self):
        """Stage 2: Technical trivia/logic to repair the engine."""
        self.location = "Mid-Transit Deep Space"
        self.display_status()
        print("\nStage 2: CRITICAL POWER FAILURE")
        print("Your main engine has sputtered! A complex logic lock-out sequence has been triggered.")
        print("You must answer the core logic question to restore primary power.")

        puzzles = [
            {
                "question": "I am always in front of you, but can never be seen. What am I?",
                "answer": "FUTURE",
                "skill_check": "Logic",
            },
            {
                "question": "A capacitor bank shows '47uF'. The nearest identical replacement is labeled '0.000047F'. Is it an exact match? (YES/NO)",
                "answer": "YES",
                "skill_check": "Engineering",
            },
            {
                "question": "If two astronauts leave the station at the same time, one travels at 0.5c and the other at 0.75c, which one experiences slower time dilation? (FASTER/SLOWER)",
                "answer": "SLOWER",
                "skill_check": "Logic",
            }
        ]
        
        # Select a puzzle, and give a hint based on copilot skill
        puzzle = random.choice(puzzles)
        
        # Bonus hint based on copilot skill
        if self.copilot_skill == puzzle['skill_check']:
            print(f"Copilot {self.copilot_name} (Skill: {self.copilot_skill}) offers a detailed schematic.")
            bonus_hint = "The answer is case-insensitive, but be precise."
            if puzzle['skill_check'] == "Engineering":
                 bonus_hint += " Hint: Remember SI unit prefixes."
            print(f"Hint: {bonus_hint}")
            
        print("\n--- The Logic Question ---")
        user_answer = input(f"Query: {puzzle['question']} | Your Answer: ").strip().upper()

        if user_answer == puzzle['answer']:
            print("\nSUCCESS: Access granted! The correct logic sequence has rebooted the engine.")
            self.current_integrity = min(self.max_integrity, self.current_integrity + 15) # Small repair
            print("Minor hull repairs initiated. +15 HP.")
        else:
            damage = random.randint(30, 50)
            if self.copilot_skill == puzzle['skill_check']:
                # The copilot's bonus helps them suggest a re-attempt if the player failed
                if random.random() < self.copilot_bonus:
                    print(f"RE-ATTEMPT: {self.copilot_name} spots a minor error in your input. Try again.")
                    user_answer = input(f"Query: {puzzle['question']} | Your Answer: ").strip().upper()
                    if user_answer == puzzle['answer']:
                         print("\nSUCCESS: Second attempt successful! Engine Online.")
                         self.current_integrity = min(self.max_integrity, self.current_integrity + 5)
                         print("Engine back online.")
                         return
            
            print("FAILURE: Incorrect sequence entered. A power surge destabilizes life support.")
            self.take_damage(damage)

        print("--- End of Stage 2 ---")
        
    def deep_space_anomaly(self):
        """Stage 3: Encountering an unknown energy signature."""
        self.location = "Outer Solar System"
        self.display_status()
        print("\nStage 3: DEEP SPACE ANOMALY")
        print("Sensors detect a massive, non-hostile energy signature directly ahead. It might be a cosmic refueling point or a gravity well.")
        
        options = {
            "1": {"desc": "Approach slowly and attempt to harness the energy (High Risk/High Reward)."},
            "2": {"desc": "Skirt the edge of the field, maintaining a safe distance (Medium Risk/Low Reward)."},
            "3": {"desc": "Execute a full-burn evasive maneuver, wasting fuel but ensuring safety (Low Risk/No Reward)."},
        }
        
        prompt = "\nHow do you handle the unknown energy source?"
        # Pass the new options dict to get_user_choice
        choice = self.get_user_choice(prompt, options)
        if self.game_over_flag: return

        outcome = random.random()

        if choice == "1":
            # Best outcome if Logic or Engineering is high
            chance = 0.40 + self.copilot_bonus if self.copilot_skill in ["Logic", "Engineering"] else 0.20
            if outcome < chance:
                print("CRITICAL SUCCESS: You successfully stabilized the energy and harvested it!")
                self.current_integrity = self.max_integrity
                print("Hull fully repaired, systems optimized. Integrity restored to MAX!")
            else:
                self.take_damage(random.randint(40, 65))
                print("CATASTROPHIC FAILURE: The energy surge was unstable. Massive system damage.")
        
        elif choice == "2":
            # Moderately safe, influenced by shield strength
            if self.shield_strength > 15:
                print("SUCCESS: Smooth skirting maneuver. Minor turbulence.")
                self.take_damage(random.randint(1, 5))
            else:
                self.take_damage(random.randint(15, 30))
                print("FAILURE: Too close! The anomaly's edge still ripped into your hull.")
        
        elif choice == "3":
            # Guaranteed safety, but no reward
            print("SAFE: Full burn evasion successful. Time slightly lost, but the ship is safe.")
            
        print("--- End of Stage 3 ---")

    def martian_orbit_challenge(self):
        """Stage 4: Final challenge before landing."""
        self.location = "Mars Orbit"
        self.display_status()
        print("\nStage 4: MARTIAN ORBIT - LANDING SEQUENCE")
        print("Mars is in sight! However, the automated landing system requires a manual override with two complex parameters:")
        
        if self.current_integrity < 50:
             print("Due to low integrity, any error in the landing sequence will be fatal.")

        options = {
            "1": {"desc": "Use a high-risk atmospheric skip maneuver to save fuel and time."},
            "2": {"desc": "Execute a standard orbital insertion, demanding high precision and shield modulation."},
        }
        
        prompt = "\nHow do you approach the final descent?"
        # Pass the new options dict to get_user_choice
        choice = self.get_user_choice(prompt, options)
        if self.game_over_flag: return

        # Final success chance factors: Integrity, Shield, Copilot Skill
        base_chance = 0.50
        
        if choice == "1": # High risk (Pilot skill helps)
            chance = base_chance + (self.copilot_bonus if self.copilot_skill == "Piloting" else 0) - (1 - self.current_integrity / self.max_integrity) * 0.25 # Lower integrity penalizes
            
            if random.random() < chance:
                print("\nSUCCESS: The ship barely cleared the upper atmosphere, saving critical fuel and slowing perfectly.")
            else:
                damage = 60 if self.current_integrity > 50 else self.current_integrity + 10 # Fatal if low integrity
                self.take_damage(damage)
                print("CRITICAL FAILURE: Atmospheric turbulence tore into the hull during the skip maneuver.")

        elif choice == "2": # Standard approach (Shield/Engineering helps)
            chance = base_chance + (self.copilot_bonus if self.copilot_skill in ["Engineering", "Logic"] else 0) + (self.shield_strength / 50)
            
            if random.random() < chance:
                print("\nSUCCESS: A precise orbital burn and perfect shield modulation for entry. Flawless descent.")
            else:
                damage = 50 if self.current_integrity > 50 else self.current_integrity + 10 # Fatal if low integrity
                self.take_damage(damage)
                print("CRITICAL FAILURE: Shield modulation failed during entry, causing severe thermal stress.")
        
        print("--- End of Stage 4 ---")


    def start_game(self):
        """Initializes and runs the main game loop."""
        print("=" * 70)
        print("WELCOME TO MARTIAN ODYSSEY - A TEXT ADVENTURE")
        print("Your mission: Successfully pilot your vessel and crew to the surface of Mars.")
        print("Maintain your ship's integrity (HP) and make smart choices!")
        print("=" * 70)

        # Phase 1 & 2: Setup
        self.choose_ship()
        if self.game_over_flag: return
        self.choose_copilot()
        if self.game_over_flag: return
        
        print("\nLaunch Sequence Initiated...")
        print("T-Minus 10 seconds to burn. Good luck, Commander.")
        time.sleep(2)
        print("\n" + "#" * 50)
        print("LIFTOFF! The journey to Mars begins.")
        print("#" * 50)
        time.sleep(1.5)

        # Phase 3: Run Stages
        for stage_function in self.stages:
            if self.game_over_flag:
                break
            stage_function()
            time.sleep(1.5)

        # Phase 4: Final Outcome
        if self.game_over_flag:
            print("\n" + "=" * 50)
            print("GAME OVER - MISSION FAILURE")
            print(f"You perished in {self.location}. Mars remains a dream.")
            print("Final Integrity: 0 HP")
            print("=" * 50)
        else:
            self.martian_orbit_challenge() # Run the final stage

            if self.game_over_flag:
                print("\n" + "=" * 50)
                print("GAME OVER - MISSION FAILURE")
                print(f"You perished in {self.location} during the final approach.")
                print("Final Integrity: 0 HP")
                print("=" * 50)
            else:
                print("\n" + "=" * 70)
                print("VICTORY! MARS IS YOURS!")
                print(f"Your mission is complete. You successfully landed the {self.ship_name} on the Martian surface with {self.current_integrity} HP remaining.")
                print(f"The combined skill of you and {self.copilot_name} has secured a new future for humanity.")
                print("CONGRATULATIONS, COMMANDER!")
                print("=" * 70)


if __name__ == "__main__":
    game = MartianOdyssey()
    game.start_game()