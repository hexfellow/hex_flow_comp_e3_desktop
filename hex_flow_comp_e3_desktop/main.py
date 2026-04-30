#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2026 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2026-04-28
################################################################

from .comp_e3_desktop import HexFlowCompE3Desktop


def main():
    comp = HexFlowCompE3Desktop()
    comp.start()
    comp.run()


if __name__ == "__main__":
    main()
