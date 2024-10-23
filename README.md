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