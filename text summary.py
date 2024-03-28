!pip install transformers
!pip install bert-extractive-summarizer
!pip install nltk

from transformers import pipeline
from nltk.translate.bleu_score import sentence_bleu
import nltk
nltk.download('punkt')

# Initialize summarization pipeline
summarizer = pipeline("summarization")

# Input text
body = '''
Cricket is a game played by two teams of eleven players each on a pitch with two sets of three stumps, which are called wickets. The bowler bowls the ball down the pitch to the batsman of the opposing team, who must defend the wickets in front of which he stands. The target of the game is to score as many runs as possible.

Runs are scored by individual players by running on the playing strip (called pitch) between the wickets, or by hitting a ball that flies outside the boundary of the playground or which falls inside the boundary but bounces or rolls outside. When the balls go directly outside the boundary, the batsman scores six runs, and when the ball falls within the boundary but rolls outside then the batsman scores four runs. The opponent team will bowl and field and their objective is to take the wickets for each of the batsmen playing on the pitch.

A batsman can be dismissed in one of several ways: by the bowler hitting the wicket with the ball, which is called, bowled; by a fielder catching the ball hit by the batsman before it touches the ground and it is called caught; by the wicket-keeper or another fielder breaking the stumps while the batsman attempts a run and is therefore out of his ground. This is called stumped or run out. A batsman can also be dismissed if the batsman breaks the wicket with his own bat or body and this is called a hit wicket; by a part of the batsman’s body being hit by a ball that would otherwise have hit the wicket is called leg before the wicket or “lbw”.

A match consists of one or two innings, and each inning ends when the tenth batsman of the batting team is out, when a certain number of overs (an over: a series of six balls bowled) have been played or when the captain of the batting team declares ending the innings voluntarily.
'''

# Generate the summary
summary = summarizer(body, max_length=100, min_length=30, do_sample=False)[0]['summary_text'].strip()

# Print the summary
print("#########################")
print(summary)

# Tokenize reference and candidate summaries
reference_sentences = nltk.sent_tokenize(body)
candidate_sentences = nltk.sent_tokenize(summary)

# Compute BLEU score for each sentence and average them
bleu_scores = [sentence_bleu([nltk.word_tokenize(ref)], nltk.word_tokenize(cand)) for ref, cand in zip(reference_sentences, candidate_sentences)]
avg_bleu_score = sum(bleu_scores) / len(bleu_scores)

print('Average BLEU score -> {}'.format(avg_bleu_score))
