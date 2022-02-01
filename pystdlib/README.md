# PYSTDLIB #
My personal convenience classes, functions and whatnots. Named after the C standard library, because I'm too lazy to be original.<br>


## Notes #
Only tested on Python 3.10.1! (Should run on any Python 3.x versions tho)<br>


## Installation #
 ### Normal installation #
  To install pystdlib just to use it, run:<br>
  > Windows:<br>
  >>`py -m pip install pystdlib`<br>
  >
  > MacOS & Linux:<br>
  >>`python3 -m pip install pystdlib`<br>
 
 ### Developer installation #
  To install pystdlib with the needed development packages, run:<br>
  > Windows:<br>
  >> `py -m pip install -e .[dev]`<br>
  >
  > MacOS & Linux:<br>
  >> `python3 -m pip install -e .[dev]`<br>
 


## Documentation #
> module `pystdlib`:<br>
>> class `pystdlib.Iota`:<br>
>> A Python implementation of the `iota` keyword in Go.<br>
>>> int `Iota.iota_counter`:<br>
>>> Integer representing the current value of the `Iota` instance.<br>
>>><br>
>>> function `Iota.iota()`:<br>
>>> Return the current value of `Iota.iota_counter` and increment<br>
>>> <br>
>>> function `Iota.reset()`:<br>
>>> Reset the value of `Iota.iota_counter`
><br>
>
>> function `pystdlib.hcf(msg:str = '', die:bool = False) -> NoReturn`:<br>
>> Halt and Catch Fire.<br>
>> Depending on `die`:<br>
>>- if `die` is set, then print `msg` and exit with code 1;
>>- else assert `False` with message `msg`.

<br><br>

## Examples #
```python
>>> import pystdlib as std
>>> i = std.Iota() # examples for the Iota instance
>>> i.iota() # iota_counter is now 1
0
>>> i.iota() # iota_counter is now 2
1
>>> i.iota_counter # iota_counter is now 2 (as demonstrated)
2
>>> i.reset()
>>> i.iota_counter
0
>>>
>>>
>>>  hcf(msg = "Look, it's an assertion!")
Traceback (most recent call last):
File "<stdin>", line 1, in  <module>
AsserionError: Look, it's an assertion!
>>>  hcf(die = True)

[Program finished with  exit code 1]
```
