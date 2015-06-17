############################################
Python Desktop Development Environment Setup
############################################

An opinionated series of Ansible Playbooks for creating a Python development
environment on an Ubuntu system.

===========
Assumptions
===========

These tasks have to assume some basic things.  Below is the list of these
assumptions:

* user is a sudoer
* the system being used is Ubuntu 14.04 or greater (the only system this is
  being built on)
* Python 2.6 or Python 2.7 are the default on the system
  * This is a ansible requirement, once ansible runs on Python 3 this will
    change
* The user has enough space in their home directory to support the files and
  is willing to have the following files in their home directory changed:
  * bashrc
  * condarc
  * vimrc