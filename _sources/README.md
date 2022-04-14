# HeatHack-Sessions
Materials for running the group sessions of HeatHack's structured programme for groups to think about what net zero means for their traditionally-built community buildings 

Written in Jupyter Book.

Intended workflow (Simplified GitFlow with developers working on one branch):

          dev         - author materials here; there isn't much chance we'll conflict but push often
           |
           |
           |
          main        -  when materials are ready to build into website, merge into main
           |
           |
           |
        gh-pages      - complete derivative branch produced automatically, do not edit; contains website

If we end up with conflicts (unlikely) then we can use feature branches, merging them into dev and then into main.
