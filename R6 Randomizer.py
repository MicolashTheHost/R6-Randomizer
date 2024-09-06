import random
import tkinter as tk

# Data for the operators
attacking_operators = {
        "Striker": {"primary": ["M4", "M249"], "secondary": ["5.7 USG", "ITA12S"]},
        "Sledge": {"primary": ["M590A1", "L85A2"], "secondary": ["P226 Mk 25"]},
        "Thatcher": {"primary": ["AR33", "L85A2", "M590A1"], "secondary": ["P226 Mk 25"]},
        "Ash": {"primary": ["G36C", "R4-C"], "secondary": ["M45 MEUSOC", "5.7 USG"]},
        "Thermite": {"primary": ["M1014", "556XI"], "secondary": ["M45 MEUSOC", "5.7 USG"]},
        "Twitch": {"primary": ["F2", "417", "SG-CQB"], "secondary": ["P9", "LFP586"]},
        "Montagne": {"primary": ["Le Roc Extendable Shield"], "secondary": ["P9", "LFP586"]},
        "Glaz": {"primary": ["OTs-03"], "secondary": ["Gonne-6", "PMM", "Bearing 9"]},
        "Fuze": {"primary": ["6P41", "AK-12", "Ballistic Shield"], "secondary": ["GSH-18", "PMM"]},
        "Blitz": {"primary": ["G52-Tactical Shield"], "secondary": ["P12"]},
        "IQ": {"primary": ["AUG A2", "552 Commando", "G8A1"], "secondary": ["P12"]},
        "Buck": {"primary": ["C8-SFW", "CAMRS"], "secondary": ["Mk1 9mm"]},
        "Blackbeard": {"primary": ["Mk17 CQB", "SR-25"], "secondary": ["D-50"]},
        "Capitão": {"primary": ["PARA-308", "M249"], "secondary": ["PRB92", "Gonne-6"]},
        "Hibana": {"primary": ["Type-89", "SuperNova"], "secondary": ["P229", "Bearing 9"]},
        "Jackal": {"primary": ["C7E", "PDW9", "ITA12L"], "secondary": ["USP40", "ITA12S"]},
        "Ying": {"primary": ["T-95 LSW", "SIX12"], "secondary": ["Q-929"]},
        "Zofia": {"primary": ["LMG-E", "M762"], "secondary": ["RG15"]},
        "Dokkaebi": {"primary": ["Mk 14 EBR", "BOSG.12.2"], "secondary": ["C75 Auto", "SMG-12", "Gonne-6"]},
        "Lion": {"primary": ["V308", "417", "SG-CQB"], "secondary": ["P9", "LFP586"]},
        "Finka": {"primary": ["Spear .308", "6P41", "SASG-12"], "secondary": ["PMM", "GSH-18"]},
        "Maverick": {"primary": ["AR-15.50", "M4"], "secondary": ["1911 TACOPS"]},
        "Nomad": {"primary": ["AK-74M", "ARX200"], "secondary": [".44 Mag Semi-Auto", "PRB92"]},
        "Gridlock": {"primary": ["F90", "M249 SAW"], "secondary": ["Super Shorty", "SDP 9mm"]},
        "Nøkk": {"primary": ["FMG-9", "SIX12 SD"], "secondary": ["5.7 USG", "D-50"]},
        "Amaru": {"primary": ["G8A1", "SuperNova"], "secondary": ["SMG-11", "ITA12S", "Gonne-6"]},
        "Kali": {"primary": ["CSRX 300"], "secondary": ["SPSMG9", "C75 Auto", "P226 Mk 25"]},
        "Iana": {"primary": ["ARX200", "G36C"], "secondary": ["Mk1 9mm", "Gonne-6"]},
        "Ace": {"primary": ["AK-12", "M1014"], "secondary": ["P9"]},
        "Zero": {"primary": ["SC3000K", "MP7"], "secondary": ["5.7 USG", "Gonne-6"]},
        "Flores": {"primary": ["AR33", "SR-25"], "secondary": ["GSH-18"]},
        "Osa": {"primary": ["556XI", "PDW9"], "secondary": ["PMM"]},
        "Sens": {"primary": ["417", "POF-9"], "secondary": ["SDP 9mm"]},
        "Grim": {"primary": ["552 Commando", "SG-CQB"], "secondary": ["P229", "Bailiff 410"]},
        "Brava": {"primary": ["PARA-308", "CAMRS"], "secondary": ["USP40", "Super Shorty"]},
        "Ram": {"primary": ["R4-C", "LMG-E"], "secondary": ["ITA12S", "Mk1 9mm"]},
        "Deimos": {"primary": ["AK-74M", "M590A1"], "secondary": [".44 Vendetta"]}
    }

