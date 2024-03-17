# PythonHornDesign
Python based acoustic horn design utility. 



## Latest
[See DEVELOP branch for latest...](https://github.com/kurtjcu/PythonHornDesign/tree/develop)


## Installation
```bash

mamba create -n phorndesign python=3.10
mamba activate phorndesign

mamba install -c conda-forge numpy scipy matplotlib gmsh plotly pandoc

git submodule add https://github.com/rocapp/desmos2python.git
cd desmos2python
python3 -m pip install .
```

## Stage 1
- [x] Setup project repo
- [ ] Implement OS waveguide curve
- [ ] Rotate curve to generate waveguide
- [ ] Export mesh of wavewguide
- [ ] Export stl of waveguide
 

## Licence
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

## Developing

### Methodology
This repo uses a git-flow branching methodology. The master branch is the stable release branch. The develop branch is the current development branch. Feature branches are created from the develop branch and merged back into the develop branch. When a release is ready, the develop branch is merged into the master branch and tagged with the release number. It is likely that a release may take a long time to be ready, so the master branch may be behind the develop branch for a long time( or forever...:) ). 

### Environment
I am developing on Ubuntu and WSL using mamba(conda) to manage python packages and environment(s).

