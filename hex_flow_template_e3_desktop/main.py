#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2026 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2026-04-28
################################################################

from .template_e3_desktop import HexFlowTemplateE3Desktop


def main():
    template = HexFlowTemplateE3Desktop()
    template.start()
    template.run()


if __name__ == "__main__":
    main()