defending_operators = {
    "Sentry": {"primary": ["Commando 9", "M870"], "secondary": ["C75 Auto", "Super Shorty"]},
    "Smoke": {"primary": ["M590A1", "FMG-9"], "secondary": ["P226 Mk 25", "SMG-11"]},
    "Mute": {"primary": ["MP5K", "M590A1"], "secondary": ["P226 Mk 25"]},
    "Castle": {"primary": ["UMP45", "M1014"], "secondary": ["5.7 USG", "M45 MEUSOC", "Super Shorty"]},
    "Pulse": {"primary": ["UMP45", "M1014"], "secondary": ["5.7 USG", "M45 MEUSOC"]},
    "Doc": {"primary": ["MP5", "SG-CQB", "P90"], "secondary": ["LFP586", "P9", "Bailiff 410"]},
    "Rook": {"primary": ["MP5", "SG-CQB", "P90"], "secondary": ["LFP586", "P9"]},
    "Jäger": {"primary": ["M870", "416-C Carbine"], "secondary": ["P12"]},
    "Bandit": {"primary": ["MP7", "M870"], "secondary": ["P12"]},
    "Tachanka": {"primary": ["9x19VSN", "DP27"], "secondary": ["PMM", "GSH-18", "Bearing 9"]},
    "Kapkan": {"primary": ["9x19VSN", "SASG-12"], "secondary": ["PMM", "GSH-18"]},
    "Frost": {"primary": ["Super 90", "9mm C1"], "secondary": ["Mk1 9mm", "ITA12S"]},
    "Valkyrie": {"primary": ["MPX", "SPAS-12"], "secondary": ["D-50"]},
    "Caveira": {"primary": ["M12", "SPAS-15"], "secondary": ["Luison"]},
    "Echo": {"primary": ["MP5SD", "SuperNova"], "secondary": ["P229", "Bearing 9"]},
    "Mira": {"primary": ["VECTOR .45 ACP", "ITA12L"], "secondary": ["USP40", "Super Shorty"]},
    "Lesion": {"primary": ["SIX12 SD", "T-5 SMG"], "secondary": ["Q-929"]},
    "Ela": {"primary": ["Scorpion EVO 3 A1", "FO-12"], "secondary": ["RG15"]},
    "Vigil": {"primary": ["K1A", "BOSG.12.2"], "secondary": ["C75 Auto", "SMG-12"]},
    "Maestro": {"primary": ["ALDA 5.56", "ACS12"], "secondary": ["Bailiff 410", "Keratos .357"]},
    "Alibi": {"primary": ["Mx4 Storm", "ACS12"], "secondary": ["Bailiff 410", "Keratos .357"]},
    "Clash": {"primary": ["CCE Shield"], "secondary": ["SPSMG9", "Super Shorty", "P-10C"]},
    "Kaid": {"primary": ["AUG A3", "TCSG12"], "secondary": [".44 Mag Semi-Auto", "LFP586"]},
    "Mozzie": {"primary": ["Commando 9", "P10 RONI"], "secondary": ["USP40"]},
    "Warden": {"primary": ["M590A1", "MPX"], "secondary": ["P-10C", "SMG-12"]},
    "Goyo": {"primary": ["Vector .45 ACP", "TCSG12"], "secondary": ["P229"]},
    "Wamai": {"primary": ["AUG A2", "MP5K"], "secondary": ["D-40", "Keratos .357"]},
    "Oryx": {"primary": ["SPAS-12", "T-5 SMG"], "secondary": ["Bailiff 410", "USP40"]},
    "Melusi": {"primary": ["MP5", "Super 90"], "secondary": ["RG15", "ITA12S"]},
    "Aruni": {"primary": ["P10 Roni", "Mk 14 EBR"], "secondary": ["PRB92"]},
    "Thunderbird": {"primary": ["Spear .308", "SPAS-15"], "secondary": ["Bearing 9", "Q-929"]},
    "Thorn": {"primary": ["UZK50GI", "M870"], "secondary": ["1911 TACOPS", "C75 Auto"]},
    "Azami": {"primary": ["9X19VSN", "ACS12"], "secondary": ["D-50"]},
    "Solis": {"primary": ["P90", "ITA12S"], "secondary": ["SMG-11"]},
    "Fenrir": {"primary": ["MP7", "SASG-12"], "secondary": ["Bailiff 410", "5.7 USG"]},
    "Tubarao": {"primary": ["MPX", "AR-15.50"], "secondary": ["P226 Mk 25"]}
}

