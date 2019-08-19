# Intro to Supersonic Extensions

A great thing about Supersonic is that you can extend it's capability with Extensions. The Extensions API is designed to be flexible and intuitive.

# Getting Started with Building Extensions

Let's build a simple extension that outputs the current status and the total. All extensions need to extend the `Extension` class, so let's import that first. We will also import the `test` function so that we can test the extension later. 

```python
from supersonic.ext import Extension, test
```

Then let's extend the `Extension` class. We will just put in `pass` for the content of the class for now.

```python
class HelloWorldExtension(Extension):
    pass
```

Now let's talk about the Extensions API.<br/>
There are 3 methods that you can override in `Extension`.

- `__init__()`  
Called by **the user** when they create an instance of an extension.

- `conf(total)`  
Called by **Supersonic** to configure the extension.

- `stat_update(current)`  
Called by **Supersonic** to get an updated status string.

There is also a special instance variable that is set by Supersonic called `total`. It is an int that stores the total. You can access it in both the `conf` method and the `stat_update` method.

When overriding these methods, you always need to call `super([your class name], self).[method name goes here]([parameters goes here])` before doing anything inside your custom method.<br/>
You cannot change the parameters of methods called by Supersonic, but the parameters of methods called by the user can be changed.

Now let's write the code for our simple extension and finish it off! Remove `pass` and write the following:

```python
class HelloWorldExtension(Extension):
    # This method will be called by the user
    def __init__(self, join_str="out of", unit="items"):
        # Don't forget this line
        super(HelloWorldExtension, self).__init__()
        self.join_str = join_str
        self.unit = unit

    # This method will be called by Supersonic to get the status string
    def stat_update(self, current):
        # Don't forget this line
        super(HelloWorldExtension, self).stat_update(current)
        # This returned string will be displayed to the user
        return str(current) + " " + self.join_str + " " + str(self.total) + " " + self.unit
```

And we are done! Let's test it out.

```python
test(HelloWorldExtension())
```

# Documentation

<sub>supersonic.ext.</sub>
<strong>Extension()</strong>

The base class for all Supersonic Extensions. If you want to make your own extensions, see here: [Getting Started with Building Extensions](#getting-started-with-building-extensions)

## Overridable methods
- `__init__()`  
Called by the user when they create an instance of an extension. Parameters can be changed.

- `conf(total)`  
Called by Supersonic to configure the extension. Parameters cannot be changed.  
**Parameters**  
    - total  
    The total number of things or tasks the user needs to process.

- `stat_update(current)`  
Called by Supersonic to get an updated status string. Parameters cannot be changed.  
**Parameters**  
    - current  
    The current status.

## Properties
- `total`  
The total number of things or tasks the user needs to process. Set by Supersonic. Can be accessed from `conf(total)` and `stat_update(current)`.

<hr/>
<sub>supersonic.exts.bar.</sub>
<strong>Bar(progress_charset=CHARSET_DEFAULT, placeholder=" ", length=20)</strong><br/>
<sub>supersonic.exts.</sub>
<strong>Bar(progress_charset=CHARSET_DEFAULT, placeholder=" ", length=20)</strong>

A built-in extension for progress bars. You can change what the progress bar displays by setting `progress_charset` and `placeholder`. See more about these parameters in the Parameters section.

## Parameters
### progress_charset (Default: CHARSET_DEFAULT)
<div style="padding-left: 15px;">
What the progress bar displays for complete parts of the bar. This should be a list or a tuple.<br/>
Supersonic will cycle through all characters in the charset and display it to the user for the first block. Then when the cycle is over, it will go on to the next block and leave the first block with the last character in the charset.<br/>
Built-in charsets:<br/>

```
Bar.CHARSET_DEFAULT          #
Bar.CHARSET_NUMERIC          1 2 3 4 5 6 7 8 9 #
Bar.CHARSET_ARROW            > =
Bar.CHARSET_UNICODE_BLOCK    █
Bar.CHARSET_UNICODE_SMOOTH   ▏ ▎ ▍ ▌ ▋ ▊ ▉ █
```
</div>

### placeholder (Default: " ")
<div style="padding-left: 15px;">
What the progress bar displays for uncomplete parts of the bar.
</div>

### length (Default: 20)
<div style="padding-left: 15px;">
Length of the progress bar.
</div>

<hr/>
<sub>supersonic.exts.eta.</sub>
<strong>Eta(alpha=4)</strong><br/>
<sub>supersonic.exts.</sub>
<strong>Eta(alpha=4)</strong>

A built-in extension for calculating and displaying an estimate of the remaining time. Change `alpha` to change how far Supersonic will remember into the past.

## Parameters
### alpha (Default: 4)
<div style="padding-left: 15px;">
How far Supersonic will remember into the past.
</div>

<hr/>
<sub>supersonic.exts.identity.</sub>
<strong>Total()</strong><br/>
<sub>supersonic.exts.</sub>
<strong>Total()</strong>

A built-in extension for showing the total.

<hr/>
<sub>supersonic.exts.identity.</sub>
<strong>Current()</strong><br/>
<sub>supersonic.exts.</sub>
<strong>Current()</strong>

A built-in extension for showing the current status.

<hr/>
<sub>supersonic.exts.identity.</sub>
<strong>Fraction()</strong><br/>
<sub>supersonic.exts.</sub>
<strong>Fraction()</strong>

A built-in extension for showing the current status and the total as a fraction.

<hr/>
<sub>supersonic.exts.percentage.</sub>
<strong>Percentage(digits=0)</strong><br/>
<sub>supersonic.exts.</sub>
<strong>Percentage(digits=0)</strong>

A built-in extension for calculating and displaying an estimate of the remaining time. Change `digits` to change how many digits of the percentage Supersonic will show.

## Parameters
### digits (Default: 0)
<div style="padding-left: 15px;">
How many digits of the percentage Supersonic will show.
</div>

<hr/>

Checkout my website at [http://www.WhatsYourIdea.com/](http://www.WhatsYourIdea.com/ "Website")
