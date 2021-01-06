# cypher-session
A collection of classical cyphers that encrypts or decrypts messages.
![Screenshot](https://github.com/binarynil/cypher-session/raw/main/gif/cyphergif.gif)

### Cyphers
- Autokey
- Atbash
- Baconian
- Beaufort
- Caesar
- ROT13
- Running Key
- Vignere

### Examples
#### Encryption
```
auto -e somekey hello
```
#### Decryption
```
vig -d somekey world
```
Some ciphers don't need the encryption or decryption flags
```
rot13 sometext
```
