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

```16 bytes sao de IV```

```bash
./encrypt_ofb.py senha < encrypt.py> | dd bs=1 count=32 | encrypt_ofb.py senha | less  # se perder o fim, OFB u CFB é igual 

```bash
./encrypt_ofb.py senha < encrypt.py> | dd bs=1 skip=1 | encrypt_ofb.py senha | less
```

Se se perder o inicio, irá se perder o IV, o CFB dá lixo, CFB permite o autosincronismo, permite recuperar perdas da unidade de feedback