shield_operators = {"Montagne", "Blitz", "Clash"}

# Function to handle operator selection based on the chosen side
def select_side(side):
    include_shields = custom_yes_no_prompt("Shields", "Do you want to play Shields today? (No will filter out shields)")
    operator, weapons = get_random_operator(side, include_shields)

    if operator:
        result = f"Your random {side} operator is: {operator}"
        random_loadout = custom_yes_no_prompt("Random Loadout", "Do you want a random loadout?")

        if random_loadout:
            primary = random.choice(weapons["primary"])
            secondary = random.choice(weapons["secondary"])
            result += f"\nRandom Loadout - Primary: {primary}, Secondary: {secondary}"
        else:
            result += "\nUsing default loadout."

        show_message("Your Operator", result)

        friends_random = custom_yes_no_prompt("Friends", "Do your friends want random operators as well?")
        if friends_random:
            friend_results = "\nRandom Operators for your friends:"
            for i in range(4):  # Generate 4 extra operators
                friend_operator, friend_weapons = get_friend_operator(side)
                friend_primary = random.choice(friend_weapons["primary"])
                friend_secondary = random.choice(friend_weapons["secondary"])
                friend_results += f"\nFriend {i + 1} - Operator: {friend_operator} - Primary: {friend_primary}, Secondary: {friend_secondary}"

            show_message("Friends' Operators", friend_results)

    else:
        show_message("Error", "Invalid side selection!")

# Custom prompt to replace messagebox.askyesno
def custom_yes_no_prompt(title, message, parent=None):
    # Retrieve parent window position if available
    x = parent.winfo_x() + 20 if parent else 100
    y = parent.winfo_y() + 20 if parent else 100

    prompt_window = tk.Toplevel()
    prompt_window.title(title)
    # Set window position relative to parent
    prompt_window.geometry(f"400x300+{x}+{y}")

    label = tk.Label(prompt_window, text=message, font=("Arial", 14), wraplength=350)
    label.pack(pady=20)

    answer = tk.BooleanVar()

    def on_yes():
        answer.set(True)
        prompt_window.destroy()

    def on_no():
        answer.set(False)
        prompt_window.destroy()

    yes_button = tk.Button(prompt_window, text="Yes", command=on_yes, font=("Arial", 14), width=10, height=1)
    yes_button.pack(side="left", padx=20, pady=10)

    no_button = tk.Button(prompt_window, text="No", command=on_no, font=("Arial", 14), width=10, height=1)
    no_button.pack(side="right", padx=20, pady=10)

    prompt_window.wait_window()
    return answer.get()

# GUI for side selection
def choose_side():
    side_selection = tk.Tk()
    side_selection.title("Select Side")
    side_selection.geometry("400x300")

    label = tk.Label(side_selection, text="What side are you on?", font=("Arial", 16))
    label.pack(pady=20)

    attack_button = tk.Button(side_selection, text="Attack", command=lambda: [side_selection.destroy(), select_side("attack")],
                              width=15, height=2, font=("Arial", 14))
    attack_button.pack(pady=10)

    defense_button = tk.Button(side_selection, text="Defense", command=lambda: [side_selection.destroy(), select_side("defense")],
                               width=15, height=2, font=("Arial", 14))
    defense_button.pack(pady=10)

    side_selection.mainloop()

# GUI-related functions
def show_message(title, message, parent=None):
    # Retrieve parent window position if available
    x = parent.winfo_x() + 20 if parent else 100
    y = parent.winfo_y() + 20 if parent else 100

    message_window = tk.Toplevel()
    message_window.title(title)
    # Set window position relative to parent
    message_window.geometry(f"400x300+{x}+{y}")

    label = tk.Label(message_window, text=message, font=("Arial", 14), wraplength=350)
    label.pack(pady=20)

    ok_button = tk.Button(message_window, text="OK", command=message_window.destroy, font=("Arial", 14), width=10, height=1)
    ok_button.pack(pady=10)

    message_window.wait_window()

