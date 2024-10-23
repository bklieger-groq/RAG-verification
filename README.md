# RAG-verification
Technique for verifying RAG citations

### Quickstart

~~~
python3 -m venv venv
~~~
~~~
source venv/bin/activate
~~~
~~~
pip3 install -r requirements.txt
~~~
~~~
export GROQ_API_KEY=gsk...
~~~
~~~
python3 app.py
~~~

```
Results Comparison:
Citation-based accuracy: 100.00%
Direct answer accuracy: 94.74%

Citation Based Results:
Accuracy: 100.00%
Correct: 19/19

CITATION
Question: What was the key insight Paul Graham had about making online stores look legitimate?
Correct Answer: C. Getting page layouts, fonts, and colors right
LLM Answer: C. Getting page layouts, fonts, and colors right
Correct: True

Citations:
  1: It helped to have studied art, because the main goal of an online store builder is to make users look legit, and the key to looking legit is high production values.
  2: If you get page layouts and fonts and colors right, you can make a guy running a store out of his bedroom look more legit than a big company.
Explanation: Based on the citations, the key insight Paul Graham had about making online stores look legitimate is having high production values, which includes getting page layouts, fonts, and colors right [1]. This is because high production values can make a small online store look more legitimate than a big company [2].

DIRECT
Question: What was the key insight Paul Graham had about making online stores look legitimate?
Correct Answer: C. Getting page layouts, fonts, and colors right
LLM Answer: B. Having high production values
Correct: False
```
