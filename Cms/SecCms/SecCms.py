#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.SecCms import SecCmsRemoteCodeExecutionV6_45
from Cms.SecCms import SecCmsRemoteCodeExecutionV6_54
from Cms.SecCms import SecCmsRemoteCodeExecutionV6_55
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(SecCmsRemoteCodeExecutionV6_45.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SecCmsRemoteCodeExecutionV6_54.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(SecCmsRemoteCodeExecutionV6_55.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] SecCms component payload successfully loaded\033[0m")
    time.sleep(0.5)

