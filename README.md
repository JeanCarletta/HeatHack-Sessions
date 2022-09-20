# HeatHack-Sessions
Background reading for the sessions of HeatHack's structured programme for groups to think about what net zero means for their traditionally-built community buildings 

Written in Jupyter Book.

Intended workflow (Simplified GitFlow with developers working on one branch):

          dev         - author materials here; there isn't much chance we'll conflict but push often
           |
           |
           |
          main        -  when materials are ready to build into website, copy that part into main (see below).
           |
           |
           |
        gh-pages      - complete derivative branch produced automatically, do not edit; contains website

If we end up with conflicts (unlikely) then we can use feature branches, merging them into dev and then into main.

To copy a part into main, make sure dev on the origin is up to date.  Then switch to the main branch.

(main)$ git checkout origin/dev -- path-to-part
(main)$ git checkout origin/dev -- _toc.yml      # to get the table of contents changes

then add, commit, push as usual.  Once all parts are ready for building main will become more like a traditional main branch but until then, many commits on dev could remain unpulled.

There is a table of contents at the top level covering everything, but also individual table of contents for use during development that just build individual sections.