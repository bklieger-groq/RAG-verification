from groq import Groq
import os
import re
from rapidfuzz import fuzz
import json
from tqdm import tqdm  # Add this import at the top

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

retrieved_content_str = """[Document(page_content="Asterix comics begin by zooming in on a tiny corner of Roman Gaul that turns out not to be controlled by the Romans. You can do something similar on a map of New York City: if you zoom in on the Upper East Side, there's a tiny corner that's not rich, or at least wasn't in 1993. It's called Yorkville, and that was my new home. Now I was a New York artist — in the strictly technical sense of making paintings and living in New York.\n\nI was nervous about money, because I could sense that Interleaf was on the way down. Freelance Lisp hacking work was very rare, and I didn't want to have to program in another language, which in those days would have meant C++ if I was lucky. So with my unerring nose for financial opportunity, I decided to write another book on Lisp. This would be a popular book, the sort of book that could be used as a textbook. I imagined myself living frugally off the royalties and spending all my time painting. (The painting on the cover of this book, ANSI Common Lisp, is one that I painted around this time.)\n\nThe best thing about New York for me was the presence of Idelle and Julian Weber. Idelle Weber was a painter, one of the early photorealists, and I'd taken her painting class at Harvard. I've never known a teacher more beloved by her students. Large numbers of former students kept in touch with her, including me. After I moved to New York I became her de facto studio assistant.\n\nShe liked to paint on big, square canvases, 4 to 5 feet on a side. One day in late 1994 as I was stretching one of these monsters there was something on the radio about a famous fund manager. He wasn't that much older than me, and was super rich. The thought suddenly occurred to me: why don't I become rich? Then I'll be able to work on whatever I want.\n\nMeanwhile I'd been hearing more and more about this new thing called the World Wide Web. Robert Morris showed it to me when I visited him in Cambridge, where he was now in grad school at Harvard. It seemed to me that the web would be a big deal. I'd seen what graphical user interfaces had done for the popularity of microcomputers. It seemed like the web would do the same for the internet.\n\nIf I wanted to get rich, here was the next train leaving the station. I was right about that part. What I got wrong was the idea. I decided we should start a company to put art galleries online. I can't honestly say, after reading so many Y Combinator applications, that this was the worst startup idea ever, but it was up there. Art galleries didn't want to be online, and still don't, not the fancy ones. That's not how they sell. I wrote some software to generate web sites for galleries, and Robert wrote some to resize images and set up an http server to serve the pages. Then we tried to sign up galleries. To call this a difficult sale would be an understatement. It was difficult to give away. A few galleries let us make sites for them for free, but none paid us.", metadata={'source': 'data/paul_graham/paul_graham_essay.txt'}),
 Document(page_content='I had to ban myself from writing essays during most of this time, or I\'d never have finished. In late 2015 I spent 3 months writing essays, and when I went back to working on Bel I could barely understand the code. Not so much because it was badly written as because the problem is so convoluted. When you\'re working on an interpreter written in itself, it\'s hard to keep track of what\'s happening at what level, and errors can be practically encrypted by the time you get them.\n\nSo I said no more essays till Bel was done. But I told few people about Bel while I was working on it. So for years it must have seemed that I was doing nothing, when in fact I was working harder than I\'d ever worked on anything. Occasionally after wrestling for hours with some gruesome bug I\'d check Twitter or HN and see someone asking "Does Paul Graham still code?"\n\nWorking on Bel was hard but satisfying. I worked on it so intensively that at any given time I had a decent chunk of the code in my head and could write more there. I remember taking the boys to the coast on a sunny day in 2015 and figuring out how to deal with some problem involving continuations while I watched them play in the tide pools. It felt like I was doing life right. I remember that because I was slightly dismayed at how novel it felt. The good news is that I had more moments like this over the next few years.\n\nIn the summer of 2016 we moved to England. We wanted our kids to see what it was like living in another country, and since I was a British citizen by birth, that seemed the obvious choice. We only meant to stay for a year, but we liked it so much that we still live there. So most of Bel was written in England.\n\nIn the fall of 2019, Bel was finally finished. Like McCarthy\'s original Lisp, it\'s a spec rather than an implementation, although like McCarthy\'s Lisp it\'s a spec expressed as code.\n\nNow that I could write essays again, I wrote a bunch about topics I\'d had stacked up. I kept writing essays through 2020, but I also started to think about other things I could work on. How should I choose what to do? Well, how had I chosen what to work on in the past? I wrote an essay for myself to answer that question, and I was surprised how long and messy the answer turned out to be. If this surprised me, who\'d lived it, then I thought perhaps it would be interesting to other people, and encouraging to those with similarly messy lives. So I wrote a more detailed version for others to read, and this is the last sentence of it.\n\n\n\n\n\n\n\n\n\nNotes\n\n[1] My experience skipped a step in the evolution of computers: time-sharing machines with interactive OSes. I went straight from batch processing to microcomputers, which made microcomputers seem all the more exciting.', metadata={'source': 'data/paul_graham/paul_graham_essay.txt'}),
 Document(page_content='What I Worked On\n\nFebruary 2021\n\nBefore college the two main things I worked on, outside of school, were writing and programming. I didn\'t write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.\n\nThe first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district\'s 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain\'s lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.\n\nThe language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in the card reader and press a button to load the program into memory and run it. The result would ordinarily be to print something on the spectacularly loud printer.\n\nI was puzzled by the 1401. I couldn\'t figure out what to do with it. And in retrospect there\'s not much I could have done with it. The only form of input to programs was data stored on punched cards, and I didn\'t have any data stored on punched cards. The only other option was to do things that didn\'t rely on any input, like calculate approximations of pi, but I didn\'t know enough math to do anything interesting of that type. So I\'m not surprised I can\'t remember any programs I wrote, because they can\'t have done much. My clearest memory is of the moment I learned it was possible for programs not to terminate, when one of mine didn\'t. On a machine without time-sharing, this was a social as well as a technical error, as the data center manager\'s expression made clear.\n\nWith microcomputers, everything changed. Now you could have a computer sitting right in front of you, on a desk, that could respond to your keystrokes as it was running instead of just churning through a stack of punch cards and then stopping. [1]\n\nThe first of my friends to get a microcomputer built it himself. It was sold as a kit by Heathkit. I remember vividly how impressed and envious I felt watching him sitting in front of it, typing programs right into the computer.\n\nComputers were expensive in those days and it took me years of nagging before I convinced my father to buy one, a TRS-80, in about 1980. The gold standard then was the Apple II, but a TRS-80 was good enough. This was when I really started programming. I wrote simple games, a program to predict how high my model rockets would fly, and a word processor that my father used to write at least one book. There was only room in memory for about 2 pages of text, so he\'d write 2 pages at a time and then print them out, but it was a lot better than a typewriter.', metadata={'source': 'data/paul_graham/paul_graham_essay.txt'}),
 Document(page_content='At this stage I had a negative net worth, because the thousand dollars or so I had in the bank was more than counterbalanced by what I owed the government in taxes. (Had I diligently set aside the proper proportion of the money I\'d made consulting for Interleaf? No, I had not.) So although Robert had his graduate student stipend, I needed that seed funding to live on.\n\nWe originally hoped to launch in September, but we got more ambitious about the software as we worked on it. Eventually we managed to build a WYSIWYG site builder, in the sense that as you were creating pages, they looked exactly like the static ones that would be generated later, except that instead of leading to static pages, the links all referred to closures stored in a hash table on the server.\n\nIt helped to have studied art, because the main goal of an online store builder is to make users look legit, and the key to looking legit is high production values. If you get page layouts and fonts and colors right, you can make a guy running a store out of his bedroom look more legit than a big company.\n\n(If you\'re curious why my site looks so old-fashioned, it\'s because it\'s still made with this software. It may look clunky today, but in 1996 it was the last word in slick.)\n\nIn September, Robert rebelled. "We\'ve been working on this for a month," he said, "and it\'s still not done." This is funny in retrospect, because he would still be working on it almost 3 years later. But I decided it might be prudent to recruit more programmers, and I asked Robert who else in grad school with him was really good. He recommended Trevor Blackwell, which surprised me at first, because at that point I knew Trevor mainly for his plan to reduce everything in his life to a stack of notecards, which he carried around with him. But Rtm was right, as usual. Trevor turned out to be a frighteningly effective hacker.\n\nIt was a lot of fun working with Robert and Trevor. They\'re the two most independent-minded people I know, and in completely different ways. If you could see inside Rtm\'s brain it would look like a colonial New England church, and if you could see inside Trevor\'s it would look like the worst excesses of Austrian Rococo.\n\nWe opened for business, with 6 stores, in January 1996. It was just as well we waited a few months, because although we worried we were late, we were actually almost fatally early. There was a lot of talk in the press then about ecommerce, but not many people actually wanted online stores. [8]', metadata={'source': 'data/paul_graham/paul_graham_essay.txt'})]"""

