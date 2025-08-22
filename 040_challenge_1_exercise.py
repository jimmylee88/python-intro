# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging than the example.

# Write a function that takes a list of words and returns a report of all the
# words that are longer than 10 characters but don't contain a hyphen. If those
# words are longer than 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  # Filter in words that are 10 chars long
  long_words = extract_long_words(words)
  # Filter out words containing hyphens
  without_hyphens = reject_hyphenated_words(long_words)
  # Map ones over 15 chars to the shortened v with ellipsis added to the end
  shortened_if_longer = shorten_very_long_words(without_hyphens)
  # Summarise to a string report
  return format_long_word_report(shortened_if_longer)

def extract_long_words(words):
  long_words = []
  for word in words:
    if len(word) > 10:
      long_words.append(word)
  return long_words

def reject_hyphenated_words(words):
  unhyphenated_words = []
  for word in words:
    if "-" not in word:
      unhyphenated_words.append(word)
  return unhyphenated_words

def shorten_very_long_words(words):
  processed_words = []
  for word in words:
    if len(word) > 15:
      shortened_word = word[0:15] + "..."
      processed_words.append(shortened_word)
    else: 
      processed_words.append(word)
  return processed_words

def format_long_word_report(long_words):
  report = "These words are quite long: "
  return report + ", ".join(long_words)


check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
