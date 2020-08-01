#!/usr/bin/env python3

from aws_cdk import core

from lib.cdkpipelines_demo_pipeline_stack import CdkpipelinesDemoPipelineStack


app = core.App()
CdkpipelinesDemoPipelineStack(app, "intro-cdkpipelines")

app.synth()
