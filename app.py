from groq import Groq
import os
import re
from fuzzywuzzy import fuzz
import json

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

retrieved_content_str = """[Document(page_content="Asterix comics begin by zooming in on a tiny corner of Roman Gaul that turns out not to be controlled by the Romans. You can do something similar on a map of New York City: if you zoom in on the Upper East Side, there's a tiny corner that's not rich, or at least wasn't in 1993. It's called Yorkville, and that was my new home. Now I was a New York artist — in the strictly technical sense of making paintings and living in New York.\n\nI was nervous about money, because I could sense that Interleaf was on the way down. Freelance Lisp hacking work was very rare, and I didn't want to have to program in another language, which in those days would have meant C++ if I was lucky. So with my unerring nose for financial opportunity, I decided to write another book on Lisp. This would be a popular book, the sort of book that could be used as a textbook. I imagined myself living frugally off the royalties and spending all my time painting. (The painting on the cover of this book, ANSI Common Lisp, is one that I painted around this time.)\n\nThe best thing about New York for me was the presence of Idelle and Julian Weber. Idelle Weber was a painter, one of the early photorealists, and I'd taken her painting class at Harvard. I've never known a teacher more beloved by her students. Large numbers of former students kept in touch with her, including me. After I moved to New York I became her de facto studio assistant.\n\nShe liked to paint on big, square canvases, 4 to 5 feet on a side. One day in late 1994 as I was stretching one of these monsters there was something on the radio about a famous fund manager. He wasn't that much older than me, and was super rich. The thought suddenly occurred to me: why don't I become rich? Then I'll be able to work on whatever I want.\n\nMeanwhile I'd been hearing more and more about this new thing called the World Wide Web. Robert Morris showed it to me when I visited him in Cambridge, where he was now in grad school at Harvard. It seemed to me that the web would be a big deal. I'd seen what graphical user interfaces had done for the popularity of microcomputers. It seemed like the web would do the same for the internet.\n\nIf I wanted to get rich, here was the next train leaving the station. I was right about that part. What I got wrong was the idea. I decided we should start a company to put art galleries online. I can't honestly say, after reading so many Y Combinator applications, that this was the worst startup idea ever, but it was up there. Art galleries didn't want to be online, and still don't, not the fancy ones. That's not how they sell. I wrote some software to generate web sites for galleries, and Robert wrote some to resize images and set up an http server to serve the pages. Then we tried to sign up galleries. To call this a difficult sale would be an understatement. It was difficult to give away. A few galleries let us make sites for them for free, but none paid us.", metadata={'source': 'data/paul_graham/paul_graham_essay.txt'}),
 Document(page_content='I had to ban myself from writing essays during most of this time, or I\'d never have finished. In late 2015 I spent 3 months writing essays, and when I went back to working on Bel I could barely understand the code. Not so much because it was badly written as because the problem is so convoluted. When you\'re working on an interpreter written in itself, it\'s hard to keep track of what\'s happening at what level, and errors can be practically encrypted by the time you get them.\n\nSo I said no more essays till Bel was done. But I told few people about Bel while I was working on it. So for years it must have seemed that I was doing nothing, when in fact I was working harder than I\'d ever worked on anything. Occasionally after wrestling for hours with some gruesome bug I\'d check Twitter or HN and see someone asking "Does Paul Graham still code?"\n\nWorking on Bel was hard but satisfying. I worked on it so intensively that at any given time I had a decent chunk of the code in my head and could write more there. I remember taking the boys to the coast on a sunny day in 2015 and figuring out how to deal with some problem involving continuations while I watched them play in the tide pools. It felt like I was doing life right. I remember that because I was slightly dismayed at how novel it felt. The good news is that I had more moments like this over the next few years.\n\nIn the summer of 2016 we moved to England. We wanted our kids to see what it was like living in another country, and since I was a British citizen by birth, that seemed the obvious choice. We only meant to stay for a year, but we liked it so much that we still live there. So most of Bel was written in England.\n\nIn the fall of 2019, Bel was finally finished. Like McCarthy\'s original Lisp, it\'s a spec rather than an implementation, although like McCarthy\'s Lisp it\'s a spec expressed as code.\n\nNow that I could write essays again, I wrote a bunch about topics I\'d had stacked up. I kept writing essays through 2020, but I also started to think about other things I could work on. How should I choose what to do? Well, how had I chosen what to work on in the past? I wrote an essay for myself to answer that question, and I was surprised how long and messy the answer turned out to be. If this surprised me, who\'d lived it, then I thought perhaps it would be interesting to other people, and encouraging to those with similarly messy lives. So I wrote a more detailed version for others to read, and this is the last sentence of it.\n\n\n\n\n\n\n\n\n\nNotes\n\n[1] My experience skipped a step in the evolution of computers: time-sharing machines with interactive OSes. I went straight from batch processing to microcomputers, which made microcomputers seem all the more exciting.', metadata={'source': 'data/paul_graham/paul_graham_essay.txt'}),
 Document(page_content='What I Worked On\n\nFebruary 2021\n\nBefore college the two main things I worked on, outside of school, were writing and programming. I didn\'t write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.\n\nThe first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district\'s 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain\'s lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.\n\nThe language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in the card reader and press a button to load the program into memory and run it. The result would ordinarily be to print something on the spectacularly loud printer.\n\nI was puzzled by the 1401. I couldn\'t figure out what to do with it. And in retrospect there\'s not much I could have done with it. The only form of input to programs was data stored on punched cards, and I didn\'t have any data stored on punched cards. The only other option was to do things that didn\'t rely on any input, like calculate approximations of pi, but I didn\'t know enough math to do anything interesting of that type. So I\'m not surprised I can\'t remember any programs I wrote, because they can\'t have done much. My clearest memory is of the moment I learned it was possible for programs not to terminate, when one of mine didn\'t. On a machine without time-sharing, this was a social as well as a technical error, as the data center manager\'s expression made clear.\n\nWith microcomputers, everything changed. Now you could have a computer sitting right in front of you, on a desk, that could respond to your keystrokes as it was running instead of just churning through a stack of punch cards and then stopping. [1]\n\nThe first of my friends to get a microcomputer built it himself. It was sold as a kit by Heathkit. I remember vividly how impressed and envious I felt watching him sitting in front of it, typing programs right into the computer.\n\nComputers were expensive in those days and it took me years of nagging before I convinced my father to buy one, a TRS-80, in about 1980. The gold standard then was the Apple II, but a TRS-80 was good enough. This was when I really started programming. I wrote simple games, a program to predict how high my model rockets would fly, and a word processor that my father used to write at least one book. There was only room in memory for about 2 pages of text, so he\'d write 2 pages at a time and then print them out, but it was a lot better than a typewriter.', metadata={'source': 'data/paul_graham/paul_graham_essay.txt'}),
 Document(page_content='At this stage I had a negative net worth, because the thousand dollars or so I had in the bank was more than counterbalanced by what I owed the government in taxes. (Had I diligently set aside the proper proportion of the money I\'d made consulting for Interleaf? No, I had not.) So although Robert had his graduate student stipend, I needed that seed funding to live on.\n\nWe originally hoped to launch in September, but we got more ambitious about the software as we worked on it. Eventually we managed to build a WYSIWYG site builder, in the sense that as you were creating pages, they looked exactly like the static ones that would be generated later, except that instead of leading to static pages, the links all referred to closures stored in a hash table on the server.\n\nIt helped to have studied art, because the main goal of an online store builder is to make users look legit, and the key to looking legit is high production values. If you get page layouts and fonts and colors right, you can make a guy running a store out of his bedroom look more legit than a big company.\n\n(If you\'re curious why my site looks so old-fashioned, it\'s because it\'s still made with this software. It may look clunky today, but in 1996 it was the last word in slick.)\n\nIn September, Robert rebelled. "We\'ve been working on this for a month," he said, "and it\'s still not done." This is funny in retrospect, because he would still be working on it almost 3 years later. But I decided it might be prudent to recruit more programmers, and I asked Robert who else in grad school with him was really good. He recommended Trevor Blackwell, which surprised me at first, because at that point I knew Trevor mainly for his plan to reduce everything in his life to a stack of notecards, which he carried around with him. But Rtm was right, as usual. Trevor turned out to be a frighteningly effective hacker.\n\nIt was a lot of fun working with Robert and Trevor. They\'re the two most independent-minded people I know, and in completely different ways. If you could see inside Rtm\'s brain it would look like a colonial New England church, and if you could see inside Trevor\'s it would look like the worst excesses of Austrian Rococo.\n\nWe opened for business, with 6 stores, in January 1996. It was just as well we waited a few months, because although we worried we were late, we were actually almost fatally early. There was a lot of talk in the press then about ecommerce, but not many people actually wanted online stores. [8]', metadata={'source': 'data/paul_graham/paul_graham_essay.txt'})]"""

