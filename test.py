#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

#import principal
import principal

errors = 0
success = 0

print("Executando somar, 1 + 1 deve ser = 2")
if principal.somar(1,1) != 2:
    print("Deu merda")
    errors += 1
else:
    print("Deu certo")
    success += 1

print("Executando subtrair, 1 - 1 deve ser = 0")
if principal.subtrair(1,1) != 0:
    print("Deu merda")
    errors += 1
else:
    print("Deu certo")
    success += 1


print("Passaram: ", success)
print("Quebraram: ", errors)
if errors > 0:
    sys.exit(1)
