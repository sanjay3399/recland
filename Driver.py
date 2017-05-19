import glob
import ETL
import pandas as pd
import ProfileMatcher as Matcher

def Drive(filename, k):
	'''
	PARAMETERS:
		filename 		- name of the file containg (JD) Job Description
		k 				- how many top records to retrieve
	RETRUNS:
		table of top k candidates 
	'''

    # TO BE USED IN CASE OF ACTUAL DATA
    path = 'data/profiles/*.txt'
    files = glob.glob(path)
    profiles = pd.DataFrame(columns=['Name', 'Headline', 'Location', 'Summary', 'Experience', 'Skills'])
    for file in files:
        print file
        with open(file, 'r') as f:
            data = filter(None, map(str.strip, f.readlines()))
            try:
                data.remove('See more')
            except Exception as e:
                pass
            finally:
                profiles = profiles.append(ETL.extractData(data))
    profiles.to_csv("data/profiles.csv")
    # TO BE USED IN CASE OF ACTUAL DATA

    return Matcher.Match(filename, k)

if __name__ == '__main__':
    top_candidates = Drive("data/SampleJD.docx", 10)
    print top_candidates