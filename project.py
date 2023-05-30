from rich.console import Console
from time import sleep
from jokeapi import Jokes
import os
import asyncio
import aiohttp
import datetime
import art

console = Console()

def main():
    while True:
        try:
            answer = input("How can I help you?\n> ").lower()

            if answer:
                if "hi" in answer or "hello" in answer:
                    print(
                        "01001000 01100101 01101100 01101100 01101111 00100001\n"
                        "That's 'Hello!' in my language!\n")
                elif "bye" in answer or "goodbye" in answer:
                    print(
                        "01000010 01111001 01100101 00100001\n"
                        "That's 'Bye!' in my language!\n"
                    )
                    raise KeyboardInterrupt
                
                elif "time" in answer:
                    if "24" in answer:
                        print(f"The current time is {get_time24()}\n")
                    else:
                        print(f"The current time is {get_time12()}\n")
                elif "date" in answer:
                    print(f"Today's date is {get_date()}\n")
                elif "day" in answer:
                    print(f"Today is {get_day()}\n")
                elif "joke" in answer:
                    while True:
                        try:
                            asyncio.run(get_joke())
                            try:
                                ask = input("\nWant more (yes/no)? ").lower()
                                if ask in ["yes", "y"]:
                                    continue
                                elif ask in ["no", "n"]:
                                    break
                                else:
                                    raise ValueError()
                            except ValueError:
                                print("what was that again? ")
                        except aiohttp.ClientConnectorError:
                            print("Connection error. Cannot connect to the jokes server at the moment.\n"
                                  "Please make sure you have stable internet.\n")
                            break


                while True:
                    try:
                        ask = input("Anything else you want me to assist you with (yes/no)? ").strip().lower()
                        if ask in ["yes", "y"]:
                            break
                        elif ask in ["no", "n"]:
                            raise KeyboardInterrupt()
                        else:
                            raise ValueError()
                    except ValueError:
                        print("what was that again? ")

            else:
                with console.status("", spinner="simpleDots"):
                    sleep(3)
                pass

        except KeyboardInterrupt:
            with console.status("Okay, signing off...", spinner="dots2"):
                for i in range(10):
                    sleep(0.25)
            os.system("clear||cls")
            art.tprint("\nHave a nice day!", font="cybermedium")
            console.log("[bold green] Hope to see you soon!")
            break


def get_time12():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_time24():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y")

def get_day():
    now = datetime.datetime.now()
    return now.strftime("%A")

async def get_joke():
    j = await Jokes()
    joke = await j.get_joke()
    if joke["type"] == "single":
        print(joke["joke"])
    else:
        print(joke["setup"])
        print(joke["delivery"])




if __name__ == "__main__":
    with console.status("Please wait. Pixy is getting ready...", spinner="aesthetic", refresh_per_second=100):
            sleep(0.6)
    art.tprint("HELLO, I AM PIXY", font="cyberlarge")
    main()