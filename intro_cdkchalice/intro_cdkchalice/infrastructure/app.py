#!/usr/bin/env python3
"""
Name: app.py
Created by: Masato Shima
Created on: 2021/01/31
Description: app.py
"""

from aws_cdk import core as cdk
from stacks.chaliceapp import ChaliceApp

app = cdk.App()

ChaliceApp(
	app,
	"cdk-intro-cdkchalice"
)

app.synth()

# End
