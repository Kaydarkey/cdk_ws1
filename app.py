#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_ws1.cdk_ws1_stack import CdkWs1Stack


app = cdk.App()
CdkWs1Stack(app, "CdkWs1Stack")

app.synth()
