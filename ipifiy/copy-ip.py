#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyperclip, winsound, ipify

pyperclip.copy(ipify.get_ip())

winsound.MessageBeep()