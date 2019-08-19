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

<sub>supersonic.</sub>
<strong>supersonic(total=100, pdigits=1, ascii=True, bar_length=15)</strong><br/>
<sub>supersonic.</sub>
<strong>sonic(total=100, pdigits=1, ascii=True, bar_length=15)</strong>

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
<sub>supersonic.</sub>
<strong>custom(*arrangement, total=100)</strong>

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

## Properties
### current
Current progress.

## Methods
<strong>show()</strong>, <strong>update()</strong>

Clear last status and show.

<strong>clear()</strong>

Clear last status.

<strong>stat(stat)</strong>

Set status to a specific value `stat`.

<strong>progress(by=1)</strong>

Increase the current status by a specific value `by`.

<strong>done()</strong>

Finished task!

<hr/>
<sub>supersonic.ext.</sub>
<strong>Extension()</strong>

The base class for all Supersonic Extensions. If you want to make your own extensions, see here: [supersonic/exts/README.md](supersonic/exts/README.md)

<hr/>

Checkout my website at [http://www.WhatsYourIdea.com/](http://www.WhatsYourIdea.com/ "Website")
