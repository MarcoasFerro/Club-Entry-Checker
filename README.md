# Club Entry Checker

Python program that checks whether a person can enter a club, 
applying minimum age rules and a rule for underage guests with a companion.

## What it does

- Asks for the person's age
- Asks whether they are accompanied
- If accompanied, also checks the companion's age
- Grants or denies entry based on the rules:
  - Alone: must be 18 or older
  - Accompanied: both the person and the companion must be 18 or older

## Why I built it

Started as a course exercise, but I decided to go beyond what was asked 
by adding the companion-age rule as a second business rule, instead of 
checking only the minimum age.

## How to run

```bash
python balada.py
```

## Next steps

- [ ] Store each checked person's data in a list
- [ ] Allow checking multiple guests in sequence without restarting
- [ ] Validate invalid input (e.g. answers other than "sim"/"não")
