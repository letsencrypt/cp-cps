import io
import unittest

from no_stipulation import make_no_stipulations

document_input = io.StringIO(
"""# 1. LOREM

## 1.1 Ipsum

### 1.1.1 Dolor

### 1.1.2 Sit

### 1.1.3 Amet

Some content.

### 1.1.4 Consectetur

### 1.1.5 Adipiscing

### 1.1.6 Elit

## 1.2 Sed

### 1.2.1 Do

Some multi-line

Content just to be

Safe

### 1.2.2 Eiusmod

Some more content, finally!

# 2. Tempor

## 2.1 Incididunt

### 2.1.1 Ut

## 2.2 Labore

"""
).readlines()

document_output = """# 1. LOREM

## 1.1 Ipsum

### 1.1.1 Dolor

No stipulation.

### 1.1.2 Sit

No stipulation.

### 1.1.3 Amet

Some content.

### 1.1.4 Consectetur

No stipulation.

### 1.1.5 Adipiscing

No stipulation.

### 1.1.6 Elit

No stipulation.

## 1.2 Sed

### 1.2.1 Do

Some multi-line

Content just to be

Safe

### 1.2.2 Eiusmod

Some more content, finally!

# 2. Tempor

## 2.1 Incididunt

### 2.1.1 Ut

No stipulation.

## 2.2 Labore

No stipulation.

"""

class TestMakeNoStipulations(unittest.TestCase):
    def test_make_no_stipulations_empty(self):
        self.assertEqual(make_no_stipulations(""), "\n\n")

    def test_make_no_stipulations_happy_path(self):
        self.maxDiff = None
        self.assertEqual(make_no_stipulations(document_input), document_output)
