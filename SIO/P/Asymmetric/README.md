## Asymmetric

# Encript RSA
```bash
python3 generator.py > keypair.pem
```

BASE 64, who dat?

```bash
python3 pub_enc.py keypair.pem
```

```bash
python3 pub_enc.py keypair.pem < input 
```

```bash
python3 pub_enc.py keypair.pem < input > output2
````

chmod u+x priv_dec.py 


dd if=/dev/zero bs=1 count=190 > long_input
od -x long_input 