example = {
    "citations": [
        {
            "number": 1,
            "quote": "In the summer of 2016 we moved to England. We wanted our kids to see what it was like living in another country, and since I was a British citizen by birth, that seemed the obvious choice."
        },
        {
            "number": 2,
            "quote": "We only meant to stay for a year, but we liked it so much that we still live there. So most of Bel was written in England."
        }
    ],
    "response": "Paul Graham and his family moved to England in the summer of 2016 [1]. While they initially planned for a one-year stay, they ended up settling there permanently [2]."
}

def normalize_text(text):
    """
    Normalizes text by converting to lowercase, removing extra whitespace,
    and removing punctuation except periods for sentence boundaries.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove punctuation except periods
    text = re.sub(r'[^\w\s.]', '', text)
    
    return text

def fuzzy_match_citation(citation, document_content, threshold=80):
    """
    Finds the location of a citation within the document content using fuzzy matching.
    Returns the similarity score and the matching text from the document.
    
    Args:
        citation (str): The quote to find
        document_content (str): The full document text to search in
        threshold (int): Minimum score (0-100) to consider a match valid
        
    Returns:
        dict: Contains match score and matched text if found
    """
    # Normalize both texts
    norm_citation = normalize_text(citation)
    norm_document = normalize_text(document_content)
    
    # Split document into chunks roughly the size of the citation
    chunk_size = len(norm_citation) * 3  # Larger window for better context
    overlap = len(norm_citation)  # Overlap by citation length to avoid splitting matches
    
    best_score = 0
    best_match = None
    
    # Slide through document with overlapping chunks
    for i in range(0, len(norm_document) - chunk_size + 1, chunk_size - overlap):
        chunk = norm_document[i:i + chunk_size]
        
        # Use token_set_ratio to handle partial matches and word reordering
        score = fuzz.token_set_ratio(norm_citation, chunk)
        
        if score > best_score:
            best_score = score
            # If we found a good match, get the original text
            if score >= threshold:
                # Find the corresponding original text
                start_idx = max(0, i - 20)  # Add some padding
                end_idx = min(len(document_content), i + chunk_size + 20)
                best_match = document_content[start_idx:end_idx]
    
    return {
        "score": best_score,
        "matched_text": best_match if best_score >= threshold else None
    }

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": f"""Using the fetched document content, provide an answer to the user's question grounded in verbatim citations. Respond with these citations first that directly answer the user's question, then produce a text response that references the citations in this format: The United States is in North America [1].

Return the response in this JSON schema:
{json.dumps(example, indent=2)}

Citations should be numbered sequentially starting from 1, be exact quotes from the source material that directly answer the question, and be referenced in the response using [n] notation."""
        },
        {
            "role": "user",
            "content": f"### Fetched document content:\n{retrieved_content_str}"
        },
        {
            "role": "user",
            "content": "### User question:\nWhen did Paul Graham start working on Bel?"
        }
    ],
    model="llama-3.1-8b-instant",
    temperature=0
)

response = chat_completion.choices[0].message.content

print(response)

parsed_response = json.loads(response)

# Extract the citations from the parsed response
citations = parsed_response.get("citations", [])

# Verify the citations in the fetched document content
for citation in citations:
    match_result = fuzzy_match_citation(citation["quote"], retrieved_content_str)
    if match_result["score"] > 0.8:
        print(f"Citation {citation['number']} verified with {match_result['score']:.2f} confidence")
    else:
        print(f"Warning: Citation {citation['number']} could not be verified in the source material")