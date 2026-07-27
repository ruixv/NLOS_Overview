# RIS-assisted NLOS source-integration failure

```text
Traceback (most recent call last):
  File "/home/runner/work/NLOS_Overview/NLOS_Overview/scripts/run_ris_nlos_doa.py", line 5, in <module>
    main()
  File "/home/runner/work/NLOS_Overview/NLOS_Overview/scripts/integrate_ris_nlos_doa.py", line 226, in main
    patch_readme()
  File "/home/runner/work/NLOS_Overview/NLOS_Overview/scripts/integrate_ris_nlos_doa.py", line 67, in patch_readme
    text = replace_once(text, category_anchor, category_rows + category_anchor, "README RF/RIS category")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/NLOS_Overview/NLOS_Overview/scripts/integrate_ris_nlos_doa.py", line 27, in replace_once
    die(f"{label}: expected one anchor, found {count}")
  File "/home/runner/work/NLOS_Overview/NLOS_Overview/scripts/integrate_ris_nlos_doa.py", line 21, in die
    raise RuntimeError(message)
RuntimeError: README RF/RIS category: expected one anchor, found 0
```
