# HASH(asss?)

```bash
python3 hash.py hash.py SHA256 # or SHA1
```


Criação de um ficheiro de 1024 bytes
```bash
dd if=/dev/urandom of=test bs=1 count=1024
```

Some cmds:
```bash
python3 hash.py test SHA256

python3 stat.py SHA1 | sed -e 's/-/,/' | gnuplot -p -e "plot '-' w l"
```