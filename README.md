# Extract sequences from fasta file by name

The script is used for extracting nucleotide or amino acid sequences, with fasta format, by sequence name. We provide two model to achieve the goal, rigorous and relaxed model.

The relaxed model means the query name maybe part of target name. For example, the query name is 'abc', while the target sequence name in fasta file is '12abcdef', the sequence named '12abcdef' also can be extracted by this model. The output would keep the unique sequences.

The rigorous model means the query name must be same with the target name. This model is default.


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

## Argument details

-f | --fasta
  
  The argument represent the file name, which keep nucleotide or amino acid sequences with fasta.

-i | --idlist

  The file include sequence name that need to extract. Save one sequence name per line. 

-o | --out

  The output file name, the default is out.fasta.

-m | --model

  The extract model, default value is rigorous. Another value is relaxed. 
