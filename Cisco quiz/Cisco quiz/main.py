import importlib
import random
import sys

TOPICS = {
    "1": "general_eigrp",
    "2": "operational_eigrp",
    "3": "config_eigrp",
    "4": "general_ospf",
    "5": "operational_ospf",     
    "6": "config_ospf",
    "7": "general_bgp",
    "8": "operational_bgp",
    "9": "config_bgp"
}

def load_questions(topic_name):
    try:
        module = importlib.import_module(f"questions.{topic_name}")
        return module.questions
    except (ModuleNotFoundError, AttributeError):
        print("Topic file not found or improperly formatted.")
        return {}

def quiz_topic(topic):
    questions = load_questions(topic)
    if not questions:
        return

    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    for q in question_keys:
        print(f"\nQuestion: {q}")
        user_answer = input("Your answer: ").strip()

        # Support new structure: dict with "answer" and optional "note"
        correct_info = questions[q]

        if isinstance(correct_info, dict):
            correct_answer = correct_info["answer"]
            notes = correct_info.get("notes")
        else:
            correct_answer = correct_info
            notes = None

        if user_answer.lower() == correct_answer.lower():
            print("✅ Correct!")
            if notes:
                print(f"💡 Note: {notes}")
        else:
            print(f"❌ Incorrect! Correct answer: {correct_answer}")

        next_action = input("Press [Enter] for next, [m]enu, or [e]xit: ").strip().lower()
        if next_action == "m":
            return
        elif next_action == "e":
            sys.exit("Goodbye!")

def main_menu():
    while True:
        print("\n--- Cisco Exam Quiz ---")
        for key, value in TOPICS.items():
            if value != "exit":
                print(f"{key}. {value.upper()}")
        print("0. Exit")

        choice = input("Choose a topic: ").strip()
        if choice in TOPICS:
            if choice == "0":
                print("Good luck with your exam!")
                break
            else:
                quiz_topic(TOPICS[choice])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
