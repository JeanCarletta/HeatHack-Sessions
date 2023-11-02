import pandas as pd
from string import Template
import os

# BUG - we get Nans for fields that require XLOOKUP unless I save
# a version of the spreadsheet with values only.

# We have a spreadsheet that defines the cards in the card game and is used to generate the physical cards.
# Need to generate the md pages for much of our book from a spreadsheet and copy them into location - but there is handwritten content that isn't part of the spreadsheet.
# Some of this is preliminary pages and these are as in the table of contents.
# Some is extra explanation for each card.   of the
# other spreadsheet columns first before the extra content.  The extra content must contain a header for the book to use in the table of contents.

# want to write a structure that is the_steps with an overview followed by a section for each step 
# with the cards

temp_dir = "output"
cards_dir = "_cards"
steps_dir = "_steps"
card_explanation_dir = "../card-explanations/" # hand written, 1.md is for card with number 1 etc
master_datafile = "master-spreadsheet.xlsx"
#tocfilename = "%s/_toc_cards.yml" %(temp_dir)
steps_template = "steps-template.txt"
cards_template = "cards-template.txt"


# park everything in a subdirectory so it's easy to delete/shift
## should probably just delete any existing output

try:
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    if not os.path.exists("%s/%s" % (temp_dir, cards_dir)):
        os.makedirs("%s/%s" % (temp_dir, cards_dir))
    if not os.path.exists("%s/%s" % (temp_dir, steps_dir)):
        os.makedirs("%s/%s" % (temp_dir, steps_dir))
except:
    print("Can't make output directory or required subdirectories!")

# generate the cards from the spreadsheet, template, and hand-written explanation, and shove in cards_dir

# read the spreadsheet
cards_df = pd.read_excel(master_datafile, sheet_name="cards",dtype=str)
cards_df = cards_df.fillna('') 


# read the template
try:
    with open(cards_template, 'r') as f:
        cards_src = Template(f.read())
except:
    print("Can't read cards template!")

# iterate the cards writing files for them.  The number field is the id number.

for i in range(0,len(cards_df)):
    result = cards_src.substitute(cards_df.iloc[i])
    try:
        outfilename = "%s/%s/%s.md" % (temp_dir, cards_dir, cards_df.iloc[i]['number'])
        f = open(outfilename, "w")
        f.write(result)
    except:
        print("Can't write card file: %s" % outfilename)
    try:
        hand_written_explanation="%s%s%s" % (card_explanation_dir,cards_df.iloc[i]['number'],".md")
        inf = open(hand_written_explanation,"r")
        inf_content = inf.read()
        f.write(inf_content)
        f.close()
    except:
        print("No card explanation for this file: %s" % outfilename)

# iterate the steps writing files for them. The number field is the id number.

## read the spreadsheet
steps_df = pd.read_excel(master_datafile, sheet_name="steps",dtype=str)
steps_df = steps_df.fillna('') 

## read the template
try:
    with open(steps_template, 'r') as f:
        steps_src = Template(f.read())
except:
    print("Can't read steps template!")


## write out step files
### ideally template would include little representations of each card in the step?

for i in range(0,len(steps_df)):
    result = steps_src.substitute(steps_df.iloc[i])
    try:
        outfilename = "%s/%s/%s.md" % (temp_dir, steps_dir, steps_df.iloc[i]['number'])
        f = open(outfilename, "w")
        f.write(result)
    except:
        print("Can't write steps file: %s" % outfilename)
   

# write the table of contents - this is no longer correct, ignore it.
# try:
#     f = open(tocfilename, "w")
#     f.write("- file: card-game/pages/intro\n  sections:\n    - file: card-game/pages/reading-a-card\n    - file: card-game/pages/how-to-play\n")
#     for i in range(0,len(steps_df)):
#         f.write("%s%s%s%s%s" % ("    - file: card-game/",steps_dir, "/", steps_df.iloc[i]['number'],"\n      sections:\n"))
#         for j in range(0,len(cards_df)):
#             if cards_df.iloc[j]['step_number'] == steps_df.iloc[i]['number']:
#                 f.write("%s%s%s%s%s" % ("        - file: card-game/", cards_dir, "/", cards_df.iloc[j]['number'],"\n"))
#     f.write("    - file: card-game/pages/wildcard\n    - file: card-game/pages/actions-weve-excluded\n      sections:\n")
#     f.write("        - file: card-game/pages/actions-weve-excluded/hydrogen-ready-boiler\n")
#     f.write("        - file: card-game/pages/actions-weve-excluded/micro-chp\n")
#     f.write("        - file: card-game/pages/actions-weve-excluded/solar-panels-for-hot-water\n")
#     f.write("        - file: card-game/pages/actions-weve-excluded/turn-electrics-off-at-plug\n")
#     f.write("        - file: card-game/pages/actions-weve-excluded/install-air-curtains\n")
#     f.write("        - file: card-game/pages/actions-weve-excluded/destratification-fans\n")
#     f.write("        - file: card-game/pages/actions-weve-excluded/biomass\n")
#     f.write("        - file: card-game/pages/actions-weve-excluded/efficient-appliances\n")
#     f.close()
# except:
#     print("Can't write to toc file: %s" % tocfilename)

   
    
    

   



