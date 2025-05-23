# -*- coding: utf-8 -*-
"""Character_Encoding.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zQfM1LtBtIq7ubTE8yR8brpmFVAInC9B
"""

import pandas as pd
import numpy as np

# Helpful character module
import charset_normalizer

# Set seed for reproducibility
np.random.seed(0)

# Start with a string
before = "This is the euro symbol: |\?`"
type(before)

# Encode to a different encoding, replace characters that raise errors
after = before.encode("utf-8", errors="replace")
type(after)

after

before

print(after.decode("utf-8"))

# Try to decode our byte with ascii encoding
print(after.decode("ascii"))

# start with a string
before = "This is the euro symbol: $"

# Encode it to a different encoding, replacing characters that raise errors
after = before.encode("ascii", errors="replace")

# Convert it back to utf-8
print(after.decode("ascii"))

# We have lost the original underlying byte string! It's been
# replaced with the underlying byte string for the unknown character :(

kickstarter_2016 = pd.read_csv("/content/kickstarter_projects.csv")

# Look at the first ten thousand bytes to guess the character encoding
with open("/content/kickstarter_projects.csv", 'rb') as rawdata:
  result = charset_normalizer.detect(rawdata.read(10000))

# Check what the character encoding might be
print(result)

# Read in the file with the encoding detected by charset_normalizer
kickstarter_2016 = pd.read_csv("/content/kickstarter_projects.csv", encoding='utf-8')

# Look at the first few line
kickstarter_2016.head()

# Save our file (will be saved as UTF-8 by default)
kickstarter_2016.to_csv("ks-projects201801-utf8.csv")

