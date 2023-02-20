# placepicker

From a provided list of restaurants or things, you're given two methods to arrive at a destination.

For the time being, this application will not store user data. It will have hardcoded locations for the sole purpose of helping me and my friends pick a location at which to eat food.

## Two Modes

There are three modes by which a user can arrive at a location. _Filtered Random Location_ or _Pick and Pass_. The names are decently descriptive but here is how they work.

### Filtered Random Location Mode

The user is presented with a list of locations. They will eliminate the locations that they are certain they do not want to go to. When they are ready, they can let pseudorandomness decide their fate and choose a random location from the remaining list. If they are unsatisfied with the result, they can choose to reroll or to blacklist the selection and reroll.

There is an alternate version of this mode where the process is somewhat inverted. The user starts with an empty list and adds candidates to it. Then they choose to let the computer choose which place they will go.

### Pick and Pass

In this mode, the user begins with a list of candidates. The user(s) will eliminate an agreed upon number of candidates before passing it to the next person they're with to do the same. Eventually, there will only be one location left.

Future upgrades:
- Location candidates are stored in a database rather than being hardcoded in a Python object
- User authentication and user specific data
- Maybe get ChatGPT to generate a message for the user about the place selected

## Stack

- SvelteKit or NextJS
- Tailwindcss
- Python
- FastAPI
- PostgreSQL database

## Maintainers (Roles could evolve)

Jack Branch
- Project engineer
- Frontend developer

Coby Colvin
- Backend developer
