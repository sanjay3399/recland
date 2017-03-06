# with open("listofUScities.txt", "r") as f:
#     for line in f:
#         cleanedLine = line.strip()
#         if cleanedLine: # is not empty
#             print(cleanedLine)

clean_lines = []
with open("listofUScities.txt", "r") as f:
    lines = f.readlines()
    clean_lines = [l.strip() for l in lines if l.strip()]

with open("listofUScities.txt", "w") as f:
    f.writelines('\n'.join(clean_lines))