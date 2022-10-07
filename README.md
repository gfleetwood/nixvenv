# Overview

A command line interface for Virtual environments with nix. 

# Installation

`pip install git+https://github.com/gfleetwood/nixvenv`

# Usage

To initialize the package overall:

`nv_init`

This creates a path `$HOME/.config/nixvenv`, and puts all the current templates there. You can edit them to create your own.

To start a new environment run:

`nv_create LANGUAGE`


For your chosen language this copies the file from the config directory to your current directory and activates it. For example:

`nv_create python`

Copies the python nix shell template to your current directory and activates it.

