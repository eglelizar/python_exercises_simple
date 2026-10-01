import pytest
from main import solution


def test_example_case() -> None:
  """Verifies normal execution flow based on the problem statement example."""
  user_profile = "user-medium"
  events = [
      "submit compile 30 20",
      "submit test 20 20",
      "release compile",
      "submit package 40 40",
  ]
  expected = ["admit compile", "admit test", "admit package"]
  assert solution(user_profile, events) == expected


def test_rejection_due_to_capacity() -> None:
  """Ensures tasks exceeding single-dimension or multi-dimension limits are rejected."""
  user_profile = "user-small"  # Capacity [50, 50]
  events = ["submit heavy_task 60 10", "submit light_task 20 20"]
  expected = ["reject heavy_task", "admit light_task"]
  assert solution(user_profile, events) == expected


def test_release_frees_capacity() -> None:
  """Verifies that releasing an active task properly restores available capacity."""
  user_profile = "user-small"  # Capacity [50, 50]
  events = [
      "submit task1 40 40",
      "submit task2 20 20",  # Rejected: 40 + 20 > 50
      "release task1",
      "submit task2 20 20",  # Admitted: capacity freed
  ]
  expected = ["admit task1", "reject task2", "admit task2"]
  assert solution(user_profile, events) == expected


def test_empty_events() -> None:
  """Handles edge case of an empty event stream gracefully."""
  assert solution("user-medium", []) == []


def test_unknown_profile_defaults() -> None:
  """Verifies behavior when an unknown user profile is provided."""
  user_profile = "unknown-tier"  # Defaults to [1000, 1000]
  events = ["submit massive_job 500 500", "submit giant_job 600 600"]
  expected = ["admit massive_job", "reject giant_job"]
  assert solution(user_profile, events) == expected


def test_release_nonexistent_action() -> None:
  """Ensures releasing an inactive or unknown task does not throw errors."""
  events = ["release ghost_task", "submit normal_task 10 10"]
  expected = ["admit normal_task"]
  assert solution("user-medium", events) == expected