def get_long_gatsby_paragraphs():
    """Extract paragraphs longer than 100 chars from gatsby.txt"""
    with open('gatsby.txt', 'r') as f:
        text = f.read()
    paragraphs = text.split('\n\n')
    return [p for p in paragraphs if len(p.strip()) > 100]

def intersperse_gatsby(text):
    """Insert random Gatsby paragraphs between double newlines"""
    gatsby_paragraphs = get_long_gatsby_paragraphs()
    if not gatsby_paragraphs:
        return text
        
    parts = text.split('\n\n')
    result = []
    
    for i, part in enumerate(parts):
        result.append(part)
        if i < len(parts) - 1:  # Don't add after last part
            gatsby_p = gatsby_paragraphs[i % len(gatsby_paragraphs)]
            result.append(gatsby_p)
            
    return '\n\n'.join(result)

# Intersperse Gatsby paragraphs into retrieved content
retrieved_content_str = intersperse_gatsby(retrieved_content_str)

eval_questions = [
    {
        "question": "Where did Paul Graham move to in 2016?",
        "choices": ["France", "England", "Cambridge", "New York"],
        "correct_answer": "England"
    },
    {
        "question": "What programming language did Paul Graham first learn to program in?",
        "choices": ["BASIC", "Fortran", "Lisp", "C++"],
        "correct_answer": "Fortran"
    },
    {
        "question": "Which computer model did Paul Graham's father buy him?",
        "choices": ["Apple II", "Heathkit", "TRS-80", "IBM 1401"],
        "correct_answer": "TRS-80"
    },
    {
        "question": "In what neighborhood of New York did Paul Graham live in 1993?",
        "choices": ["Upper East Side", "Yorkville", "Manhattan", "Cambridge"],
        "correct_answer": "Yorkville"
    },
    {
        "question": "Who was Paul Graham's painting teacher at Harvard?",
        "choices": ["Julian Weber", "Idelle Weber", "Robert Morris", "Rich Draves"],
        "correct_answer": "Idelle Weber"
    },
    {
        "question": "What was Paul Graham's first business idea related to the web?",
        "choices": ["Online store builder", "Art galleries online", "WYSIWYG site builder", "Web hosting"],
        "correct_answer": "Art galleries online"
    },
    {
        "question": "Who did Robert Morris recommend as a programmer?",
        "choices": ["Julian Weber", "Rich Draves", "Trevor Blackwell", "Robert Morris"],
        "correct_answer": "Trevor Blackwell"
    },
    {
        "question": "How many stores did Paul Graham's business open with in January 1996?",
        "choices": ["4", "5", "6", "3"],
        "correct_answer": "6"
    },
    {
        "question": "What was the limitation of Paul Graham's word processor on the TRS-80?",
        "choices": ["Only 2 pages of text in memory", "Could only handle punch cards", "Limited to static pages", "Memory overflow"],
        "correct_answer": "Only 2 pages of text in memory"
    },
    {
        "question": "Where was the IBM 1401 computer located in Paul Graham's school?",
        "choices": ["Data processing center", "Basement", "Junior high school", "Computer lab"],
        "correct_answer": "Basement"
    },
    {
        "question": "What was the specific limitation that made programming on the IBM 1401 difficult for Paul Graham?",
        "choices": ["No display screen", "Limited memory", "Programs could only use punched card input", "No interactive OS"],
        "correct_answer": "Programs could only use punched card input"
    },
    {
        "question": "How did Paul Graham's WYSIWYG site builder handle links differently from static pages?",
        "choices": [
            "They used hash tables for storage", 
            "They referred to closures stored in a hash table on the server",
            "They generated static pages later"
        ],
        "correct_answer": "They referred to closures stored in a hash table on the server"
    },
    {
        "question": "According to the text, how did Robert Morris and Trevor Blackwell's minds differ?",
        "choices": [
            "Like independent vs dependent thinking",
            "Like grad student vs programmer",
            "Like a colonial New England church vs Austrian Rococo",
            "Like notecards vs software"
        ],
        "correct_answer": "Like a colonial New England church vs Austrian Rococo"
    },
    {
        "question": "What specific technical issue did Paul Graham first encounter with programming on the IBM 1401?",
        "choices": [
            "Data processing errors",
            "Punch card failures",
            "Program non-termination",
            "Printer malfunctions"
        ],
        "correct_answer": "Program non-termination"
    },
    {
        "question": "What was Trevor Blackwell known for before demonstrating his programming abilities?",
        "choices": [
            "His graduate studies at Harvard",
            "His plan to reduce everything to a stack of notecards",
            "His work with Robert Morris",
            "His independent-minded nature"
        ],
        "correct_answer": "His plan to reduce everything to a stack of notecards"
    },
    {
        "question": "What was the key insight Paul Graham had about making online stores look legitimate?",
        "choices": [
            "Using WYSIWYG editors",
            "Having high production values",
            "Getting page layouts, fonts, and colors right",
            "Making static pages"
        ],
        "correct_answer": "Getting page layouts, fonts, and colors right"
    },
    {
        "question": "What specific financial situation did Paul Graham face when he moved to Yorkville?",
        "choices": [
            "He had consulting income from Interleaf",
            "He had a negative net worth due to unpaid taxes",
            "He was living frugally off book royalties",
            "He was making money from freelance Lisp work"
        ],
        "correct_answer": "He had a negative net worth due to unpaid taxes"
    },
    {
        "question": "What was Paul Graham's specific motivation for writing another Lisp book?",
        "choices": [
            "To make money from freelance work",
            "To avoid programming in C++",
            "To live frugally off royalties while painting",
        ],
        "correct_answer": "To live frugally off royalties while painting"
    },
    {
        "question": "What specific event triggered Paul Graham's thought about becoming rich?",
        "choices": [
            "Hearing about a famous fund manager on radio while stretching canvas",
            "Working as Idelle Weber's studio assistant",
            "Seeing the World Wide Web with Robert Morris",
            "Stretching large canvases in the studio"
        ],
        "correct_answer": "Hearing about a famous fund manager on radio while stretching canvas"
    }
]

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

