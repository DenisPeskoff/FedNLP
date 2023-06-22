## processed_statement_sentences JSON (Sander)

This is a JSON file containing scores for every sentence of every statement. Note that sentences are created by splitting on ".". I put "TOO SHORT" for sentences which have less than five characters. Averages can be computed by taking the average of score arrays without the "TOO SHORT" values. You should find more accurate averages than previously, since I had counted "TOO SHORT" as 0 before.

## transcript_speakers CSV (Sander)
This contains a list of speakers, dates, and scores for every transcript. This was done by prompting GPT-4 with the last 8K tokens a speaker said in the transcript, cost ~250$.

## minutes_scores (Sander)
Contains date and score for each minutes file, processed as a whole with GPT-4-32K. Was pretty cheap and quick.