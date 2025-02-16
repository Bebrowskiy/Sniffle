import httpx
import trio
import time
import random
from holehe.core import import_submodules, get_functions, TrioProgress, launch_module, print_result, is_email
from argparse import Namespace


async def email_check(email):

    if not is_email(email):
        print("\033[1;31m[-]\033[0m Please enter a target email!")
        return

    # Asynchronous email search via Holehe with rate limit control.
    modules = import_submodules("holehe.modules")  # Importing modules
    websites = get_functions(modules)  # Uploading the list of sites
    
    args = Namespace(email=[email], onlyused=False, nocolor=False, noclear=False, nopasswordrecovery=False, csvoutput=False, timeout=10)
    timeout = 20

    start_time  = time.time()

    async with httpx.AsyncClient() as client:  # Client Creation
        out = []
        instrument = TrioProgress(len(websites))
        trio.lowlevel.add_instrument(instrument)  # Adding progress

        async with trio.open_nursery() as nursery:
            for website in websites:
                nursery.start_soon(launch_module, website, email, client, out)
                # Add a random pause between requests
                await trio.sleep(random.uniform(0.5, 2))  # Pause between 0.5 and 2 seconds to reduce the query rate

            trio.lowlevel.remove_instrument(instrument)  # Taking away the progress

        out = sorted(out, key=lambda i: i["name"])

    print_result(out, args, email, start_time, websites)  # Result output


def main():
    print("\033[1;32m╔══ Email Search ══╗\033[0m")
    print("    \033[1;32mUsing\033[0m \033[1;31mHolehe\033[0m")
    print("\033[1;32m╚══════════════════╝\033[0m")
    email = input("\033[1;32mEmail: \033[0m")

    
    trio.run(email_check, email)