def evaluate_multiple_choice_accuracy(eval_questions, retrieved_content_str):
    """
    Evaluates multiple choice answer accuracy using the LLM.
    Returns accuracy metrics and individual question results.
    """
    correct_count = 0
    results = []
    
    # Add progress bar
    progress_bar = tqdm(eval_questions, desc="Direct evaluation")
    
    for question in progress_bar:
        # Create letter-mapped choices (A, B, C, D, etc.)
        letter_choices = {
            chr(65 + i): choice 
            for i, choice in enumerate(question["choices"])
        }
        
        # Format choices with letters
        choices_text = "\n".join([
            f"{letter}. {choice}" 
            for letter, choice in letter_choices.items()
        ])
        
        # Get correct answer letter
        correct_letter = [
            letter for letter, choice in letter_choices.items()
            if choice == question["correct_answer"]
        ][0]
        
        prompt = f"""Based on the provided text, answer this multiple choice question:

Question: {question["question"]}

{choices_text}

Return your answer in this JSON format:
{{
    "selected_letter": "single letter of your chosen answer (A, B, C, etc.)",
}}"""

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system", 
                    "content": "Only answer based on the provided text. Always respond with a single letter (A, B, C, etc.) as your selected_letter."
                },
                {
                    "role": "user",
                    "content": f"### Reference text:\n{retrieved_content_str}"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.1-8b-instant",
            temperature=0
        )

        try:
            llm_response = json.loads(chat_completion.choices[0].message.content)
            selected_letter = llm_response["selected_letter"].upper()
            selected_answer = letter_choices.get(selected_letter)
            is_correct = selected_letter == correct_letter
            
            if is_correct:
                correct_count += 1
                
            results.append({
                "question": question["question"],
                "correct_answer": question["correct_answer"],
                "correct_letter": correct_letter,
                "llm_letter": selected_letter,
                "llm_answer": selected_answer,
                "is_correct": is_correct,
                "explanation": "",
                "citations": [],  # Added for consistency
                "attempts": 1     # Added for consistency
            })
            
        except (json.JSONDecodeError, KeyError) as e:
            results.append({
                "question": question["question"],
                "error": f"Failed to process LLM response: {str(e)}",
                "attempts": 1
            })

    return {
        "method": "direct",  # Add this directly here
        "accuracy": correct_count / len(eval_questions),
        "correct_count": correct_count,
        "total_questions": len(eval_questions),
        "detailed_results": results
    }

