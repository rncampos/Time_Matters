import click
from time_matters import timeMatters, timeMattersPerSentence
@click.command()
@click.option("-t", '--text', help='insert text', required=False)
@click.option("-l", '--language', help='insert language', required=True)
@click.option("-dps", '--date_per_sentence', help='select if want to analyze per sentence',default=False ,required=False)
@click.option("-cwd", '--context_window_distance', help='max distance between words',default=10, required=False)
@click.option("-th", '--threshold', help='minimum DICE threshold similarity values',default=0.05, required=False)
@click.option("-n", '--max_array_len', help='size of the context vector',default=0 ,required=False)
@click.option("-ky", '--max_keywords', help='max keywords',default=10 ,required=False)
@click.option("-icwd", '--ignore_contextual_window_distance', help='ignore contextual window distance',default=False ,required=False)
@click.option("-aps", '--analysis_sentence', help='DICE Calculation per sentence',default=True ,required=False)
@click.option("-td", '--heideltime_document_type', help='Type of the document specified by <file> (options: News, Narrative, Colloquial, Scientific).', default='News', required=False)
@click.option("-dct", '--heideltime_document_creation_time', help='Creation date of document only valid format (YYYY-MM-DD).only will be considered if document type are News or colloquial.', default="", required=False)
@click.option("-i", '--input_file', help='input text file', required=False)
def Dates(text, language, date_per_sentence, context_window_distance, threshold, max_array_len, max_keywords, ignore_contextual_window_distance, analysis_sentence, input_file, heideltime_document_type, heideltime_document_creation_time):
    def run_time_matters(text_content):
        if date_per_sentence:
            output = timeMattersPerSentence(text_content, language, context_window_distance, threshold, max_array_len, max_keywords, ignore_contextual_window_distance, heideltime_document_type, heideltime_document_creation_time)
            print(output)
        else:
            output = timeMatters(text_content, language, context_window_distance, threshold, max_array_len, max_keywords, analysis_sentence, ignore_contextual_window_distance, heideltime_document_type, heideltime_document_creation_time)
            print(output)
    if text and input_file:
        print('Select only text or file to be analysed')
        exit(1)
    elif not text and not input_file:
        print('you must insert text or select file with text')
        exit(1)
    else:
        if text:
            run_time_matters(text)
        else:
            with open(input_file) as file:
                text_content = file.read()
                run_time_matters(text_content)


if __name__ == "__main__":
    Dates()
