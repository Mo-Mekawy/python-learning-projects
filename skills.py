'''add, delete, update and show skills and thier progress from database'''
import sqlite3
import sys
import os


USER_ID = 1
# change the current working directory to this path then create the database and connect to it
os.chdir(r"F:\programing\python\python programs\Elzero Web School") # change this path to a real path on your pc to get the code working
db = sqlite3.connect("skills.db")
# make tables and fields
db.execute(
    "CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT, password TEXT)")
db.execute(
    "CREATE TABLE IF NOT EXISTS skills (user_id INTEGER, name TEXT, progress INTEGER)")

# get max id
cur = db.cursor()
cur.execute("SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1")

user_id = cur.fetchone()
if user_id:
    user_id = user_id[0]
# get username and password and pass him if it exists
user_name = input("Username: ").strip().capitalize()
password = input("Password: ").strip()
cur = db.cursor()
cur.execute("SELECT user_id FROM users WHERE name=? AND password=?",
            (user_name, password))
exists = cur.fetchone()
if exists:
    USER_ID = exists[0]
else:
    if input("you aren't registered do you want to sign up (y/n)? ").strip().capitalize() in ("Y", "Yes"):
        while True:
            try:
                user_name = input("Username: ").strip().capitalize()
                if not (4 < len(user_name) < 16):
                    print(
                        "user name must be less than 16 and more than 4 character including digits and sympols")
                    continue
            except ValueError:
                print("Invalid user name")
                continue
            break
        password = input("Password: ").strip()
        # sign up the user
        if user_id:
            USER_ID = user_id + 1
        cur = db.cursor()
        cur.execute("INSERT INTO users (user_id, name, password) VALUES (?,?,?)",
                    (USER_ID, user_name, password))
    else:
        db.close()
        sys.exit()


# set up the cursor
cursor = db.cursor()


def main():
    '''run every function on the option given by the user'''
    answer = "Yes"
    while answer == "Yes" or answer == "Y":
        # get option
        option = get_option()
        match option:
            case "s":
                skill_count, skills = show_skills()
                print(f"\nyou have {skill_count} skills")
                if skill_count > 0:
                    print(f"skills and progress:")
                    print(skills)
            case "a":
                add_skill()
            case "d":
                delete_skill()
            case "u":
                update_skill()
            case "q":
                db.commit()
                db.close()
                sys.exit("successfully closed.")
        while True:
            answer = input(
                "Do you want to continue (y/n)? ").strip().capitalize()
            if answer not in ["Yes", "Y", "No", "N"]:
                print("Invalid command")
            else:
                break
    # save changes and close tha connection
    db.commit()
    db.close()


def get_option():
    '''get operating option from user'''
    input_message = """
What do you want to do?
"s" => Show all skills
"a" => Add new skill
"d" => Delete a skill
"u" => Update skill progress
"q" => Quite the app
Choose option:"""
    options = ["s", "a", "d", "u", "q"]

    user_input = input(input_message).strip().lower()  # get option from user
    while True:  # validate user input
        if len(user_input) != 1 or user_input not in options:

            print(f"\nOption are only {options}")
            user_input = input(input_message).strip().lower()
        else:
            return user_input


def show_skills():
    '''show skills in database'''
    skills = ""  # the string that contain all skills
    cursor.execute(
        "SELECT name, progress FROM skills WHERE user_id=?", (USER_ID,))
    data = cursor.fetchall()
    skills_count = len(data)  # get the number of skills

    for skill in data:
        name, progress = skill
        skills += f"{name}===>{progress}%\n"  # add the skill in good format
    return skills_count, skills


def add_skill():
    '''prompt the user for a skill and add it to database'''
    # get skill name from user and make sure it is not already in the database
    while True:
        skill_name = input("Skill Name: ").strip().capitalize()
        cursor.execute(
            "SELECT name FROM skills WHERE name=? AND user_id=?", (skill_name, USER_ID))
        if cursor.fetchone():
            print(
                f"Skill {skill_name} already exists please enter another name")
        else:
            break
    # get skill progress from user and validate it
    while True:
        try:
            progress = int(input("Skill Progress: ").strip())
            break
        except ValueError:
            print("please enter an integer")

    # add skill name and progress to their fields in database
    cursor.execute(
        "INSERT INTO skills (name, progress, user_id) VALUES (?, ?, ?)", (
            skill_name, progress, USER_ID))
    print(f"skill {skill_name} is added with progress of {progress}%")


def delete_skill():
    '''prompt the user for the name of the skill to be deleted'''
    # get skill name to delete
    skill_name = input("Skill Name: ").strip().capitalize()
    # ensure that the skill is in database
    skills = []
    result = show_skills()[1].splitlines()
    for item in result:
        skills.append(item.split("===>")[0])

    if skill_name in skills:
        cursor.execute(
            "DELETE FROM skills WHERE user_id=? AND name=?", (
                USER_ID, skill_name)
        )
        print(f"skill {skill_name} is deleted successfully")
    else:
        print(f"skill {skill_name} is not found")


def update_skill():
    '''prompt the user for the name of the skill to be updated'''
    # get skill name to update the new progress
    skill_name = input("Skill Name: ").strip().capitalize()
    # ensure that the skill is in database
    skills = []
    result = show_skills()[1].splitlines()
    for item in result:
        skills.append(item.split("===>")[0])

    if skill_name not in skills:
        print(f"skill {skill_name} is not found")
        return

    # get skill progress from user and validate it
    while True:
        try:
            progress = int(input("Skill Progress: ").strip())
            break
        except ValueError:
            print("please enter an integer")
    # update the progress field
    cursor.execute(
        "UPDATE skills SET progress=? WHERE user_id=? AND name=?", (
            progress, USER_ID, skill_name))
    print(f"skill {skill_name} is updated successfully")


if __name__ == "__main__":
    main()
