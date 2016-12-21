# BDL_7Chan
**Engine API version**: `2.0.0`

A 7Chan engine for BDL.


## Installation
```shell
$> git clone https://github.com/Wawachoo/BDL_7Chan
$> cd BDL_7Chan
$> python3.5 setup.py install
```


## Supported URLs
This engine supports URL of type `https://7chan.org/SECTION/res/THREAD_ID`.


## Repository name
The engine returns the thread name from from the thread page.


## Metadata
This engine export the following metadata:
* `{thread_section}`: thread section (ex: `g`);
* `{thread_name}`: thread name (ex: `the name of the thread`);
* `{thread_id}`: thread identifier (ex: `1234567`)