def evaluate_with_citations(eval_questions, retrieved_content_str, max_retries=2):
    """
    Evaluates multiple choice questions by requiring direct citations from the text.
    Uses fuzzy matching to verify citations before accepting an answer.
    """
    results = []
    correct_count = 0
    
    # Add progress bar
    progress_bar = tqdm(eval_questions, desc="Citation-based evaluation")
    
    citation_example = {
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
        "explanation": "Based on the citations, the answer is clearly England. The text explicitly states they moved there in 2016 [1] and ended up staying permanently [2].",
        "selected_letter": "B"
    }
    
    for question in progress_bar:
        # Create letter-mapped choices
        letter_choices = {
            chr(65 + i): choice 
            for i, choice in enumerate(question["choices"])
        }
        
        choices_text = "\n".join([
            f"{letter}. {choice}" 
            for letter, choice in letter_choices.items()
        ])
        
        correct_letter = [
            letter for letter, choice in letter_choices.items()
            if choice == question["correct_answer"]
        ][0]
        
        # Try up to max_retries + 1 times
        for attempt in range(max_retries + 1):
            system_prompt = f"""Using the fetched document content, answer this multiple choice question with verbatim citations that support your answer.

Return your answer in this JSON schema:
{json.dumps(citation_example, indent=2)}

Citations should be:
1. Numbered sequentially starting from 1
2. Exact quotes from the source material that directly support your answer
3. Referenced in your explanation using [n] notation: The United States is in North America [1]"""

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": f"### Fetched document content:\n{retrieved_content_str}"
                    },
                    {
                        "role": "user",
                        "content": f"""Question: {question["question"]}

Choices:
{choices_text}"""
                    }
                ],
                model="llama-3.1-8b-instant",
                temperature=0
            )

            try:
                llm_response = json.loads(chat_completion.choices[0].message.content)
                citations_valid = True
                
                # Verify all citations
                for citation in llm_response["citations"]:
                    match_result = fuzzy_match_citation(citation["quote"], retrieved_content_str)
                    if match_result["score"] <= 80:
                        citations_valid = False
                        break
                
                if citations_valid:
                    selected_letter = llm_response["selected_letter"].upper()
                    selected_answer = letter_choices.get(selected_letter)
                    is_correct = selected_letter == correct_letter
                    
                    if is_correct:
                        correct_count += 1
                        
                    results.append({
                        "question": question["question"],
                        "correct_answer": question["correct_answer"],
                        "correct_letter": correct_letter,
                        "llm_letter": selected_letter,
                        "llm_answer": selected_answer,
                        "is_correct": is_correct,
                        "citations": llm_response["citations"],
                        "explanation": llm_response["explanation"],
                        "attempts": attempt + 1,
                    })
                    break
                    
                elif attempt == max_retries:
                    results.append({
                        "question": question["question"],
                        "error": "Failed to verify citations after maximum retries",
                        "attempts": attempt + 1
                    })
                    
            except (json.JSONDecodeError, KeyError) as e:
                if attempt == max_retries:
                    results.append({
                        "question": question["question"],
                        "error": f"Failed to process LLM response: {str(e)}",
                        "attempts": attempt + 1
                    })

    return {
        "method": "citation_based",
        "accuracy": correct_count / len(eval_questions),
        "correct_count": correct_count,
        "total_questions": len(eval_questions),
        "detailed_results": results
    }

