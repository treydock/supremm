#!/usr/bin/env python
""" Timeseries generator module """

from supremm.plugin import RateConvertingTimeseriesPlugin
import numpy

class InfiniBandTimeseries(RateConvertingTimeseriesPlugin):
    """ Generate the infiniband usage as a timeseries data """

    name = property(lambda x: "ib_lnet")
    metric_system = property(lambda x: "pcp")
    mode = property(lambda x: "timeseries")
    requiredMetrics = property(lambda x: ["infiniband.port.switch.in.bytes", "infiniband.port.switch.out.bytes"])
    optionalMetrics = property(lambda x: [])
    derivedMetrics = property(lambda x: [])

    def __init__(self, job, config):
        super(InfiniBandTimeseries, self).__init__(job, config)

    def computetimepoint(self, data):
        return (numpy.sum(data[0]) + numpy.sum(data[1])) / 1048576.0
