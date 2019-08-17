# Introduction

Supersonic is an Open-Source library for creating progress indicators (e.g. progress bars). It is super fast and super customizable.

# Getting Started

## Installation

Use this command to install Supersonic: `pip install supersonic`

After you have installed Supersonic, you can test if it has been successfully installed by running `import supersonic` in python. If Supersonic was installed successfully, it should show no errors.

## Example

```python

import supersonic as ss
import time

## Arguments
### t (the first argument) - Prefix text
### total - Total
### pdigits - Number of digits of the percentage to show
### ascii - True: Ascii, False: Unicode
### bar_length - Progress bar length
# Supersonic 1.2 now supports context managers!
with ss.sonic("Testing", total=1000, pdigits=1, ascii=False, bar_length=20) as p:
	for i in range(1000):
		p.progress() #or p.stat(i+1)
		time.sleep(0.01)

```

## Making Extensions

A great thing about Supersonic is that you can extend it's capability with Extensions. You can find out more about Extensions here: [supersonic/exts/README.md](supersonic/exts/README.md)

# Documentation

<span style="font-size:17px;">supersonic.</span>
<span style="font-size:25px;">supersonic(<span style="font-size:18px;">total=100, pdigits=1, ascii=True, bar_length=15</span>)</span><br/>
<span style="font-size:17px;">supersonic.</span>
<span style="font-size:25px;">sonic(<span style="font-size:18px;">total=100, pdigits=1, ascii=True, bar_length=15</span>)</span>

`supersonic.supersonic` is a wrapper around `supersonic.custom` that let's you create progress bars without creating your own layout. If you want full control over the final product, checkout `supersonic.custom`.

## Parameters
### total (Default: 100)
<div style="padding-left: 15px;">
Number of things or tasks you need to process.
</div>

### pdigits (Default: 1)
<div style="padding-left: 15px;">
How many digits to show in the percentage of completion.
</div>

### ascii (Default: True)
<div style="padding-left: 15px;">
Encoding of the Progress Indicator. Supersonic will use Ascii if this is True and use Unicode if this is False.
</div>

### bar_length (Default: 15)
<div style="padding-left: 15px;">
How long the progress bar should be.
</div>

<hr/>
<span style="font-size:17px;">supersonic.</span>
<span style="font-size:25px;">custom(<span style="font-size:18px;">*arrangement, total=100</span>)</span>

## Parameters
### *arrangement
<div style="padding-left: 15px;">
The arrangement(or layout) of the progress indicator. It can contain both Strings and Extensions.<br/><br/>
Example:<br/>

```python
supersonic.custom(Percentage(), " |", Bar(), "| done")
# Result: 
# 50% |##########          | done
```
</div>

### total (Default: 100)
<div style="padding-left: 15px;">
Number of things or tasks you need to process.
</div>

<hr/>
<span style="font-size:17px;">supersonic.ext.</span>
<span style="font-size:25px;">Extension()</span>

The base class for all Supersonic Extensions. If you want to make your own extensions, see here: [supersonic/exts/README.md](supersonic/exts/README.md)

<hr/>

Checkout my website at [http://www.WhatsYourIdea.com/](http://www.WhatsYourIdea.com/ "Website")
