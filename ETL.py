import glob
import pandas as pd

def extractData(content):
    profile = {}
    for c in content:
        line = c.split(':')
        profile[line[0]] = line[1]
    year, month = 0, 0
    try:
        exp_list = profile.get("Experience").split(',')[:-1]
        for exp_item in exp_list:
            exp_item = exp_item.split(' ')
            for exp, exp_type in zip(exp_item[::2], exp_item[1::2]):
                try:
                    if exp_type == 'mos':
                        month += int(exp)
                    else:
                        year += int(exp)
                except Exception as e:
                    continue
        year += month/12
        month = int((month/12.0 - int(month/12)) * 12)
        profile["Experience"] = str(year) + ' years, ' + str(month) + ' months'
        return pd.DataFrame([profile], columns=['Name', 'Headline', 'Location', 'Summary', 'Experience', 'Skills'])
    except Exception as e:
        return None

if __name__ == '__main__':
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
                profiles = profiles.append(extractData(data))
    profiles.to_csv("data/profiles.csv")