def get_random_operator(side, include_shields):
    # Filter operators based on user preference for shields
    attack_ops = {
        "Striker": {"primary": ["M4", "M249"], "secondary": ["5.7 USG", "ITA12S"]},
        "Sledge": {"primary": ["M590A1", "L85A2"], "secondary": ["P226 Mk 25"]},
        "Thatcher": {"primary": ["AR33", "L85A2", "M590A1"], "secondary": ["P226 Mk 25"]},
        "Ash": {"primary": ["G36C", "R4-C"], "secondary": ["M45 MEUSOC", "5.7 USG"]},
        "Thermite": {"primary": ["M1014", "556XI"], "secondary": ["M45 MEUSOC", "5.7 USG"]},
        "Twitch": {"primary": ["F2", "417", "SG-CQB"], "secondary": ["P9", "LFP586"]},
        "Montagne": {"primary": ["Le Roc Extendable Shield"], "secondary": ["P9", "LFP586"]},
        "Glaz": {"primary": ["OTs-03"], "secondary": ["Gonne-6", "PMM", "Bearing 9"]},
        "Fuze": {"primary": ["6P41", "AK-12", "Ballistic Shield"], "secondary": ["GSH-18", "PMM"]},
        "Blitz": {"primary": ["G52-Tactical Shield"], "secondary": ["P12"]},
        "IQ": {"primary": ["AUG A2", "552 Commando", "G8A1"], "secondary": ["P12"]},
        "Buck": {"primary": ["C8-SFW", "CAMRS"], "secondary": ["Mk1 9mm"]},
        "Blackbeard": {"primary": ["Mk17 CQB", "SR-25"], "secondary": ["D-50"]},
        "Capitão": {"primary": ["PARA-308", "M249"], "secondary": ["PRB92", "Gonne-6"]},
        "Hibana": {"primary": ["Type-89", "SuperNova"], "secondary": ["P229", "Bearing 9"]},
        "Jackal": {"primary": ["C7E", "PDW9", "ITA12L"], "secondary": ["USP40", "ITA12S"]},
        "Ying": {"primary": ["T-95 LSW", "SIX12"], "secondary": ["Q-929"]},
        "Zofia": {"primary": ["LMG-E", "M762"], "secondary": ["RG15"]},
        "Dokkaebi": {"primary": ["Mk 14 EBR", "BOSG.12.2"], "secondary": ["C75 Auto", "SMG-12", "Gonne-6"]},
        "Lion": {"primary": ["V308", "417", "SG-CQB"], "secondary": ["P9", "LFP586"]},
        "Finka": {"primary": ["Spear .308", "6P41", "SASG-12"], "secondary": ["PMM", "GSH-18"]},
        "Maverick": {"primary": ["AR-15.50", "M4"], "secondary": ["1911 TACOPS"]},
        "Nomad": {"primary": ["AK-74M", "ARX200"], "secondary": [".44 Mag Semi-Auto", "PRB92"]},
        "Gridlock": {"primary": ["F90", "M249 SAW"], "secondary": ["Super Shorty", "SDP 9mm"]},
        "Nøkk": {"primary": ["FMG-9", "SIX12 SD"], "secondary": ["5.7 USG", "D-50"]},
        "Amaru": {"primary": ["G8A1", "SuperNova"], "secondary": ["SMG-11", "ITA12S", "Gonne-6"]},
        "Kali": {"primary": ["CSRX 300"], "secondary": ["SPSMG9", "C75 Auto", "P226 Mk 25"]},
        "Iana": {"primary": ["ARX200", "G36C"], "secondary": ["Mk1 9mm", "Gonne-6"]},
        "Ace": {"primary": ["AK-12", "M1014"], "secondary": ["P9"]},
        "Zero": {"primary": ["SC3000K", "MP7"], "secondary": ["5.7 USG", "Gonne-6"]},
        "Flores": {"primary": ["AR33", "SR-25"], "secondary": ["GSH-18"]},
        "Osa": {"primary": ["556XI", "PDW9"], "secondary": ["PMM"]},
        "Sens": {"primary": ["417", "POF-9"], "secondary": ["SDP 9mm"]},
        "Grim": {"primary": ["552 Commando", "SG-CQB"], "secondary": ["P229", "Bailiff 410"]},
        "Brava": {"primary": ["PARA-308", "CAMRS"], "secondary": ["USP40", "Super Shorty"]},
        "Ram": {"primary": ["R4-C", "LMG-E"], "secondary": ["ITA12S", "Mk1 9mm"]},
        "Deimos": {"primary": ["AK-74M", "M590A1"], "secondary": [".44 Vendetta"]}
    }


    defense_ops = {
    "Sentry": {"primary": ["Commando 9", "M870"], "secondary": ["C75 Auto", "Super Shorty"]},
    "Smoke": {"primary": ["M590A1", "FMG-9"], "secondary": ["P226 Mk 25", "SMG-11"]},
    "Mute": {"primary": ["MP5K", "M590A1"], "secondary": ["P226 Mk 25"]},
    "Castle": {"primary": ["UMP45", "M1014"], "secondary": ["5.7 USG", "M45 MEUSOC", "Super Shorty"]},
    "Pulse": {"primary": ["UMP45", "M1014"], "secondary": ["5.7 USG", "M45 MEUSOC"]},
    "Doc": {"primary": ["MP5", "SG-CQB", "P90"], "secondary": ["LFP586", "P9", "Bailiff 410"]},
    "Rook": {"primary": ["MP5", "SG-CQB", "P90"], "secondary": ["LFP586", "P9"]},
    "Jäger": {"primary": ["M870", "416-C Carbine"], "secondary": ["P12"]},
    "Bandit": {"primary": ["MP7", "M870"], "secondary": ["P12"]},
    "Tachanka": {"primary": ["9x19VSN", "DP27"], "secondary": ["PMM", "GSH-18", "Bearing 9"]},
    "Kapkan": {"primary": ["9x19VSN", "SASG-12"], "secondary": ["PMM", "GSH-18"]},
    "Frost": {"primary": ["Super 90", "9mm C1"], "secondary": ["Mk1 9mm", "ITA12S"]},
    "Valkyrie": {"primary": ["MPX", "SPAS-12"], "secondary": ["D-50"]},
    "Caveira": {"primary": ["M12", "SPAS-15"], "secondary": ["Luison"]},
    "Echo": {"primary": ["MP5SD", "SuperNova"], "secondary": ["P229", "Bearing 9"]},
    "Mira": {"primary": ["VECTOR .45 ACP", "ITA12L"], "secondary": ["USP40", "Super Shorty"]},
    "Lesion": {"primary": ["SIX12 SD", "T-5 SMG"], "secondary": ["Q-929"]},
    "Ela": {"primary": ["Scorpion EVO 3 A1", "FO-12"], "secondary": ["RG15"]},
    "Vigil": {"primary": ["K1A", "BOSG.12.2"], "secondary": ["C75 Auto", "SMG-12"]},
    "Maestro": {"primary": ["ALDA 5.56", "ACS12"], "secondary": ["Bailiff 410", "Keratos .357"]},
    "Alibi": {"primary": ["Mx4 Storm", "ACS12"], "secondary": ["Bailiff 410", "Keratos .357"]},
    "Clash": {"primary": ["CCE Shield"], "secondary": ["SPSMG9", "Super Shorty", "P-10C"]},
    "Kaid": {"primary": ["AUG A3", "TCSG12"], "secondary": [".44 Mag Semi-Auto", "LFP586"]},
    "Mozzie": {"primary": ["Commando 9", "P10 RONI"], "secondary": ["USP40"]},
    "Warden": {"primary": ["M590A1", "MPX"], "secondary": ["P-10C", "SMG-12"]},
    "Goyo": {"primary": ["Vector .45 ACP", "TCSG12"], "secondary": ["P229"]},
    "Wamai": {"primary": ["AUG A2", "MP5K"], "secondary": ["D-40", "Keratos .357"]},
    "Oryx": {"primary": ["SPAS-12", "T-5 SMG"], "secondary": ["Bailiff 410", "USP40"]},
    "Melusi": {"primary": ["MP5", "Super 90"], "secondary": ["RG15", "ITA12S"]},
    "Aruni": {"primary": ["P10 Roni", "Mk 14 EBR"], "secondary": ["PRB92"]},
    "Thunderbird": {"primary": ["Spear .308", "SPAS-15"], "secondary": ["Bearing 9", "Q-929"]},
    "Thorn": {"primary": ["UZK50GI", "M870"], "secondary": ["1911 TACOPS", "C75 Auto"]},
    "Azami": {"primary": ["9X19VSN", "ACS12"], "secondary": ["D-50"]},
    "Solis": {"primary": ["P90", "ITA12S"], "secondary": ["SMG-11"]},
    "Fenrir": {"primary": ["MP7", "SASG-12"], "secondary": ["Bailiff 410", "5.7 USG"]},
    "Tubarao": {"primary": ["MPX", "AR-15.50"], "secondary": ["P226 Mk 25"]}
}


    if side == "attack":
        operator = random.choice(list(attack_ops.keys()))
        return operator, attack_ops[operator]
    elif side == "defense":
        operator = random.choice(list(defense_ops.keys()))
        return operator, defense_ops[operator]
    else:
        return None, None

def get_friend_operator(side):
    # Select random operators for friends, without filtering shields
    if side == "attack":
        operator = random.choice(list(attacking_operators.keys()))
        return operator, attacking_operators[operator]
    elif side == "defense":
        operator = random.choice(list(defending_operators.keys()))
        return operator, defending_operators[operator]
    else:
        return None, None

def main():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Start the side selection GUI
    choose_side()

if __name__ == "__main__":
    main()