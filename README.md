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
Question: When did Paul Graham start working on Bel?

Response:
{
  "citations": [
    {
      "number": 1,
      "quote": "In late 2015 I spent 3 months writing essays, and when I went back to working on Bel I could barely understand the code."
    }
  ],
  "response": "Paul Graham started working on Bel in late 2015 [1]."
}

Verification:
Citation 1 verified with 100.00 confidence

```

The evaluation shows citation helps in certain cases!

```
Results Comparison:
Citation-based accuracy: 100.00%
Direct answer accuracy: 94.74%

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

### Credits

Groq implementation developed by Benjamin Klieger and Rick Lamers with inspiration from Trelis Research [(Original Video)](https://www.youtube.com/watch?v=-wGzSnhQKPM).
