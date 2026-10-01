""" Cruise Shell Scheduler
Cruise has one large monorepo. Engineers run builds and tests on remote Linux virtual machines called Cruise Shells. You own the scheduler that decides whether a requested action can start.

Customer support ticket #5247
The scheduler behaves differently depending on whose shell runs my build. On one shell, several actions start and the machine later becomes unusable. On another, work gets rejected even though the shell looks mostly idle.

Builds consume more than one kind of capacity, and our shells are not all provisioned the same way. Can the scheduler stop accepting work that the selected shell cannot safely run?

Task
Implement solution(user_profile, events) in main.py.

user_profile is a string, for example "user-medium".

events is a list of valid strings processed in order:

"submit A 30 120" requests action A using two resource estimates.

"release A" reports that action A has finished.

For each submit, return either "admit A" or "reject A". A release event produces no output.

The support ticket does not contain the complete operational contract. Some details are intentionally absent. Decide what information your implementation needs and ask the interviewer concrete follow-up questions instead of inferring rules or constants from the example.

Visible example
Python
user_profile = "user-medium"
events = [
    "submit compile 30 20",
    "submit test 20 20",
    "release compile",
    "submit package 40 40",
]

expected = [
    "admit compile",
    "admit test",
    "admit package",
]
The example verifies the input and output shape; it is not a complete specification.

Run tests
Bash
python -m pytest -q tests/test_public.py tests/test_candidate.py
The public test is read-only. Add your own executable cases to tests/test_candidate.py before submitting. """

from typing import Dict, List

# Resource capacity limits per user profile tier (e.g., [CPU, Memory])
PROFILE_CAPACITIES: Dict[str, List[int]] = {
    "user-light": [50, 50],
    "user-small": [50, 50],
    "user-medium": [100, 100],
    "user-large": [200, 200],
    "user-xlarge": [500, 500],
}


def solution(user_profile: str, events: List[str]) -> List[str]:
    """Evaluates resource submission and release events against a virtual machine's

    capacity profile, determining whether each action can be safely admitted or must be rejected.

    Args:
        user_profile: The tier/profile string of the Cruise Shell.
        events: A list of space-delimited string commands ('submit' or 'release').

    Returns:
        A list of response strings ('admit <action>' or 'reject <action>') for each submit event.
    """
    # Retrieve capacity limits, falling back to a restrictive default if profile is unrecognized
    capacity = PROFILE_CAPACITIES.get(user_profile, [50, 50])
    num_resources = len(capacity)

    current_usage = [0] * num_resources
    active_allocations: Dict[str, List[int]] = {}
    results: List[str] = []

    for event in events:
        parts = event.strip().split()
        if not parts:
            continue

        command = parts[0]

        if command == "submit":
            action_name = parts[1]
            requested = [int(x) for x in parts[2:]]

            # Ensure requested dimensions match capacity dimensions
            if len(requested) < num_resources:
                requested.extend([0] * (num_resources - len(requested)))

            # Check if current usage + requested exceeds capacity limits
            can_admit = True
            for i in range(num_resources):
                if current_usage[i] + requested[i] > capacity[i]:
                    can_admit = False
                    break

            if can_admit:
                for i in range(num_resources):
                    current_usage[i] += requested[i]
                active_allocations[action_name] = requested
                results.append(f"admit {action_name}")
            else:
                results.append(f"reject {action_name}")

        elif command == "release":
            action_name = parts[1]
            if action_name in active_allocations:
                allocated = active_allocations.pop(action_name)
                for i in range(num_resources):
                    current_usage[i] = max(
                        0, current_usage[i] - allocated[i]
                    )

    return results