def compare_evaluation_methods(eval_questions, retrieved_content_str):
    """
    Runs both evaluation methods and compares their results.
    """
    print("Starting evaluations...")
    citation_results = evaluate_with_citations(eval_questions, retrieved_content_str)
    print("\n") # Add newline for better spacing between progress bars
    direct_results = evaluate_multiple_choice_accuracy(eval_questions, retrieved_content_str)
    
    print("\nResults Comparison:")
    print(f"Citation-based accuracy: {citation_results['accuracy']:.2%}")
    print(f"Direct answer accuracy: {direct_results['accuracy']:.2%}")
    
    return {
        "citation_based": citation_results,
        "direct": direct_results
    }

# Run the comparison
comparison_results = compare_evaluation_methods(eval_questions, retrieved_content_str)

# Detailed printing of results
print_detailed_results = True

for method, results in comparison_results.items():
    print(f"\n{method.replace('_', ' ').title()} Results:")
    print(f"Accuracy: {results['accuracy']:.2%}")
    print(f"Correct: {results['correct_count']}/{results['total_questions']}")
    print("\nDetailed Results:")
    if print_detailed_results:
        for result in results['detailed_results']:
            if "error" in result:
                print(f"\nQuestion: {result['question']}")
                print(f"Error: {result['error']}")
                if "attempts" in result:
                    print(f"Attempts: {result['attempts']}")
            else:
                print(f"\nQuestion: {result['question']}")
                print(f"Correct Answer: {result['correct_letter']}. {result['correct_answer']}")
                print(f"LLM Answer: {result['llm_letter']}. {result['llm_answer']}")
                print(f"Correct: {result['is_correct']}")
                if "citations" in result:
                    print("\nCitations:")
                    for citation in result["citations"]:
                        print(f"  {citation['number']}: {citation['quote']}")
                print(f"Explanation: {result['explanation']}")