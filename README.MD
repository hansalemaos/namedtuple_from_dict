# namedtuple from dict / valid identifier from string 


```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install namedtuple-from-dict

from namedtuple_from_dict import create_valid_identifier, dict_to_namedtuple

from string import printable
from random import choices, randrange

# startwith will be added if the original string starts with a number
# 9times6 -> aa_9times6

testdict = {
    1: "hallo",
    "n k q": 223,
    (1, 2, 4): {222, 333},
    "validkey1": "test",
    "validkey2": "tes1t",
    "notvalidkey!1": "tes1t",
}

testtuple = dict_to_namedtuple(dic=testdict, name="testdata", startwith="aa_")

print(testtuple)
for i in range(10):
    randomchars = "".join(choices(printable, k=randrange(3, 10)))
    varname = create_valid_identifier(randomchars, startwith="aa_")
    print(f"{randomchars=}")
    print(f"{varname=}")


# testdata(aa_1='hallo', n_k_q=223, aa_1_2_4={333, 222}, validkey1='test', validkey2='tes1t', notvalidkey_1='tes1t')
# randomchars=':ga(F'
# varname='ga_F'
# randomchars='lh[)iN>A/'
# varname='lh_iN_A'
# randomchars='fI&mE)'
# varname='fI_mE'
# randomchars='//YW'
# varname='YW'
# randomchars='aY\x0c'
# varname='aY'
# randomchars='k|\ts \x0b'
# varname='k_s'
# randomchars='!kGhJ`'
# varname='kGhJ'
# randomchars='8u*s'
# varname='aa_8u_s'
# randomchars='\\z;_cP'
# varname='z__cP'
# randomchars='e)=Qb\t7p'
# varname='e_Qb_7p'

	
```




