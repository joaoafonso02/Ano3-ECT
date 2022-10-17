## Aula1

# Encript
```bash
python3 encrypt.py senha < encrypt.py > cryptograma
```

# Decript
```bash
python3 decrypt.py senha < cryptograma > file
```

## Aula 2
```bash
dd if=criptograma bs=1 count=1663 | ./decrypt.py senha /dev/null 
```