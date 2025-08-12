import importlib
import random
import sys



VENDORS = {"1": "cisco", "2": "juniper"}
CATEGORIES = {"1": "routing", "2": "switching", "3": "os"}
TOPICS = {
    "cisco": {
        "routing": ["general_eigrp", "operational_eigrp", "config_eigrp", "general_ospf", "operational_ospf", "config_ospf", "general_bgp", "operational_bgp", "config_bgp"],
        "switching": ["vlan"],
        "os": ["ios_basics"]
    },
    "juniper": {
        "routing": ["general_ospf", "operational_ospf", "config_ospf", "general_bgp", "operational_bgp", "config_bgp"],
        "switching": ["vlan"],
        "os": ["junos_basics"]
    }
}


def select_option(options, prompt):
    while True:
        #With the items method we make an instance (object) of the class dict_items (i.e  VENDOR.items() returns: dict_items([('1', 'cisco'), ('2', 'juniper')]) )
        for key, value in options.items():
            print(f"{key}) {value}")
        choice = input(prompt).strip()
        #Choice is a string. So choice in options is like: "1" in VENDOR  (this is true for this example).
        if choice in options:
            return options[choice]
        print("Invalid choice, try again.")

def run_quiz():
    vendor = select_option(VENDORS, "Choose Vendor: ")
    category = select_option(CATEGORIES, "Choose Category: ")
    #Get TOPICS[vendor][category], but safely, without a KeyError. If the key does not exits it returns an empty dict {}. 
    available_topics = TOPICS.get(vendor, {}).get(category, [])
    if not available_topics:
        print("No topics available for this selection.")
        return
    
    print("\nAvailable topics:")
    for i, t in enumerate(available_topics, 1):
        print(f"{i}) {t}")
    
    try:
        topic_index = int(input("Choose Topic: ")) - 1
        topic = available_topics[topic_index]
    except (ValueError, IndexError):
        print("Invalid topic selection.")
        return
    
    quiz_topic(vendor, category, topic)


def load_questions(vendor, category, topic):
    try:
        module_path = f"questions.{vendor}.{category}.{topic}"  # this is equivalent with "module_path = 'questions.{}.{}.{}'.format('cisco', 'routing', 'config_ospf')"  module_path = 'questions.cisco.routing.config_ospf'
        module = importlib.import_module(module_path)           # this returns type(module) = module
        return module.questions                                 # this returns the dictionary (within the module) 'questions' within the package of <module 'questions.cisco.routing.config_ospf' from ..\\questions\\cisco\\routing\\config_ospf.py'>
    except ModuleNotFoundError:                                 # within module variable this is now has the path to the package ..\\questions\\cisco\\routing\\config_ospf.py.
        print("❌ Error: Topic not found.")
        return None

def quiz_topic(vendor, category, topic):
    questions = load_questions(vendor, category, topic)
    if not questions:                                           
        return
                                                                # make a list of questions.keys(). This is an instance (object) of the <class 'dict_keys'>. 
    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    for q in question_keys:
                                                               #Grep the value of the data key, which is a dict. 
        data = questions[q]
                                                               #Grep the value of data["answer"]
        correct_answer = data["answer"]

        print(f"\nQuestion: {q}")                              # this is equivalent with print('question: .{}'.format(q))
        answer = input("Your answer: ").strip()

        if answer.lower() == correct_answer.lower():
            print("✅ Correct!")
            # Check if notes exist. 1) if "notes" is a key in dict. data and if so data["notes"] the value must not be empty. 
            if "notes" in data and data["notes"]:
                print(f"📝 Notes: {data['notes']}")
        else:
            print(f"❌ Incorrect! Correct answer: {correct_answer}")

        next_action = input("Press [Enter] for next, [m]enu, or [e]xit: ").strip().lower()
        if next_action == "m":
            return
        elif next_action == "e":
            sys.exit("Goodbye!")                              # is 'enter' is present the if logic stops in this local hierarchy. The for loop in the higher hierarchy is instanstiated. 


def main_menu():
    while True:
        print("\n--- Vendor Selection ---")
        vendor = select_option(VENDORS, "Choose a vendor: ")
        if not vendor:
            print("Goodbye!")
            break                                             # break out of the while loop. 

        print("\n--- Category Selection ---")
        category = select_option(CATEGORIES, "Choose a category: ")
        if not category:
            continue                                         # instansiate the while loop again. 

        topic_list = TOPICS.get(vendor, {}).get(category, [])  # first level of topic_list is here the dict. with key, value: 'category':['topic1', 'topic2', 'topic3']. The second level gives the list of the topics. 
        if not topic_list:
            print("⚠ No topics available for this selection.")
            continue

        while True:
            print("\n--- Topic Selection ---")
            for i, topic_name in enumerate(topic_list, 1):    # Docstring of enumerate. See enumerate.__doc__ 
                print(f"{i}. {topic_name.replace('_', ' ').capitalize()}")
            print("0. Back")

            topic_choice = input("Choose a topic (number or name): ").strip()
            if topic_choice == "0":
                break

            # Match by number
            if topic_choice.isdigit():
                index = int(topic_choice) - 1
                if 0 <= index < len(topic_list):
                    selected_topic = topic_list[index]
                    quiz_topic(vendor, category, selected_topic)  # ✅ Run quiz
                else:
                    print("Invalid topic number.")
            # Match by name
            else:
                matches = [t for t in topic_list if t.lower() == topic_choice.lower()]
                if matches:
                    selected_topic = matches[0]
                    quiz_topic(vendor, category, selected_topic)  # ✅ Run quiz
                else:
                    print("Invalid topic name.")



if __name__ == "__main__":
    main_menu()
