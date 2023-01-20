import arxiv, logging, os
from difflib import SequenceMatcher
print("Import success!")
logging.basicConfig(level=logging.INFO)
print("Logging reaady.")

smallClient = arxiv.Client(5, 10, 3)
print("Client built")

search = arxiv.Search(
    query = "cs.CR",
    #change this to download more/less files
    max_results = 5,
    sort_by = arxiv.SortCriterion.SubmittedDate
)

for result in search.results():
  skipnext = False
  print(result.title)
  for file in os.listdir(r"C:\Users\Haykal\Downloads\pyArxiv"):
      if SequenceMatcher(None, file, result.title).ratio() > 0.5:
        print("Already exists, skipping")
        skipnext = True
if skipnext  == False:
  print("Downloading...")
  paper = next(search.results())
  paper.download_pdf()
  print("Done, moving on...")
else:
    print("Skipped:" + result.title)
    paper = next(search.results())
print("All done, have a nice day.")