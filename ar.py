import arxiv, logging, os
from difflib import SequenceMatcher
print("Import success!")
"""
to use later
class CleanExit(object):
  def __enter__(self):
    return self
  def __exit__(self, exc_type, exc_value, exc_tb):
    if exc_type is KeyboardInterrupt:
      return True
    return exc_type is None
with CleanExit():
"""
while True:
  choice = input("Enable info level logging? [y/n]\n")
  if choice == "y":
    logging.basicConfig(level=logging.INFO)
    print("Logging is now active.")
    break
  elif choice == "n":
    print("Logging disabled.")
    break
  else:
    print("Unrecognized input.\n")
  

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
    print("Next paper should be: ")
print("All done, have a nice day.")