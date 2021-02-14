import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation 



def count_word_frequency(document, punctuation, stop_words): 

    word_occurrences = {}

    for word in document: 
        current = word.text.lower()
        if current not in stop_words and current not in punctuation: 
            if current not in word_occurrences.keys(): 
                word_occurrences[current] = 1
            else: 
                word_occurrences[current] += 1


    max_frequency = max(word_occurrences.values())

    # normalize frequencies 
    for word in word_occurrences.keys(): 
        word_occurrences[word] = word_occurrences[word] / max_frequency

    return word_occurrences

def compute_sentence_score(document, word_occurrences):
    sentences = [sent for sent in document.sents]

    sentence_scores = {}
    for sentence in sentences:
        for word in sentence: 
            current = word.text.lower()
            if current in word_occurrences.keys(): 
                if sentence not in sentence_scores: 
                    sentence_scores[sentence] = word_occurrences[current]
                else: 
                    sentence_scores[sentence] += word_occurrences[current]
    return sentence_scores


def summarize(sentence_scores, length):
    summary = []

    i = 0
    while i < length: 
        current_max = max(sentence_scores, key=sentence_scores.get)
        del sentence_scores[current_max]
        summary.append(current_max.text)
        i += 1

    summary = ' '.join(summary)
    return summary

if __name__ == '__main__': 

    text = """
    There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.
    An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document. Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic). This problem is called multi-document summarization. A related application is summarizing news articles. Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary.
    Image collection summarization is another application example of automatic summarization. It consists in selecting a representative set of images from a larger set of images.[3] A summary in this context is useful to show the most representative images of results in an image collection exploration system. Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions. Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured.
    """
    text2 = """Over six full decades, from his arrival on the national scene in 1945 until his death in 1991, Miles Davis made music that grew from an uncanny talent to hear the future and a headstrong desire to play it. From his beginnings in the circle of modern jazz, he came to intuit new worlds of sound and challenge. While the vast majority of musicians – jazz, rock, R&B, otherwise – find the experimental charge and imperviousness of youth eventually running down, Miles forever forged ahead, trusting and following instinct until the end.
    In doing so, Miles became the standard bearer for successive generations of musicians, shaped the course of modern improvisational music more than a half-dozen times. This biography attempts to explain those paradigm-shifts one after another, through his recordings and major life changes.
    The factors leading to that process are now the foundation of the Miles Davis legend: the dentist’s son born in 1926 to middle-class comfort in East St Louis. The fresh acolyte learning trumpet in the fertile, blues-drenched music scene of his hometown. The sensitive soul forging a seething streetwise exterior that later earned him the title, Prince Of Darkness. The determined teenager convincing his parents to send him to New York’s famed Juilliard School of Music in 1944, a ploy allowing him to locate and join the band of his idol, bebop pioneer Charlie Parker.
    It wasn’t long before the headstrong young arrival grew from sideman to leading his own projects and bands of renown, from the restrained, classical underpinning of the famous “Birth of the Cool” group (Miles’ first foray with arranger Gil Evans), to the blues-infused hardbop anthem “Walkin’”, to his first famous quintet (Coltrane, Chambers, Red Garland, Philly Joe Jones) with whom his recordings on muted trumpet helped him develop a signature sound that broke through to mainstream recognition. His subsequent jump from recording with independent labels (Prestige, Blue Note) to Columbia Records, then the Tiffany of record companies, propelled his career further from a limited jazz audience and a series of late ‘50s albums (Miles Ahead, Porgy & Bess, Miles Ahead, Kind of Blue and Sketches of Spain) secured his widespread popularity.
    Miles’ group shifted and morphed through the early ‘60s until he settled for a four-year run with his classic quintet, a lineup that is still hailed today as one of the greatest and most influential jazz groups of all time. Their albums together — from Miles Smiles, ESP and Nefertiti, to Miles In The Sky, and Filles de Kilimanjaro — traced a pattern of unparalleled growth and innovation.
    Had Miles stopped his progress at that point, he’d still be hailed as one of the greatest pioneers in jazz, but his creative momentum from the end of the ‘60s into the ‘70s would not let up. He was listening to the world around him — the amplified explosion of rock bands and the new, heavy-on-the-one funk of James Brown and Sly & The Family Stone. From the ambient hush of In A Silent Way, to the strange and unsettling – yet wildly popular Bitches Brew, he achieved another shift in musical paradigm and a personal career breakthrough.
    Bitches Brew was controversial, a best-seller and attracted another, younger generation into the Miles fold. Thousands whose musical taste respected no categorical walls flocked to hear Miles, and a slew of fusion bands were soon spawned, led by his former sidemen: Weather Report, Mahavishnu Orchestra, Return To Forever. The studio albums that defined Miles’ kaleidoscopic sound in the ‘70s included a series of (mostly) double albums, from …Brew to 1971’s Live-Evil, ‘72’s On The Corner and ‘75’s Get Up With It. The covers listed populous line-ups that reached up to 11 musicians, adding new names to an ever-widening circle of on-call talent.
    By the end of 1975, Miles was tired – and sick. A period of seclusion ensued, full years to deal with personal demons and health issues, bouncing between bouts of self-abuse and boredom. It was the longest time Miles had been off the public radar – only amplifying the appetite for his return.
    When Miles reappeared in 1981, expectation had reached fever pitch. A final series of albums for Columbia reflected his continuing fascination with funk of the day (Rose Royce, Cameo, Chaka Khan and later, Prince), and the sounds of synthesizer and drum machines (Great Miles Shift Number 8). The Man With A Horn, We Want Miles and Decoy found him still working with Teo Macero and still surrounding himself with young talent, including bassist Darryl Jones (Rolling Stones). In 1985, his album You’re Under Arrest — with unexpected covers of recent pop charters (Michael Jackson’s “Human Nature” and Cyndi Lauper’s “Time After Time”) – brought the long Davis-Columbia association to a close. He embarked on a new relationship with Warner Bros. Records and producer Tommy LiPuma, scoring successes with Tutu (written in a large part by his bassist Marcus Miller), Music from Siesta (also with Miller), Amandla (featuring a new breed of soloists, including alto saxophonist Kenny Garrett, tenor saxophonist Rick Margitza, guitarist Jean-Paul Bourelly, keyboardist Joey DeFrancesco, and others) and Doo-Bop (his collaboration with hip hop producer Easy Moe Bee.)
    Those titles proved Miles’ farewell, still pushing forward, still exploring new musical territory. Throughout his career, he had always resisted looking back, avoiding nostalgia and loathing leftovers. “It’s more like warmed-over turkey,” the eternal modernist described the music of Kind of Blue twenty-five years after recording it. Ironically, in 1991, only weeks after performing a career-overview concert in Paris that featured old friends and collaborators from as early as the ‘40s, he died from a brain aneurysm.
    Like his music, Miles always spoke with an economy of expression. And for Miles, it had to be fresh, or forget it. “I don’t want you to like me because of Kind of Blue,” he insisted. “Like me for what we’re doing now.”
    """
    length = 7

    nlp = spacy.load('en_core_web_sm')
    document = nlp(text2) # segments text into tokens (words, punctuation, new line char)

    stop_words = list(STOP_WORDS)
    punctuation = punctuation + "\n"
    word_occurences = count_word_frequency(document, punctuation, stop_words)

    sentence_scores = compute_sentence_score(document, word_occurences)
    summary = summarize(sentence_scores, length)

    print(summary + '\n')
    print('Number of characters in text:' , len(text2))
    print('Number of characters in summary:' , len(summary))
    
