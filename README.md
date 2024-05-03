# qubes-clean
Removes all unsafe characters from the Qubes global clipboard

#### Installation

Simply copy this script into dom0 as `/usr/local/bin/clean.py`, then mark it as executable using `chmod +x /usr/local/bin/clean.py`

You should then be able to run the script simply by typing `clean.py` into a terminal in dom0. Optionally, you can bind this script to a keybind in dom0

### How to copy files to dom0

The Qubes official documentation has information about copying files to dom0: https://www.qubes-os.org/doc/how-to-copy-from-dom0/#copying-to-dom0

For better security, you should download this into a disposable VM, to prevent a compromised qube from tampering with the data locally

For the best security, you should type this script manually into dom0. You can verify that you copied the script correctly by running `b2sum /usr/local/bin/clean.py` and comparing with the following hash:

```
cfd25c7483b721ac0bf4009b5c4d23c045c1b7eb5a38e8bc707deae1ceb32c05c6fd5b58ffd1344499c789801c1f1abbe6d233280d5e6201d32a501c7864a2e3  /usr/local/bin/clean.py
```
