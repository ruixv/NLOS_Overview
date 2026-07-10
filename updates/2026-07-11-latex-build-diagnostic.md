# LaTeX build diagnostic (11 July 2026)

latexmk exit code: 12

```text
Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 31 Jan. 2024. Version 4.83.
No existing .aux file, so I'll make a simple one, and require run of *latex.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Category 'other':
  Rerun of 'pdflatex' forced or previously required:
    Reason or flag: 'Initial setup'

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -recorder  "bare_jrnl.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./bare_jrnl.tex
LaTeX2e <2023-11-01> patch level 1
L3 programming layer <2024-01-22>

! LaTeX Error: File `IEEEtran.cls' not found.

Type X to quit or <RETURN> to proceed,
or enter new name. (Default extension: cls)

Enter file name: 
! Emergency stop.
<read *> 
         
l.59 ^^M
        
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on bare_jrnl.log.
Latexmk: Missing input file 'IEEEtran.cls' (or dependence on it) from following:
  ! LaTeX Error: File `IEEEtran.cls' not found.
Latexmk: Sometimes, the -f option can be used to get latexmk
  to try to force complete processing.
  But normally, you will need to correct the file(s) that caused the
  error, and then rerun latexmk.
  In some cases, it is best to clean out generated files before rerunning
  latexmk after you've corrected the files.
Latexmk: Getting log file 'bare_jrnl.log'
Latexmk: Examining 'bare_jrnl.fls'
Latexmk: Examining 'bare_jrnl.log'
Latexmk: Errors, so I did not complete making targets
Collected error summary (may duplicate other messages):
  pdflatex: Command for 'pdflatex' gave return code 1
      Refer to 'bare_jrnl.log' and/or above output for details

```
