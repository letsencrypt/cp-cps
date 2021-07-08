import io
import unittest

from no_stipulation import make_no_stipulations

document_input = io.StringIO(
"""---
title: Testament of Tester Testington
subtitle: Version 1.0
author:
  - Tester Testington
date: 3 June, 2021  
copyright: |
  Copyright 2021 Tester Testington of Test Town

  This work is licensed under the Conspicuous Attribution 4.0 NT for Workgroups Testing license.
---

# 1. LOREM

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

Some multi-paragraph

Content just to be

Safe

## 2.2 Labore

Something else.

""").readlines()

document_output = """---
title: Testament of Tester Testington
subtitle: Version 1.0
author:
  - Tester Testington
date: 3 June, 2021  
copyright: |
  Copyright 2021 Tester Testington of Test Town

  This work is licensed under the Conspicuous Attribution 4.0 NT for Workgroups Testing license.
---

# 1. LOREM

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

Some multi-paragraph

Content just to be

Safe

## 2.2 Labore

Something else.

"""

class TestMakeNoStipulations(unittest.TestCase):
    def test_make_no_stipulations_empty(self):
        self.assertEqual(make_no_stipulations(""), "")

    def test_make_no_stipulations_happy_path(self):
        self.maxDiff = None
        self.assertEqual(make_no_stipulations(document_input), document_output)
