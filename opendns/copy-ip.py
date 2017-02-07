#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dns.resolver, pyperclip, winsound

def get_ip():
	resolver = dns.resolver.Resolver()
	resolver.nameservers = ['208.67.222.222', '208.67.220.220']
	answer = resolver.query("myip.opendns.com", "A")
	for rdata in answer:
		return rdata

pyperclip.copy(str(get_ip()))

winsound.MessageBeep()