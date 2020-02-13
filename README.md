# extract-sequences-from-fasta

The script is used for extracting nucleotide or amino acid sequences, with fasta format, by sequence name.

View the help.

```bash
python -h
``` 

Extract sequence with relaxed model.

```bash
python3 extract_fasta_by_ID.py -f sequences.fasta -i idlist.txt -out output.fasta -m relaxed
```    

Extract sequence with rigorous model.

```bash
python3 extract_fasta_by_ID.py -f sequences.fasta -i idlist.txt -out output.fasta -m rigorous
```

